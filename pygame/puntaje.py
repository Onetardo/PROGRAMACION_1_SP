import pygame
import json

def mostrar_puntaje_jugadores_top_3(PANTALLA:pygame.Surface, texto: str, top: int):
    
    """
    Muestra el puntaje de los jugadores en la pantalla mediente imagenes, permitiendo ver los tres mejores puntajes.
    
    Args:
    PANTALLA: Superficie de Pygame donde se dibujarán los puntajes.
    texto: Texto que representa el puntaje del jugador.
    top: Indica la posición en pantalla del jugador en el ranking (1, 2 o 3).

    Returns:
    None

    """

    # Carga de imágenes 
    texto_A = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_A_png.png')
    texto_A = pygame.transform.scale(texto_A, (30, 40))
    texto_B = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_B_png.png')
    texto_B = pygame.transform.scale(texto_B, (30, 40))
    texto_C = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_C_png.png')
    texto_C = pygame.transform.scale(texto_C, (30, 40))
    texto_D = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_D_png.png')
    texto_D = pygame.transform.scale(texto_D, (30, 40))
    texto_E = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_E_png.png')
    texto_E = pygame.transform.scale(texto_E, (30, 40))
    texto_F = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_F_png.png')
    texto_F = pygame.transform.scale(texto_F, (30, 40))
    texto_G = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_G_png.png')
    texto_G = pygame.transform.scale(texto_G, (30, 40))
    texto_H = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_H_png.png')
    texto_H = pygame.transform.scale(texto_H, (30, 40))
    texto_I = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_I_png.png')
    texto_I = pygame.transform.scale(texto_I, (30, 40))
    texto_J = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_J_png.png')
    texto_J = pygame.transform.scale(texto_J, (30, 40))
    texto_K = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_K_png.png')
    texto_K = pygame.transform.scale(texto_K, (30, 40))
    texto_L = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_L_png.png')
    texto_L = pygame.transform.scale(texto_L, (30, 40))
    texto_M = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_M_png.png')
    texto_M = pygame.transform.scale(texto_M, (30, 40))
    texto_N = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_N_png.png')
    texto_N = pygame.transform.scale(texto_N, (30, 40))
    texto_O = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_O_png.png')
    texto_O = pygame.transform.scale(texto_O, (30, 40))
    texto_P = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_P_png.png')
    texto_P = pygame.transform.scale(texto_P, (30, 40))
    texto_Q = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Q_png.png')
    texto_Q = pygame.transform.scale(texto_Q, (30, 40))
    texto_R = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_R_png.png')
    texto_R = pygame.transform.scale(texto_R, (30, 40))
    texto_S = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_S_png.png')
    texto_S = pygame.transform.scale(texto_S, (30, 40))
    texto_T = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_T_png.png')
    texto_T = pygame.transform.scale(texto_T, (30, 40))
    texto_U = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_U_png.png')
    texto_U = pygame.transform.scale(texto_U, (30, 40))
    texto_V = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_V_png.png')
    texto_V = pygame.transform.scale(texto_V, (30, 40))
    texto_W = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_W_png.png')
    texto_W = pygame.transform.scale(texto_W, (30, 40))
    texto_X = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_X_png.png')
    texto_X = pygame.transform.scale(texto_X, (30, 40))
    texto_Y = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Y_png.png')
    texto_Y = pygame.transform.scale(texto_Y, (30, 40))
    texto_Z = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Z_png.png')
    texto_Z = pygame.transform.scale(texto_Z, (30, 40))
    texto_simobolo_menos = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/simbolo_menos_png.png')
    texto_simobolo_menos = pygame.transform.scale(texto_simobolo_menos, (30, 40))
    texto_cero = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_0_png.png')
    texto_cero = pygame.transform.scale(texto_cero, (30, 30))
    texto_uno = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_1_png.png')
    texto_uno = pygame.transform.scale(texto_uno, (30, 30))
    texto_dos = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_2_png.png')
    texto_dos = pygame.transform.scale(texto_dos, (30, 30))
    texto_tres = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_3_png.png')
    texto_tres = pygame.transform.scale(texto_tres, (30, 30))
    texto_cuatro = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_4_png.png')
    texto_cuatro = pygame.transform.scale(texto_cuatro, (30, 30))
    texto_cinco = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_5_png.png')
    texto_cinco = pygame.transform.scale(texto_cinco, (30, 30))
    texto_seis = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_6_png.png')
    texto_seis = pygame.transform.scale(texto_seis, (30, 30))
    texto_siete = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_7_png.png')
    texto_siete = pygame.transform.scale(texto_siete, (30, 30))
    texto_ocho = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_8_png.png')
    texto_ocho = pygame.transform.scale(texto_ocho, (30, 30))
    texto_nueve = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_9_png.png')
    texto_nueve = pygame.transform.scale(texto_nueve, (30, 30))

    # Diccionario para acceso rápido
    letras = {
        'A': texto_A, 'B': texto_B, 'C': texto_C, 'D': texto_D, 'E': texto_E, 'F': texto_F,
        'G': texto_G, 'H': texto_H, 'I': texto_I, 'J': texto_J, 'K': texto_K, 'L': texto_L,
        'M': texto_M, 'N': texto_N, 'O': texto_O, 'P': texto_P, 'Q': texto_Q, 'R': texto_R,
        'S': texto_S, 'T': texto_T, 'U': texto_U, 'V': texto_V, 'W': texto_W, 'X': texto_X,
        'Y': texto_Y, 'Z': texto_Z, '-': texto_simobolo_menos, '0': texto_cero, '1': texto_uno,
        '2': texto_dos, '3': texto_tres, '4': texto_cuatro, '5': texto_cinco, '6': texto_seis,
        '7': texto_siete, '8': texto_ocho, '9': texto_nueve
    }

    # Posición base (centrado horizontal)
    if top == 1:
        pos_x = 400
        pos_y = 120
    elif top == 2:
        pos_x = 400
        pos_y = 220
    elif top == 3:
        pos_x = 400
        pos_y = 320

    # Asegura mayúsculas
    str_puntaje = str(texto).upper()  
    ancho_letra = 20
    # Espacio entre caracteres
    espacio = 5  

    ancho_total = len(str_puntaje) * (ancho_letra + espacio)
    pos_x_inicial = pos_x - ancho_total // 2

    for i, digito in enumerate(str_puntaje):
        x = pos_x_inicial + i * (ancho_letra + espacio)
        if digito == ' ':
            # Deja espacio vacío
            continue  
        imagen = letras.get(digito)
        if imagen:
            # Ajusta la altura para números (más chicos)
            if digito.isdigit():
                PANTALLA.blit(imagen, (x, pos_y + 10))
            else:
                PANTALLA.blit(imagen, (x, pos_y))
        

def registrar_puntaje(puntaje_jugador:str, nombre_jugador:str, nivel:int):

    """
    Registra el puntaje del jugador en un archivo JSON, permitiendo que los jugadores guarden sus puntajes después de completar un nivel.
    
    Args:
    puntaje_jugador: Puntaje del jugador que se registrará.
    nombre_jugador: Nombre del jugador que se registrará.
    nivel: Entero que indica el nivel de dificultad del juego (1 para fácil, 2 para medio, 3 para difícil).

    Returns:
    None

    """

    # Cargar los datos del archivo JSON
    with open('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/archivos_json/puntajes.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
    
    # Verificar si el puntaje del jugador es mayor que los puntajes actuales
    if puntaje_jugador >= int(datos["puntaje_1"]):
        # Desplazar todos hacia abajo
        datos["puntaje_3"] = datos["puntaje_2"]
        datos["nombre_3"] = datos["nombre_2"]
        datos["nivel_3"] = datos["nivel_2"]
        
        datos["puntaje_2"] = datos["puntaje_1"]
        datos["nombre_2"] = datos["nombre_1"]
        datos["nivel_2"] = datos["nivel_1"]
        
        # Insertar nuevo 1er lugar
        datos["puntaje_1"] = puntaje_jugador
        datos["nombre_1"] = nombre_jugador
        datos["nivel_1"] = nivel

    elif puntaje_jugador >= int(datos["puntaje_2"]):
        # Desplazar 2do a 3ro
        datos["puntaje_3"] = datos["puntaje_2"]
        datos["nombre_3"] = datos["nombre_2"]
        datos["nivel_3"] = datos["nivel_2"]
        
        # Insertar nuevo 2do lugar
        datos["puntaje_2"] = puntaje_jugador
        datos["nombre_2"] = nombre_jugador
        datos["nivel_2"] = nivel

    elif puntaje_jugador >= int(datos["puntaje_3"]):
        # Insertar nuevo 3er lugar
        datos["puntaje_3"] = puntaje_jugador
        datos["nombre_3"] = nombre_jugador
        datos["nivel_3"] = nivel
        

# Guardar en archivo
    with open('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/archivos_json/puntajes.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)  # indent=4 para formato legible


def mostrar_texto_pantalla(texto:str, PANTALLA:pygame.Surface):

    """
    Genera y muestra el texto en pantalla utilizando imágenes de letras, permitiendo que el jugador vea su nombre ingresado en la pantalla de registro de puntajes.
    
    Args:
    texto: Texto que se mostrará en pantalla.
    PANTALLA: Superficie de Pygame donde se dibujará el texto

    Returns:
    None

    """
    # Cargar imágenes de letras
    texto_A = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_A_png.png')
    texto_A = pygame.transform.scale(texto_A, (50, 60))
    texto_B = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_B_png.png')
    texto_B = pygame.transform.scale(texto_B, (50, 60))
    texto_C = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_C_png.png')
    texto_C = pygame.transform.scale(texto_C, (50, 60))
    texto_D = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_D_png.png')
    texto_D = pygame.transform.scale(texto_D, (50, 60))
    texto_E = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_E_png.png')
    texto_E = pygame.transform.scale(texto_E, (50, 60))
    texto_F = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_F_png.png')
    texto_F = pygame.transform.scale(texto_F, (50, 60))
    texto_G = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_G_png.png')
    texto_G = pygame.transform.scale(texto_G, (50, 60))
    texto_H = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_H_png.png')
    texto_H = pygame.transform.scale(texto_H, (50, 60))
    texto_I = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_I_png.png')
    texto_I = pygame.transform.scale(texto_I, (50, 60))
    texto_J = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_J_png.png')
    texto_J = pygame.transform.scale(texto_J, (50, 60))
    texto_K = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_K_png.png')
    texto_K = pygame.transform.scale(texto_K, (50, 60))
    texto_L = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_L_png.png')
    texto_L = pygame.transform.scale(texto_L, (50, 60))
    texto_M = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_M_png.png')
    texto_M = pygame.transform.scale(texto_M, (50, 60))
    texto_N = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_N_png.png')
    texto_N = pygame.transform.scale(texto_N, (50, 60))
    texto_O = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_O_png.png')
    texto_O = pygame.transform.scale(texto_O, (50, 60))
    texto_P = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_P_png.png')
    texto_P = pygame.transform.scale(texto_P, (50, 60))
    texto_Q = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Q_png.png')
    texto_Q = pygame.transform.scale(texto_Q, (50, 60))
    texto_R = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_R_png.png')
    texto_R = pygame.transform.scale(texto_R, (50, 60))
    texto_S = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_S_png.png')
    texto_S = pygame.transform.scale(texto_S, (50, 60))
    texto_T = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_T_png.png')
    texto_T = pygame.transform.scale(texto_T, (50, 60))
    texto_U = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_U_png.png')
    texto_U = pygame.transform.scale(texto_U, (50, 60))
    texto_V = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_V_png.png')
    texto_V = pygame.transform.scale(texto_V, (50, 60))
    texto_W = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_W_png.png')
    texto_W = pygame.transform.scale(texto_W, (50, 60))
    texto_X = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_X_png.png')
    texto_X = pygame.transform.scale(texto_X, (50, 60))
    texto_Y = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Y_png.png')
    texto_Y = pygame.transform.scale(texto_Y, (50, 60))
    texto_Z = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/caracter_Z_png.png')
    texto_Z = pygame.transform.scale(texto_Z, (50, 60))


    # Posición base 
    pos_x = 810
    pos_y = 170
    
    # Convertir el puntaje a string
    str_puntaje = str(texto)
    
    # Calcular el ancho total del puntaje
    ancho_total = len(str_puntaje) * 55  # 75px por dígito (ajusta si es diferente)
    
    
    # Calcular posición X inicial para centrar
    pos_x_inicial = (pos_x - ancho_total) // 2
    
    # Mostrar cada dígito
    for i, digito in enumerate(str_puntaje):
        if digito == 'A':
            PANTALLA.blit(texto_A, (pos_x_inicial + i*50, pos_y))
        elif digito == 'B':
            PANTALLA.blit(texto_B, (pos_x_inicial + i*50, pos_y))
        elif digito == 'C':
            PANTALLA.blit(texto_C, (pos_x_inicial + i*50, pos_y))
        elif digito == 'D':
            PANTALLA.blit(texto_D, (pos_x_inicial + i*50, pos_y))
        elif digito == 'E':
            PANTALLA.blit(texto_E, (pos_x_inicial + i*50, pos_y))
        elif digito == 'F':
            PANTALLA.blit(texto_F, (pos_x_inicial + i*50, pos_y))
        elif digito == 'G':
            PANTALLA.blit(texto_G, (pos_x_inicial + i*50, pos_y))
        elif digito == 'H':
            PANTALLA.blit(texto_H, (pos_x_inicial + i*50, pos_y))
        elif digito == 'I':
            PANTALLA.blit(texto_I, (pos_x_inicial + i*50, pos_y))
        elif digito == 'J':
            PANTALLA.blit(texto_J, (pos_x_inicial + i*50, pos_y))
        elif digito == 'K':
            PANTALLA.blit(texto_K, (pos_x_inicial + i*50, pos_y))
        elif digito == 'L':
            PANTALLA.blit(texto_L, (pos_x_inicial + i*50, pos_y))
        elif digito == 'M':
            PANTALLA.blit(texto_M, (pos_x_inicial + i*50, pos_y))
        elif digito == 'N':
            PANTALLA.blit(texto_N, (pos_x_inicial + i*50, pos_y))
        elif digito == 'O':
            PANTALLA.blit(texto_O, (pos_x_inicial + i*50, pos_y))
        elif digito == 'P':
            PANTALLA.blit(texto_P, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Q':
            PANTALLA.blit(texto_Q, (pos_x_inicial + i*50, pos_y))
        elif digito == 'R':
            PANTALLA.blit(texto_R, (pos_x_inicial + i*50, pos_y))
        elif digito == 'S':
            PANTALLA.blit(texto_S, (pos_x_inicial + i*50, pos_y))
        elif digito == 'T':
            PANTALLA.blit(texto_T, (pos_x_inicial + i*50, pos_y))
        elif digito == 'U':
            PANTALLA.blit(texto_U, (pos_x_inicial + i*50, pos_y))
        elif digito == 'V':
            PANTALLA.blit(texto_V, (pos_x_inicial + i*50, pos_y))
        elif digito == 'W':
            PANTALLA.blit(texto_W, (pos_x_inicial + i*50, pos_y))
        elif digito == 'X':
            PANTALLA.blit(texto_X, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Y':
            PANTALLA.blit(texto_Y, (pos_x_inicial + i*50, pos_y))
        elif digito == 'Z':
            PANTALLA.blit(texto_Z, (pos_x_inicial + i*50, pos_y))
    
    
