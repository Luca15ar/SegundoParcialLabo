#===========================================Importar bibliotecas========================================================
import pygame
import sys
import csv
from clases import Nave
from clases import Nave_Enemiga
from clases import Boton
from colores import GRAY11
from colores import WHITE
from colores import YELLOW1

def space_runners_app():
    #===========================================Constantes y variables==================================================
    ANCHO_PANTALLA = 400
    ALTURA_PANTALLA = 800
    SCORE = 0
    ancho_cuadro = 80
    altura_cuadro = 50
    nombre = ""
    puntaje = 0

    #=======================================Configuracion de pantalla, titulo e icono===================================
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTURA_PANTALLA))
    pygame.display.set_caption("Space Runner")
    icono = pygame.image.load("Segundo_Parcial\Img_juego\Space_ship.png")
    pygame.display.set_icon(icono)
    icono = pygame.transform.scale(icono, (300, 300))

    #=============================================Configuración del tiempo==============================================
    fps = 60
    reloj = pygame.time.Clock()

    #===========================================Subo las imagenes del fondo=============================================
    fondo_back = pygame.image.load("Segundo_Parcial\Img_juego\space-background-back.png")
    fondo_back = pygame.transform.scale(fondo_back, (ANCHO_PANTALLA, ALTURA_PANTALLA))
    y = 0

    #========================================Inicializo las funciones de pygame========================================
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    #==============================================Configuración del sonido============================================
    pygame.mixer.music.load("Segundo_Parcial\Sonidos\musica-espacial.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.03)
    sonido_proyectil = pygame.mixer.Sound("Segundo_Parcial\Sonidos\proyectil.ogg")
    pygame.mixer.Sound.set_volume(sonido_proyectil, 0.03)
    sonido_explosion = pygame.mixer.Sound("Segundo_Parcial\Sonidos\explosion.wav")
    pygame.mixer.Sound.set_volume(sonido_explosion, 0.03)

    #================================================Titulos y textos==================================================
    fuente = pygame.font.Font("Segundo_Parcial\Fuente\Starjedi.ttf", 50)
    fuente2 = pygame.font.Font("Segundo_Parcial\Fuente\Starjedi.ttf", 20)
    titulo1 = fuente.render("SPACE", True, WHITE)
    titulo2 = fuente.render("RUNNERS", True, WHITE)

    #====================================================Banderas======================================================
    mostrar_titulo = True
    mostrar_objetos = False
    mostrar_puntajes = False
    pausa = False
    game_over = False
    win = False
    colisiono = False
    input_active = False
    puntaje_guardado = False

    #==============================================Creo las instancias=================================================

                #=======================================Personajes============================================
    nave_icon = Nave(200, 600, "Nave", 0.5)
    nave = Nave(200, 700, "Nave", 0.2, 10, sonido_proyectil)

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
    puntajes_img = pygame.image.load("Segundo_Parcial\Img_juego\Boton_puntajes.png").convert_alpha()
    puntajes_btn = Boton(130, 380, puntajes_img, 0.2)
    regresar_img = pygame.image.load("Segundo_Parcial\Img_juego\Boton_regresar.png").convert_alpha()
    regresar_btn = Boton(15, 15, regresar_img, 0.25)

                #=======================================Formulario============================================
    color_cuadro_input = GRAY11
    color_texto = WHITE
    fuente3 = pygame.font.Font("Segundo_Parcial\Fuente\Starjedi.ttf", 22)
    titulo3 = fuente3.render("ingrese nombre", True, WHITE)
    cuadro_input = pygame.Rect(50, 350, 300, 40)

    #===============================================Lógica del juego====================================================
    #Actualizar la pantalla
    pygame.display.flip()

    run = True
    while run:
        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if(evento.type == pygame.QUIT):
                run = False

        #===========================================Disparo de la nave==================================================
            elif(mostrar_objetos):
                if(evento.type == pygame.MOUSEBUTTONDOWN and nave.vivo and (win == False or game_over == False)):
                    pos_x = nave.rect.centerx
                    pos_y = nave.rect.top
                    nave.shoot(pos_x, pos_y, tiempo_actual)

            keys = pygame.key.get_pressed()

        #============================================Pausa del juego====================================================
            if(keys[pygame.K_ESCAPE]):
                pausa = not pausa
                pygame.mixer.music.pause()

        #===============================================Formulario======================================================
            elif(evento.type == pygame.KEYDOWN):
                if(input_active):
                    
                    if(evento.key == pygame.K_RETURN):
                        input_active = False
                        mostrar_objetos = True
                    elif(evento.key == pygame.K_BACKSPACE):
                        nombre = nombre[:-1]
                    else:
                        if len(nombre) < 5:
                            nombre += pygame.key.name(evento.key)

        #=========================================Movimiento de la nave=================================================
            nave.movement()
        
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
                    input_active = True
                    nombre = ""

                if(puntajes_btn.draw(pantalla) == True):
                    mostrar_titulo = False
                    mostrar_puntajes = True

            #========================================Pantalla de partida================================================
            elif(mostrar_objetos):
                texto = fuente2.render(f"Score: {SCORE}", True, WHITE) 
                pantalla.blit(texto, (10, 10))
                nave.update()
                nave.draw(pantalla)

                for nave_enemiga in oleada_uno:
                    nave_enemiga.update()
                    nave_enemiga.draw(pantalla)

                if(len(oleada_uno) == 0):
                    for nave_enemiga in oleada_dos:
                        nave_enemiga.update()
                        nave_enemiga.draw(pantalla)

                #====================================Verifico que la nave tenga diparos=================================
                if len(nave.lista_disparos) > 0:
                    for proyectil in nave.lista_disparos:
                        proyectil.update()
                        proyectil.draw(pantalla)

                        if(proyectil.rect.top < 80 or colisiono):
                            nave.lista_disparos.remove(proyectil)
                            colisiono = False
                        
                        #===========================Verifico la colision contra la nave enemiga=========================
                        if(len(oleada_uno) > 0):
                            for nave_enemiga in oleada_uno:
                                if(proyectil.colision_nave(nave_enemiga)):
                                    nave_enemiga.accion = 1
                                    colisiono = True
                                    SCORE += 100

                                if(not nave_enemiga.mostrar_nave):
                                    oleada_uno.remove(nave_enemiga)
                                    nave_enemiga.rect = pygame.Rect(0, 0, 0, 0)

                        #===========================Verifico la colision contra la nave enemiga=========================
                        if(len(oleada_uno) == 0):
                            for nave_enemiga in oleada_dos:
                                if(proyectil.colision_nave(nave_enemiga)):
                                    nave_enemiga.accion = 1
                                    colisiono = True
                                    SCORE += 100

                                if(not nave_enemiga.mostrar_nave):
                                    oleada_dos.remove(nave_enemiga)
                                    nave_enemiga.rect = pygame.Rect(0, 0, 0, 0)

                for nave_enemiga in oleada_uno:
                    if(len(nave_enemiga.lista_disparos) > 0):
                        for proyectil_enemigo in nave_enemiga.lista_disparos:
                            proyectil_enemigo.update()
                            proyectil_enemigo.draw(pantalla)

                            if(proyectil_enemigo.rect.top > 720 or colisiono):
                                nave_enemiga.lista_disparos.remove(proyectil_enemigo)
                                colisiono = False

                            #=================Verifico la colision contra el jugador====================================
                            if(proyectil_enemigo.colision_nave(nave)):
                                nave.accion = 1
                                colisiono = True 
                                game_over = True

                for nave_enemiga in oleada_dos:
                    if(len(nave_enemiga.lista_disparos) > 0):
                        for proyectil_enemigo in nave_enemiga.lista_disparos:
                            proyectil_enemigo.update()
                            proyectil_enemigo.draw(pantalla)

                            if(proyectil_enemigo.rect.top > 750 or colisiono):
                                nave_enemiga.lista_disparos.remove(proyectil_enemigo)
                                colisiono = False
                            
                            #=================Verifico la colision contra el jugador====================================
                            if(proyectil_enemigo.colision_nave(nave)):
                                nave.accion = 1
                                colisiono = True 
                                game_over = True
                            
                if(len(oleada_uno) == 0 and len(oleada_dos) == 0):
                    win = True

        #=========================Si se pausó, se detiene el juego hasta que se reanude=================================
        if(pausa):
            pausa_texto = fuente.render("Pausa", True, WHITE)
            rect_pausa = pausa_texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTURA_PANTALLA // 2))
            pantalla.blit(pausa_texto, rect_pausa)
        
        #=======================================Mostrar puntajes========================================================
        if(mostrar_puntajes):

            #============================Leer los puntajes del archivo CSV==============================================
            puntajes = []
            with open('Segundo_Parcial/Puntajes.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    puntajes.append(row)

            #=============================Ordenar los puntajes de mayor a menor=========================================
            puntajes_ordenados = sorted(puntajes, key=lambda x: int(x[1]), reverse=True)

            #==============Mostrar los primeros 5 puntajes más altos en la pantalla del juego===========================
            posy = 180
            for i in range(5):
                if i < len(puntajes_ordenados):
                    nombre = puntajes_ordenados[i][0]
                    puntaje = puntajes_ordenados[i][1]

                    texto = f"{nombre}: {puntaje}"
                    titulo4 = "Puntajes"
                    texto_renderizado = fuente3.render(texto, True, WHITE)
                    titulo_renderizado = fuente3.render(titulo4, True, YELLOW1)

                    pantalla.blit(texto_renderizado, (130, posy))
                    pantalla.blit(titulo_renderizado, (130, 150))
                    posy += 30
                else:
                    break
            
            if(regresar_btn.draw(pantalla) == True):
                mostrar_puntajes = False
                mostrar_titulo = True

        #=========================================Pantalla de victoria==================================================
        if(win):
            mostrar_titulo = False
            mostrar_objetos = False
            win_texto = fuente.render("you win", True, WHITE)
            rect_win = win_texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTURA_PANTALLA // 2))
            pantalla.blit(win_texto, rect_win)
            puntaje = SCORE

            #==============================Guardar puntajes en CSV======================================================
            if(not puntaje_guardado):
                puntajes = []
                puntajes.append([nombre, puntaje])
                puntajes_ordenados = sorted(puntajes, key=lambda x: int(x[1]), reverse=True)

                with open('Segundo_Parcial/Puntajes.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for puntaje in puntajes_ordenados:
                        writer.writerow([str(puntaje[0]).capitalize(), str(puntaje[1])])
                        puntaje_guardado = True
        
        #====================================Pantalla de derrota========================================================
        if(game_over):
            mostrar_titulo = False
            mostrar_objetos = False
            game_over_texto = fuente.render("game over", True, WHITE)
            rect_game_over = game_over_texto.get_rect(center=(ANCHO_PANTALLA // 2, ALTURA_PANTALLA // 2))
            pantalla.blit(game_over_texto, rect_game_over)
            puntaje = SCORE

            #==============================Guardar puntajes en CSV======================================================
            if(not puntaje_guardado):
                puntajes = []
                puntajes.append([nombre, puntaje])
                puntajes_ordenados = sorted(puntajes, key=lambda x: int(x[1]), reverse=True)

                with open('Segundo_Parcial/Puntajes.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for puntaje in puntajes_ordenados:
                        writer.writerow([str(puntaje[0]).capitalize(), str(puntaje[1])])
                        puntaje_guardado = True

        #==================================Mostrar formulario===========================================================
        if(input_active):
            mostrar_titulo = False
            pygame.draw.rect(pantalla, color_cuadro_input, cuadro_input)

            nombre = nombre[:5]

            pantalla.blit(titulo3, (100, 315))
            text_surface = fuente3.render(nombre, True, color_texto)
            pantalla.blit(text_surface, (cuadro_input.x + 5, cuadro_input.y))

            if(regresar_btn.draw(pantalla) == True):
                mostrar_puntajes = False
                mostrar_titulo = True
                input_active = False

        #=============================================Actualizo la pantalla=============================================
        pygame.display.update()
        reloj.tick(fps)

    #===========================================Finalizo las funciones de pygame========================================
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()