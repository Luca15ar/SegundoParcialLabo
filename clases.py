import pygame
import random

class Nave:
#===========================================Inicializo la clase=========================================================
    def __init__(self, x, y, nombre, escala, velocidad = None, sonido = None) -> None:
        self.nombre = nombre
        self.lista_animacion = []
        self.frame_index = 0
        self.accion = 0 #0 -> Inactivo 1-> Muerto
        self.tiempo_actualizacion = pygame.time.get_ticks()

        #Cargo las imagenes de inactivo
        lista_temp = []

        for i in range(12):
            img = pygame.image.load(f"Segundo_Parcial/Img_juego/{self.nombre}/Idle/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala))
            lista_temp.append(img)

        self.lista_animacion.append(lista_temp)

        #Cargo las imagenes de muerte
        lista_temp = []

        for i in range(12):
            img = pygame.image.load(f"Segundo_Parcial/Img_juego/{self.nombre}/Explosion-sprite/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 1, img.get_height() * 1))
            lista_temp.append(img)

        self.lista_animacion.append(lista_temp)
        self.image = self.lista_animacion[self.accion][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.posicion_original = (self.rect.centerx, self.rect.centery)
        self.lista_disparos = []
        self.vivo = True
        self.mostrar_nave = True
        self.velocidad = velocidad
        self.sonido = sonido
        self.sonido_sonando = False
        self.tiempo_ultimo_disparo = 0

#===============================================Métodos=================================================================
    def shoot(self, x, y, tiempo_actual):
        if(tiempo_actual - self.tiempo_ultimo_disparo >= 1000 and self.vivo == True):
            proyectil = Proyectil(x, y, "Segundo_Parcial/Img_juego/Nave/Shoot-sprite", True, 5, 0.5)
            self.lista_disparos.append(proyectil)
            self.sonido.play()
            self.tiempo_ultimo_disparo = tiempo_actual
    
    def movement(self):
        #=========================================Mientras esté vivo====================================================
        if(self.vivo):
            keys = pygame.key.get_pressed()
            
            #===============================Verifico cual tecla presionó================================================
            if(keys[pygame.K_a] and self.rect.x > 0):
                self.rect.x -= self.velocidad

            if(keys[pygame.K_d] and self.rect.x < 400 - self.image.get_width()):
                self.rect.x += self.velocidad

    def update(self):
        animacion_coldown = 100
        self.image = self.lista_animacion[self.accion][self.frame_index]

        if(pygame.time.get_ticks() - self.tiempo_actualizacion > animacion_coldown):
            self.tiempo_actualizacion = pygame.time.get_ticks()
            self.frame_index += 1
        
        #==============================Verifico que el recorrido no se pase del tamaño de la animación==================
        if(self.frame_index >= len(self.lista_animacion[self.accion])):
            self.frame_index = 0

            if(self.accion == 1):
                self.mostrar_nave = False

    def draw(self, superficie):
        #========================================Plasmar la imagen======================================================
        if(self.mostrar_nave):
            if(self.vivo):
                superficie.blit(self.image, self.rect)
                
            else:
                #=============================Reproducción del sonido===================================================
                if(not self.sonido_sonando):
                    self.sonido.play()
                    self.sonido_sonando = True

                #==============================Animación de muerte======================================================   
                self.image = self.lista_animacion[self.accion][self.frame_index]
                self.rect = self.image.get_rect()
                self.rect.center = self.posicion_original
                superficie.blit(self.image, self.rect)
                
class Nave_Enemiga(Nave):
    def __init__(self, x, y, nombre, escala, velocidad = None, sonido = None):
        super().__init__(x, y, nombre, escala, velocidad, sonido)
        self.derecha = True
        self.contador = 0
        self.max_descenso = self.rect.top + 25
        self.tiempo_enfriamiento = 2000 
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        super().update()
        self.movimiento()

    def movimiento(self):
        if(self.contador < 3):
            self.lateral_movement()
        else:
            self.descenso()
    def descenso(self):
        if(self.max_descenso == self.rect.top):
            self.contador = 0
            self.max_descenso = self.rect.top + 25
        else:
            self.rect.top += 1

    def lateral_movement(self):
        if(self.derecha):
            self.rect.left += self.velocidad
            if(self.rect.left > 300):
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left -= self.velocidad
            if(self.rect.left < 0):
                self.derecha = True

    def auto_shoot(self, tiempo_actual):
        if tiempo_actual - self.tiempo_ultimo_disparo > self.tiempo_enfriamiento:
            proyectil = Proyectil(self.rect.centerx, self.rect.bottom, "Segundo_Parcial/Img_juego/Enemy-ship-1/Shoot-sprite-enemy", False, 5, 0.5)
            self.lista_disparos.append(proyectil)
            self.tiempo_ultimo_disparo = tiempo_actual

class Proyectil:
#===========================================Inicializo la clase=========================================================
    def __init__(self, x, y, ruta, personaje, velocidad, escala) -> None:
        self.ruta = ruta
        self.lista_animacion = []
        self.frame_index = 0
        self.tiempo_actualizacion = pygame.time.get_ticks()

        for i in range(6):
            img = pygame.image.load(f"{self.ruta}/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * escala, img.get_height() * escala))
            img = pygame.transform.rotate(img, 55)
            self.lista_animacion.append(img)

        self.image = self.lista_animacion[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = velocidad
        self.disparo_personaje = personaje
#===============================================Métodos=================================================================
    def update(self):
        animacion_coldown = 100
        self.image = self.lista_animacion[self.frame_index]

        if(pygame.time.get_ticks() - self.tiempo_actualizacion > animacion_coldown):
            self.tiempo_actualizacion = pygame.time.get_ticks()
            self.frame_index += 1
        
        if(self.frame_index >= len(self.lista_animacion)):
            self.frame_index = len(self.lista_animacion) - 1

        if(self.disparo_personaje):
            self.rect.y -= self.velocidad
        else:
            self.rect.y += self.velocidad

    def colision_nave(self, nave):
        retorno = False
        #=====================================Verifico si hubo una colisión=============================================
        if(self.rect.colliderect(nave.rect)):
            retorno = True

        return retorno

    def draw(self, surface):
        #=================================Plasmar la imagen=============================================================
        surface.blit(self.image, self.rect)

class Boton:
#===========================================Inicializo la clase=========================================================
    def __init__(self, x, y, imagen, escala) -> None:
        ancho = imagen.get_width()
        altura = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(altura * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clickeo = False

#===============================================Métodos=================================================================
    def draw(self, superficie):
        accion = False
        #===========================Obtengo la posición del mouse=======================================================
        pos = pygame.mouse.get_pos()

        #=====================Reviso si hizo click en la posicion del boton=============================================
        if(self.rect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0] == 1 and self.clickeo == False):
                self.clickeo = True
                accion = True

        #==================Si suelta el click cambio la bandera a que no clickeó========================================
        if(pygame.mouse.get_pressed()[0] == 0):
            self.clickeo = False

        #=================================Plasmar la imagen=============================================================
        superficie.blit(self.imagen, (self.rect.x, self.rect.y))

        return accion