"""
Segundo Parcial
Luca Areco
45.284.179
1J
"""

#===========================================Importar bibliotecas========================================================
import pygame
from clases import Nave
from clases import Nave_Enemiga
from clases import Boton
from colores import WHITE
from colores import BLACK

#===========================================Constantes y variables======================================================
ANCHO_PANTALLA = 400
ALTURA_PANTALLA = 800
SCORE = 0

#=======================================Configuracion de pantalla, titulo e icono=======================================
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTURA_PANTALLA))
pygame.display.set_caption("Space Runner")
icono = pygame.image.load("Segundo_Parcial\Img_juego\Space_ship.png")
pygame.display.set_icon(icono)
icono = pygame.transform.scale(icono, (300, 300))

#=============================================Configuración del tiempo==================================================
fps = 60
reloj = pygame.time.Clock()

#===========================================Subo las imagenes del fondo=================================================
fondo_back = pygame.image.load("Segundo_Parcial\Img_juego\space-background-back.png")
fondo_back = pygame.transform.scale(fondo_back, (ANCHO_PANTALLA, ALTURA_PANTALLA))
fondo_front = pygame.image.load("Segundo_Parcial\Img_juego\space-background-front.png")
fondo_front = pygame.transform.scale(fondo_front, (ANCHO_PANTALLA, 400))
y = 0

#========================================Inicializo las funciones de pygame=============================================
pygame.init()
pygame.font.init()
pygame.mixer.init()

#==============================================Configuración del sonido=================================================
pygame.mixer.music.load("Segundo_Parcial\Sonidos\musica-espacial.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.03)
sonido_proyectil = pygame.mixer.Sound("Segundo_Parcial\Sonidos\proyectil.ogg")
pygame.mixer.Sound.set_volume(sonido_proyectil, 0.03)
sonido_explosion = pygame.mixer.Sound("Segundo_Parcial\Sonidos\explosion.wav")
pygame.mixer.Sound.set_volume(sonido_explosion, 0.03)

#==============================================Titulos y textos=========================================================
fuente = pygame.font.Font("Segundo_Parcial\Fuente\Starjedi.ttf", 50)
fuente2 = pygame.font.Font("Segundo_Parcial\Fuente\Starjedi.ttf", 20)
titulo1 = fuente.render("SPACE", True, WHITE)
titulo2 = fuente.render("RUNNERS", True, WHITE)

#==================================================Banderas=============================================================
mostrar_titulo = True
mostrar_objetos = False
pausa = False
game_over = False
colisiono = False
#==============================================Creo las instancias======================================================

            #=======================================Personajes============================================
nave_icon = Nave(200, 600, "Nave", 0.5)
nave = Nave(200, 700, "Nave", 0.2, 5, sonido_proyectil)

nave_enemiga_1 = Nave_Enemiga(100, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_2 = Nave_Enemiga(200, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_3 = Nave_Enemiga(300, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)

oleada_uno = []
oleada_uno.append(nave_enemiga_1)
oleada_uno.append(nave_enemiga_2)
oleada_uno.append(nave_enemiga_3)

nave_enemiga_4 = Nave_Enemiga(100, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_5 = Nave_Enemiga(200, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_6 = Nave_Enemiga(300, 100, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_7 = Nave_Enemiga(100, 200, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_8 = Nave_Enemiga(200, 200, "Enemy-ship-1", 0.1, 1, sonido_explosion)
nave_enemiga_9 = Nave_Enemiga(300, 200, "Enemy-ship-1", 0.1, 1, sonido_explosion)

oleada_dos = []
oleada_dos.append(nave_enemiga_4)
oleada_dos.append(nave_enemiga_5)
oleada_dos.append(nave_enemiga_6)
oleada_dos.append(nave_enemiga_7)
oleada_dos.append(nave_enemiga_8)
oleada_dos.append(nave_enemiga_9)

            #=========================================Botones=============================================
empezar_img = pygame.image.load("Segundo_Parcial\Img_juego\Boton_empezar.png").convert_alpha()
empezar_btn = Boton(130, 300, empezar_img, 0.2)

#===============================================Lógica del juego========================================================
run = True
while run:
    tiempo_actual = pygame.time.get_ticks()
    
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            run = False

    #===========================================Disparo de la nave======================================================
        if evento.type == pygame.MOUSEBUTTONDOWN and mostrar_objetos:
            pos_x = nave.rect.centerx
            pos_y = nave.rect.top
            nave.shoot(pos_x, pos_y, tiempo_actual)

        keys = pygame.key.get_pressed()

    #============================================Pausa del juego========================================================
        if(keys[pygame.K_ESCAPE]):
            pausa = not pausa
            pygame.mixer.music.pause()

    #=========================================Movimiento de la nave=====================================================    
        nave.movement()
            
    #=========================Si se pausó, se detiene el juego hasta que se reanude=====================================
    if(pausa):
        pausa_texto = fuente.render("Pausa", True, WHITE)
        rect_pausa = pausa_texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTURA_PANTALLA // 2))
        pantalla.blit(pausa_texto, rect_pausa)

    else:
        #======================Mientras no esté pausado se seguira actualizando el juego================================
        if(not pausa):
            pygame.mixer.music.unpause()

            #==============================================Fondo========================================================
            y_relativa = y % fondo_back.get_rect().height
            pantalla.blit(fondo_back, (0, y_relativa - fondo_back.get_rect().height))

            if(y_relativa < ALTURA_PANTALLA):
                pantalla.blit(fondo_back, (0, y_relativa))

            y += 5

            #========================================Pantalla principal=================================================
            if(mostrar_titulo):
                pantalla.blit(titulo1, (110, 50))
                pantalla.blit(titulo2, (80, 100))
                nave_icon.update()
                nave_icon.draw(pantalla)
                
                if(empezar_btn.draw(pantalla) == True):
                    mostrar_titulo = False
                    mostrar_objetos = True

            #========================================Pantalla de partida================================================
            if(mostrar_objetos):
                texto = fuente2.render(f"Score: {SCORE}", True, WHITE) 
                pantalla.blit(texto, (10, 10))
                nave.update()
                nave.draw(pantalla)

                for nave_enemiga in oleada_uno:
                    nave_enemiga.update()
                    nave_enemiga.draw(pantalla)
                    nave_enemiga.auto_shoot(tiempo_actual)

                if(len(oleada_uno) == 0):
                    for nave_enemiga in oleada_dos:
                        nave_enemiga.update()
                        nave_enemiga.draw(pantalla)
                        nave_enemiga.auto_shoot(tiempo_actual)

            #====================================Verifico que la nave tenga diparos=====================================
            if(len(nave.lista_disparos) > 0):
                for elemento in nave.lista_disparos:
                    elemento.update()
                    elemento.draw(pantalla)

                    if(len(oleada_uno) > 0):
                        # for nave_enemiga in oleada_uno:
                        #     for proyectil in nave_enemiga.lista_disparos:
                        #         proyectil.update()
                        #         proyectil.draw(pantalla)

                        #         if(proyectil.colision_nave(nave)):
                        #             nave.vivo = False
                        #             nave.accion = 1
                        #             colisiono = True

                        #         if(proyectil.rect.top > 750 or colisiono):
                        #             nave_enemiga.lista_disparos.remove(proyectil)
                        #             colisiono = False

                        #         if(not nave.vivo):
                        #             game_over = True

                        #     if(elemento.colision_nave(nave_enemiga)):
                        #         nave_enemiga.vivo = False
                        #         nave_enemiga.accion = 1
                        #         colisiono = True
                        #         SCORE += 100
                                
                        #     if(not nave_enemiga.mostrar_nave):
                        #         oleada_uno.remove(nave_enemiga)
                        #         nave_enemiga.rect = pygame.Rect(0, 0, 0, 0)
                        # Verificar colisión y actualizar proyectiles de la nave enemiga
                        for nave_enemiga in oleada_uno:
                            for proyectil in nave_enemiga.lista_disparos:
                                proyectil.update()
                                proyectil.draw(pantalla)

                                # Verificar colisión con la nave del jugador
                                if proyectil.colision_nave(nave):
                                    nave.vivo = False
                                    nave.accion = 1
                                    colisiono = True

                                # Verificar límite de la pantalla y eliminar proyectiles
                                if proyectil.rect.top > 750 or colisiono:
                                    nave_enemiga.lista_disparos.remove(proyectil)
                                    colisiono = False

                                # Verificar si la nave del jugador sigue viva
                                if not nave.vivo:
                                    game_over = True

                            # Verificar colisión con la nave enemiga y eliminarla si corresponde
                            if elemento.colision_nave(nave_enemiga):
                                nave_enemiga.vivo = False
                                nave_enemiga.accion = 1
                                colisiono = True
                                SCORE += 100

                            # Verificar si la nave enemiga debe ser eliminada
                            if not nave_enemiga.mostrar_nave:
                                oleada_uno.remove(nave_enemiga)
                                nave_enemiga.rect = pygame.Rect(0, 0, 0, 0)

                    elif(len(oleada_dos) > 0):
                        for nave_enemiga in oleada_dos:

                            for proyectil in nave_enemiga.lista_disparos:
                                proyectil.update()
                                proyectil.draw(pantalla)

                                if(proyectil.colision_nave(nave)):
                                    nave.vivo = False
                                    nave.accion = 1
                                    colisiono = True

                                if(proyectil.rect.top > 750 or colisiono):
                                    nave_enemiga.lista_disparos.remove(proyectil)
                                    colisiono = False
                                
                                if(not nave.vivo):
                                    game_over = True

                            if(elemento.colision_nave(nave_enemiga)):
                                nave_enemiga.vivo = False
                                nave_enemiga.accion = 1
                                colisiono = True
                                SCORE += 150

                            if not nave_enemiga.mostrar_nave:
                                oleada_dos.remove(nave_enemiga)
                                nave_enemiga.rect = pygame.Rect(0, 0, 0, 0)
                            

                    if(elemento.rect.top < 80 or colisiono):
                        nave.lista_disparos.remove(elemento)
                        colisiono = False

    if(game_over):
        mostrar_titulo = False
        mostrar_objetos = False
        game_over_texto = fuente.render("Game Over", True, WHITE)
        rect_game_over = game_over_texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTURA_PANTALLA // 2))
        pantalla.blit(game_over_texto, rect_game_over)

    #=============================================Actualizo la pantalla=================================================
    pygame.display.update()
    reloj.tick(fps)

#===========================================Finalizo las funciones de pygame============================================
pygame.mixer.music.stop()
pygame.quit()