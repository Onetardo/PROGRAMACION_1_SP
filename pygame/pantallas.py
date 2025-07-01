import sys

from sonidos import*
from puntaje import*
from tablero import*

# Mostrar pantallas generales.

def mostrar_menu ():
    
    """
    Muestra el menú principal del juego con opciones para seleccionar niveles, jugar, ver puntajes, salir y mutear la música ambiental.
    
    Args:
    None

    Returns:
    None

    """

    # Inicialización
    pygame.init()
    mixer.init()

    # Cargar imágen de fondo y botones
    imagen_fondo = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_nivel_png.png')
    button_nivel = pygame.transform.scale(button_nivel, (200, 70))
    button_nivel_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_nivel_png_presionado.png')
    button_nivel_presionado = pygame.transform.scale(button_nivel_presionado, (200, 70))

    button_jugar = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_jugar_png.png')
    button_jugar = pygame.transform.scale(button_jugar, (200, 70))
    button_jugar_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_jugar_png_presionado.png')
    button_jugar_presionado = pygame.transform.scale(button_jugar_presionado, (200, 70))

    button_ver_puntaje = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_ver_puntajes_png.png')
    button_ver_puntaje = pygame.transform.scale(button_ver_puntaje, (200, 70))
    button_ver_puntaje_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_ver_puntajes_png_presionado.png')
    button_ver_puntaje_presionado = pygame.transform.scale(button_ver_puntaje_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))

    button_musica_on = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_musica_on_png.png')
    button_musica_on = pygame.transform.scale(button_musica_on, (70, 70))
    button_musica_on_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_musica_on_png_presionado.png')
    button_musica_on_presionado = pygame.transform.scale(button_musica_on_presionado, (70, 70))
    
    button_musica_off = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_musica_off_png.png')
    button_musica_off = pygame.transform.scale(button_musica_off, (70, 70))
    button_musica_off_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_musica_off_png_presionado.png')
    button_musica_off_presionado = pygame.transform.scale(button_musica_off_presionado, (70, 70))

    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    FPS = 20
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = button_nivel.get_rect(x=300, y=120)
    rectangulo_vertical_presionado = button_nivel_presionado.get_rect(x=300, y=120)

    rectangulo_vertical2 = button_jugar.get_rect(x=300, y=220)
    rectangulo_vertical2_presionado = button_jugar_presionado.get_rect(x=300, y=220)

    rectangulo_vertical3 = button_ver_puntaje.get_rect(x=300, y=320)
    rectangulo_vertical3_presionado = button_ver_puntaje_presionado.get_rect(x=300, y=320)

    rectangulo_vertical4 = button_salir.get_rect(x=300, y=420)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=300, y=420)

    rectangulo_vertical5 = button_musica_on.get_rect(x=700, y=20)
    rectangulo_vertical5_presionado = button_musica_on_presionado.get_rect(x=700, y=20)

    rectangulo_vertical6 = button_musica_off.get_rect(x=700, y=20)
    rectangulo_vertical6_presionado = button_musica_off_presionado.get_rect(x=700, y=20)

   

    condicion_musica = True
    condicion_efecto = True 
    
    musica_ambiental(condicion_musica)

    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():


            PANTALLA.blit(imagen_fondo, (0, 0))

            
            # Devuelve (x, y)
            pos_mouse = pygame.mouse.get_pos() 
            
            # Verificar colisión con un rectángulo (botón, imagen, etc.)
            #Boton nivel
            if rectangulo_vertical.collidepoint(pos_mouse):
                imagen_agrandada = pygame.transform.scale(button_nivel_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical_presionado.collidepoint(evento.pos):
                        if condicion_efecto:
                            efecto_boton(True)
                        time.sleep(0.5)
                        mostrar_niveles(condicion_efecto)

            else:  
                PANTALLA.blit(button_nivel, rectangulo_vertical)
                    
            #Boton jugar
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_2 = pygame.transform.scale(button_jugar_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        if condicion_efecto:
                            efecto_boton(True)
                        time.sleep(0.5)
                        
                        numero = random.randint(1,3)
                        generar_nivel(int(numero),condicion_musica)
                        
                        
            else:  
                PANTALLA.blit(button_jugar, rectangulo_vertical2)

            #Boton puntaje
            if rectangulo_vertical3.collidepoint(pos_mouse):
                imagen_agrandada_3 = pygame.transform.scale(button_ver_puntaje_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                        if condicion_efecto:
                            efecto_boton(True)
                        time.sleep(0.5)
                        mostrar_puntajes(condicion_efecto)
            else:  
                PANTALLA.blit(button_ver_puntaje, rectangulo_vertical3)
            
            #Boton salir
            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        if condicion_efecto:
                            efecto_boton(True)
                        time.sleep(0.5)
                        pygame.quit()
                        sys.exit()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)
            
            

            #Boton sonido
            if condicion_musica:

                if rectangulo_vertical5.collidepoint(pos_mouse):
                    imagen_agrandada_5 = pygame.transform.scale(button_musica_on_presionado, (90, 90))  # +20px
                    PANTALLA.blit(imagen_agrandada_5, (rectangulo_vertical5_presionado.x - 10, rectangulo_vertical5_presionado.y - 5))  # Ajustar posición
                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
                        
                        if rectangulo_vertical5_presionado.collidepoint(evento.pos) :
                            print ("musica on")
                            condicion_efecto = False 
                            condicion_musica = False
                            efecto_boton(True)
                            musica_ambiental(True)   
                            time.sleep(0.5)  
                else:  
                    
                    PANTALLA.blit(button_musica_off, rectangulo_vertical6) 

            else:

                if rectangulo_vertical6.collidepoint(pos_mouse):
                    imagen_agrandada_6 = pygame.transform.scale(button_musica_off_presionado, (90, 90))  # +20px
                    PANTALLA.blit(imagen_agrandada_6, (rectangulo_vertical6_presionado.x - 10, rectangulo_vertical6_presionado.y - 5))  # Ajustar posición
                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        
                        if rectangulo_vertical6_presionado.collidepoint(evento.pos):
                            print ("musica off")
                            mixer.music.stop()
                            condicion_efecto = False 
                            condicion_musica = False
                            time.sleep(0.5)        
                else:  
                    PANTALLA.blit(button_musica_on, rectangulo_vertical5)



        pygame.display.flip()   


def mostrar_niveles(condicion_musica:bool):
    
    """
    Muestra los niveles disponibles para jugar, permitiendo al usuario seleccionar entre fácil, medio y difícil, o salir al menú principal.
    
    Args:
    condicion_musica: Determina si se reproduce la música ambiental o no. Si es True, se reproduce la música ambiental, si es False no se reproduce.

    Returns:
    None

    """
    
    # Inicialización
    pygame.init()
    mixer.init()


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    button_nivel_facil = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_facil_png.png')
    button_nivel_facil = pygame.transform.scale(button_nivel_facil, (200, 70))
    button_nivel_facil_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_facil_png_presionado.png')
    button_nivel_facil_presionado = pygame.transform.scale(button_nivel_facil_presionado, (200, 70))

    button_nivel_medio = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_medio_png.png')
    button_nivel_medio = pygame.transform.scale(button_nivel_medio, (200, 70))
    button_nivel_medio_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_medio_png_presionado.png')
    button_nivel_medio_presionado = pygame.transform.scale(button_nivel_medio_presionado, (200, 70))

    button_nivel_dificil = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_dificil_png.png')
    button_nivel_dificil = pygame.transform.scale(button_nivel_dificil, (200, 70))
    button_nivel_dificil_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_dificil_png_presionado.png')
    button_nivel_dificil_presionado = pygame.transform.scale(button_nivel_dificil_presionado, (200, 70))

    button_salir = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    FPS = 25
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = button_nivel_facil.get_rect(x=80, y=220)
    rectangulo_vertical_presionado = button_nivel_facil_presionado.get_rect(x=80, y=220)

    rectangulo_vertical2 = button_nivel_medio.get_rect(x=300, y=220)
    rectangulo_vertical2_presionado = button_nivel_medio_presionado.get_rect(x=300, y=220)

    rectangulo_vertical3 = button_nivel_dificil.get_rect(x=520, y=220)
    rectangulo_vertical3_presionado = button_nivel_dificil_presionado.get_rect(x=520, y=220)

    rectangulo_vertical4 = button_salir.get_rect(x=300, y=400)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=300, y=400)



    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():

            PANTALLA.blit(imagen_fondo, (0, 0))
        
            # Devuelve (x, y)
            pos_mouse = pygame.mouse.get_pos()  
            
            # Verificar colisión con un rectángulo (botón, imagen, etc.)
            # Boton nivel facil
            if rectangulo_vertical.collidepoint(pos_mouse):
                imagen_agrandada = pygame.transform.scale(button_nivel_facil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(1, condicion_musica)
            else:  
                PANTALLA.blit(button_nivel_facil, rectangulo_vertical)

            # Boton nivel medio        
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_2 = pygame.transform.scale(button_nivel_medio_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_2, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(2, condicion_musica)              
            else:  
                PANTALLA.blit(button_nivel_medio, rectangulo_vertical2)

            # Boton nivel dificil
            if rectangulo_vertical3.collidepoint(pos_mouse):
                imagen_agrandada_3 = pygame.transform.scale(button_nivel_dificil_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_3, (rectangulo_vertical3_presionado.x - 10, rectangulo_vertical3_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical3_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        generar_nivel(3, condicion_musica)                
            else:  
                PANTALLA.blit(button_nivel_dificil, rectangulo_vertical3)
            
            # Boton salir
            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        mostrar_menu()             
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)



            pygame.display.flip()   


def mostrar_puntajes (condicion_musica:bool):
    
    """
    Muestra los puntajes de los jugadores en el juego, permitiendo ver los tres mejores puntajes y salir al menú principal.
    
    Args:
    condicion_musica: Determina si se reproduce la música ambiental o no. Si es True, se reproduce la música ambiental, si es False no se reproduce.

    Returns:
    None

    """
    
    # Inicialización
    pygame.init()
    mixer.init()


    # Cargar imágenes
    imagen_fondo = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    lista_puntaje = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/lista_ver_puntaje_png.png')
    lista_puntaje = pygame.transform.scale(lista_puntaje, (500, 400))
 

    button_salir = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 600
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    FPS = 25
    clock = pygame.time.Clock()

    # Rectángulos para los botones
    rectangulo_vertical = lista_puntaje.get_rect(x=150, y=50)
    
    rectangulo_vertical2 = button_salir.get_rect(x=300, y=460)
    rectangulo_vertical2_presionado = button_salir_presionado.get_rect(x=300, y=460)

 

    # Bucle principal
    while True:
        clock.tick(FPS)
        
        for evento in pygame.event.get():
            
            
            PANTALLA.blit(imagen_fondo, (0, 0))
            PANTALLA.blit(lista_puntaje, rectangulo_vertical)

            # Devuelve (x, y)
            pos_mouse = pygame.mouse.get_pos()  

            # Verificar colisión con un rectángulo (botón, imagen, etc.)
            # Boton salir
            if rectangulo_vertical2.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical2_presionado.x - 10, rectangulo_vertical2_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical2_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical2)

            # Cargar los datos del archivo JSON
            with open('C:/Users/Matias/Desktop/segundo_parcial/pygame/archivos_json/puntajes.json', 'r') as archivo_json:
                datos = json.load(archivo_json)

            # Mostrar el título de la lista de puntajes
            jugador_1 = str(datos.get('nombre_1')) + " " + str(datos.get('puntaje_1'))
            jugador_2 = str(datos.get('nombre_2')) + " " + str(datos.get('puntaje_2'))
            jugador_3 = str(datos.get('nombre_3')) + " " + str(datos.get('puntaje_3'))

            # Mostrar los puntajes de los jugadores
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_1, 1)
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_2, 2)
            mostrar_puntaje_jugadores_top_3(PANTALLA, jugador_3, 3)


            pygame.display.flip()  


def ingresar_nombre_jugador(PANTALLA:pygame.Surface, condicion_efecto:bool, puntaje_jugador:str, tipo_nivel:int):
    
    """
    Muestra una pantalla para que el jugador ingrese su nombre y registre su puntaje, permitiendo al jugador guardar su puntaje después de completar un nivel.
    
    Args:
    PANTALLA: Superficie de Pygame donde se dibujará la pantalla de ingreso de nombre.
    condicion_efecto: Determina si se reproduce el efecto de sonido al presionar el botón de ingreso de nombre. Si es True, se reproduce el efecto de sonido, si es False no se reproduce.
    puntaje_jugador: Puntaje del jugador que se registrará.
    tipo_nivel: Entero que indica el nivel de dificultad del juego (1 para fácil, 2 para medio, 3 para difícil).

    Returns:
    None

    """

    # Configuración de pantalla
    ANCHO, ALTO = 800, 400
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    FPS = 20
    clock = pygame.time.Clock()
    
    # Cargar imágenes
    boton_enter = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/boton_enter_png.png')
    boton_enter = pygame.transform.scale(boton_enter, (200, 70))

    boton_enter_presionando = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/boton_enter_presionado_png.png')
    boton_enter_presionando = pygame.transform.scale(boton_enter_presionando, (200, 70))
    
    tabla_texto = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/cuadro_texto_png.png')
    tabla_texto = pygame.transform.scale(tabla_texto, (450, 100))

    imagen_fondo = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 600))

    # Rectángulos para los botones
    rectangulo_vertical = boton_enter.get_rect(x=300, y=270)
    rectangulo_vertical_presionado = boton_enter_presionando.get_rect(x=300, y=270)

    nombre_jugador = ""
    
    while True:
        clock.tick(FPS)
        for evento in pygame.event.get():
            
            if evento.type == pygame.KEYDOWN:
                # Limitar a 4 caracteres
                if len(nombre_jugador) <= 3:  
                    if evento.unicode.isalpha():
                        print(f"Letra presionada: {evento.unicode}")
                        # Convertir a mayúscula
                        nombre_jugador += evento.unicode.upper()  
                    
                if evento.key == pygame.K_BACKSPACE:
                    # Borrar último carácter
                    nombre_jugador = nombre_jugador[:-1]   
        
        # Devuelve (x, y)
        pos_mouse = pygame.mouse.get_pos()  
            

        PANTALLA.blit(imagen_fondo, (0, 0))

        PANTALLA.blit(tabla_texto, (170, 150))

        
        # Verificar colisión con un rectángulo (botón, imagen, etc.)
        #Boton nivel
        if rectangulo_vertical.collidepoint(pos_mouse):
            imagen_agrandada = pygame.transform.scale(boton_enter_presionando, (220, 80))  # +20px
            PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if rectangulo_vertical_presionado.collidepoint(evento.pos):
                    if condicion_efecto:
                        efecto_boton(True)
                    time.sleep(0.5)
                    registrar_puntaje(puntaje_jugador, nombre_jugador, tipo_nivel)
                    mostrar_menu()

        else:  
            PANTALLA.blit(boton_enter, rectangulo_vertical)
                

        mostrar_puntaje_pantalla(puntaje_jugador, PANTALLA )
        
        mostrar_texto_pantalla(nombre_jugador, PANTALLA)
        pygame.display.flip()

        pygame.display.flip()


def generar_nivel(tipo_nivel: int, condicion_musica:bool):
    """
    Muestra el nivel seleccionado por el usuario y comienza el juego, permitiendo al jugador jugar en diferentes niveles de dificultad (fácil, medio o difícil).
    
    Args:
    tipo_nivel: Entero que indica el nivel de dificultad seleccionado por el usuario (1 para fácil, 2 para medio, 3 para difícil).
    condicion_musica: Determina si se reproduce la música ambiental o no. Si es True, se reproduce la música ambiental, si es False no se reproduce.

    Returns:
    None

    """
    
    # Inicialización
    pygame.init()
    mixer.init()

    # Reproducir música ambiental si la condición es True
    musica_jugando(condicion_musica)
    
    # Cargar efectos de sonido
    efecto_ganaste = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_de_ganaste.mp3')
    efecto_ganaste.set_volume(0.4)
    
    efecto_agua_fallo = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_agua_fallo.mp3')
    efecto_agua_fallo.set_volume(0.4)

    efecto_golpe_barco = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_golpe_barco.mp3')
    efecto_golpe_barco.set_volume(0.4)

    efecto_golpe_hundido = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_barco_hundido.mp3')
    efecto_golpe_hundido.set_volume(5.0)

    efecto_golpe_hundido_2 = mixer.Sound('C:/Users/Matias/Desktop/segundo_parcial/pygame/recursos_musica/ruido_señal.mp3')
    efecto_golpe_hundido_2.set_volume(5.0)

    # Cargar imágenes
    button_salir = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png.png')
    button_salir = pygame.transform.scale(button_salir, (200, 70))
    button_salir_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_salir_png_presionado.png')
    button_salir_presionado = pygame.transform.scale(button_salir_presionado, (200, 70))

    button_reiniciar = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_reiniciar_png.png')
    button_reiniciar = pygame.transform.scale(button_reiniciar, (200, 70))
    button_reiniciar_presionado = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/button_reiniciar_png_presionado.png')
    button_reiniciar_presionado = pygame.transform.scale(button_reiniciar_presionado, (200, 70))

    rectangulo_vertical4 = button_salir.get_rect(x=430, y=680)
    rectangulo_vertical4_presionado = button_salir_presionado.get_rect(x=430, y=680)

    rectangulo_vertical = button_reiniciar.get_rect(x=170, y=680)
    rectangulo_vertical_presionado = button_reiniciar_presionado.get_rect(x=170, y=680)

    imagen_fondo = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/fondo_menu_png.png')
    imagen_fondo = pygame.transform.scale(imagen_fondo, (800, 800))


    # Configuración de pantalla
    ANCHO, ALTO = 800, 800
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO),pygame.NOFRAME)
    pygame.display.set_caption(f"Batalla Naval - Nivel {tipo_nivel}")
    FPS = 25
    clock = pygame.time.Clock()

    # Determinar tamaño del tablero según nivel
    if tipo_nivel == 1:
        filas, columnas = 10, 10
    elif tipo_nivel == 2:
        filas, columnas = 20, 20
    else:  # tipo_nivel == 3
        filas, columnas = 40, 40  # Reducido de 40x40 para mejor visualización

    # Crear y poblar con barcos la matriz
    matriz = iniciar_matriz(filas, columnas, 0)
    matriz, posiciones_barcos = colocar_barcos(matriz, tipo_nivel)

    for fila in matriz:
        print(fila)

    # Inicializar la matriz del jugador
    # Esta matriz se usará para marcar los disparos del jugador
    matriz_jugador = iniciar_matriz(filas, columnas, 0)


    
    coordenadas_y_recoridas = []

    # Obtener las coordenadas de los barcos
    coordenadas_barcos = []

    for i in range(filas):
        for x in range(columnas):
            if matriz[i][x] == 1:
                coordenadas_barcos.append((i,x))
                
                
    # Calcular el tamaño de las casillas del tablero
    margen = 2
    ancho_casilla = min(
        (500 - (columnas + 1) * margen) // columnas,
        (500 - (filas + 1) * margen) // filas
    )
    
    # Calcular offsets para centrado
    tablero_ancho = columnas * (ancho_casilla + margen) + margen
    tablero_alto = filas * (ancho_casilla + margen) + margen
    offset_x = (800 - tablero_ancho) // 2  # 800 es ANCHO de tu pantalla
    offset_y = (800 - tablero_alto) // 2   # 800 es ALTO de tu pantalla

    condicion_hundimiento = False
    condicion = True

    puntaje_jugador = 0

    # Bucle principal del juego
    running = True
    while running:
        clock.tick(FPS)
        
        
        for evento in pygame.event.get():
            
           

            
            # Devuelve (x, y)
            pos_mouse = pygame.mouse.get_pos()
                    
            # Obtener la celda en la que se hizo clic
            celda = obtener_celda_click(
                pos_mouse[0], 
                pos_mouse[1],
                filas=filas,
                columnas=columnas,
                ancho_casilla=ancho_casilla,
                margen=margen,
                offset_x=offset_x,
                offset_y=offset_y
            )

            


            # Verificar si se hizo clic en una celda válida
            if celda:
                
                fila, columna = celda

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    print("presiona")

                    # Verificar si la celda ya fue recorrida
                    if (fila, columna) in coordenadas_y_recoridas:
                        condicion = False
                    else:
                        condicion = True

                    
                    if condicion:
                        # Verificar si la celda contiene algun barco en esa coordenada
                        if (fila, columna) in coordenadas_barcos:
                            matriz_jugador[fila][columna] += 1
                            puntaje_jugador += 5
                            # Verificar si se hundió un barco
                            condicion_hundimiento, tamaño_hundido = verificar_hundidos(matriz_jugador, posiciones_barcos)
                            # Se agrega la coordenada a las ya recorridas
                            coordenadas_y_recoridas.append((fila, columna))
                            condicion_efecto = True
                        else:
                            condicion_efecto = False

                        if condicion_hundimiento:
                            if condicion_musica:
                                efecto_golpe_hundido_2.play()
                                efecto_golpe_hundido.play()
                            condicion_hundimiento = False
                            puntaje_jugador += (tamaño_hundido * 10)

                            # Verificar si todos los barcos han sido hundidos
                            if todos_barcos_hundidos(coordenadas_barcos, matriz_jugador):
                                if condicion_musica:
                                    efecto_ganaste.play()
                                time.sleep(2.0)
                                # Mostrar pantalla de ingreso de nombre del jugador
                                ingresar_nombre_jugador(PANTALLA, condicion_musica, puntaje_jugador, tipo_nivel)

                        elif condicion_efecto:
                            if condicion_musica:
                                efecto_golpe_barco.play()
                        else:
                            if matriz_jugador[fila][columna] != 2:
                                matriz_jugador[fila][columna] = 2
                                if condicion_musica:
                                    efecto_agua_fallo.play()
                                puntaje_jugador -= 1

                    print("puntaje jugador:", puntaje_jugador)


            
            PANTALLA.blit(imagen_fondo, (0, 0))

            # Dibujar el tablero del jugador
            dibujar_tablero(matriz_jugador, filas, columnas, 500, 500, PANTALLA)

            # Verificar colisión con un rectángulo (botón, imagen, etc.)
            # Boton salir
            if rectangulo_vertical4.collidepoint(pos_mouse):
                imagen_agrandada_4 = pygame.transform.scale(button_salir_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada_4, (rectangulo_vertical4_presionado.x - 10, rectangulo_vertical4_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical4_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        
                        mostrar_menu()
            else:  
                PANTALLA.blit(button_salir, rectangulo_vertical4)

            # Boton reiniciar
            if rectangulo_vertical.collidepoint(pos_mouse):
                imagen_agrandada = pygame.transform.scale(button_reiniciar_presionado, (220, 80))  # +20px
                PANTALLA.blit(imagen_agrandada, (rectangulo_vertical_presionado.x - 10, rectangulo_vertical_presionado.y - 5))  # Ajustar posición
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    
                    if rectangulo_vertical_presionado.collidepoint(evento.pos):
                        
                        efecto_boton(condicion_musica)
                        time.sleep(0.5)
                        
                        generar_nivel(tipo_nivel, condicion_musica)
            else:  
                PANTALLA.blit(button_reiniciar, rectangulo_vertical)


            mostrar_puntaje_pantalla(puntaje_jugador, PANTALLA)

            pygame.display.flip()
