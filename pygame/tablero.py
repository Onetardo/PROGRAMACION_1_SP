import pygame
import pygame.mixer as mixer 
import random
import time

from sonidos import*


    
def iniciar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    
    """
    Inicializa una matriz de tamaño `cant_filas` x `cant_columnas` con un valor inicial.
    
    Args:
    cant_filas: Número de filas de la matriz.
    cant_columnas: Número de columnas de la matriz.
    valor_inicial: Valor con el que se inicializarán todas las celdas de la matriz.

    Returns:
    None
    Esta función no retorna ningún valor, pero dibuja el tablero en la pantalla proporcionada.

    """

    matriz= []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz


def colocar_barcos(matriz:list, dificultad:int) -> tuple:
    
    """
    Coloca barcos en la matriz de juego según la dificultad seleccionada.
    
    Args:
    matriz: Matriz que representa el tablero de juego, donde se colocarán los barcos.
    dificultad: Entero que indica el nivel de dificultad del juego (1 para fácil, 2 para medio, 3 para difícil).

    Returns:
    
    - matriz_modificada: Matriz con los barcos colocados.
    - posiciones_barcos: Diccionario con las posiciones de los barcos colocados.

    """
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Definición de barcos
    barcos_base = [
        {'nombre': 'submarino', 'tamaño': 1, 'cantidad': 4},
        {'nombre': 'destructor', 'tamaño': 2, 'cantidad': 3},
        {'nombre': 'crucero', 'tamaño': 3, 'cantidad': 2},
        {'nombre': 'acorazado', 'tamaño': 4, 'cantidad': 1}
    ]
    
    # Ajustar cantidad según dificultad
    multiplicador = 1
    if dificultad == 2:
        multiplicador = 2
    elif dificultad == 3:
        multiplicador = 3
    
    # Diccionario para guardar posiciones
    posiciones_barcos = {barco['nombre']: [] for barco in barcos_base}
    
    # Lista de tamaños de barcos a colocar
    barcos_a_colocar = []
    for barco in barcos_base:
        barcos_a_colocar.extend([(barco['nombre'], barco['tamaño'])] * (barco['cantidad'] * multiplicador))
    
    # Ordenar de mayor a menor para mejor colocación
    barcos_a_colocar.sort(key=lambda x: x[1], reverse=True)
    
    for nombre, tamaño in barcos_a_colocar:
        colocado = False
        intentos = 0
        posiciones_barco_actual = []
        
        while not colocado and intentos < 100:
            intentos += 1
            horizontal = random.choice([True, False])
            posiciones_barco_actual = []
            
            if horizontal:
                fila = random.randint(0, filas - 1)
                col_inicio = random.randint(0, columnas - tamaño)
                col_fin = col_inicio + tamaño
                
                # Verificar área alrededor del barco
                espacio_libre = True
                for col in range(max(0, col_inicio-1), min(columnas, col_fin+1)):
                    for f in range(max(0, fila-1), min(filas, fila+2)):
                        if matriz[f][col] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Guardar posiciones y colocar barco
                    for col in range(col_inicio, col_fin):
                        matriz[fila][col] = 1
                        posiciones_barco_actual.append((fila, col))
                    colocado = True
            else:
                col = random.randint(0, columnas - 1)
                fila_inicio = random.randint(0, filas - tamaño)
                fila_fin = fila_inicio + tamaño
                
                # Verificar área alrededor del barco
                espacio_libre = True
                for fila in range(max(0, fila_inicio-1), min(filas, fila_fin+1)):
                    for c in range(max(0, col-1), min(columnas, col+2)):
                        if matriz[fila][c] != 0:
                            espacio_libre = False
                            break
                    if not espacio_libre:
                        break
                
                if espacio_libre:
                    # Guardar posiciones y colocar barco
                    for fila in range(fila_inicio, fila_fin):
                        matriz[fila][col] = 1
                        posiciones_barco_actual.append((fila, col))
                    colocado = True
        
            if colocado:
                posiciones_barcos[nombre].append(posiciones_barco_actual)
    
    return matriz, posiciones_barcos


def dibujar_tablero(matriz:list, filas:int, columnas:int, area_ancho:int, area_alto:int, pantalla:pygame.Surface):
    
    """
    Dibuja el tablero de juego en la pantalla, mostrando los barcos, fallos y agua según la matriz proporcionada.
    
    Args:
    matriz: Matriz que representa el estado del tablero, donde:
        - 0 indica agua,
        - 1 indica un barco golpeado,
        - 2 indica un fallo.
    filas: Número de filas del tablero.
    columnas: Número de columnas del tablero.
    area_ancho: Ancho del área del tablero en píxeles.
    area_alto: Alto del área del tablero en píxeles.
    pantalla: Superficie de Pygame donde se dibujará el tablero.

    Returns:
    None
    Esta función no retorna ningún valor, pero dibuja el tablero en la pantalla proporcionada.

    """

    # Cargar las imágenes (hazlo una vez al inicio del juego)
    agua_img = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/agua_nivel_png.png')
    barco_img = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/barco_golpeado_png.png')
    fallo_img = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/agua_nivel_fallo_png.png')
    
    # Escalar las imágenes al tamaño de las celdas
    margen = 2
    ancho_casilla = min(
        (area_ancho - (columnas + 1) * margen) // columnas,
        (area_alto - (filas + 1) * margen) // filas
    )
    
    # Escalar imágenes al tamaño de la celda
    agua_img = pygame.transform.scale(agua_img, (ancho_casilla, ancho_casilla))
    barco_img = pygame.transform.scale(barco_img, (ancho_casilla, ancho_casilla))
    fallo_img = pygame.transform.scale(fallo_img, (ancho_casilla, ancho_casilla))

    # Calcular posición del tablero
    tablero_ancho = columnas * (ancho_casilla + margen) + margen
    tablero_alto = filas * (ancho_casilla + margen) + margen
    offset_x = (pantalla.get_width() - tablero_ancho) // 2
    offset_y = (pantalla.get_height() - tablero_alto) // 2

    # Dibujar el tablero
    for fila in range(filas):
        for col in range(columnas):
            x = offset_x + (margen + ancho_casilla) * col + margen
            y = offset_y + (margen + ancho_casilla) * fila + margen
            
            # Seleccionar imagen según el estado de la celda
            if matriz[fila][col] == 0:  # Agua
                pantalla.blit(agua_img, (x, y))
            elif matriz[fila][col] == 1:  # Barco golpeado
                pantalla.blit(barco_img, (x, y))
            else:  # Fallo
                pantalla.blit(fallo_img, (x, y))
            
            # Opcional: mantener el borde negro
            rect = pygame.Rect(x, y, ancho_casilla, ancho_casilla)
            pygame.draw.rect(pantalla, (0, 0, 0), rect, 1)


def obtener_celda_click(x:int, y:int, filas:int, columnas:int, ancho_casilla:int, margen:int, offset_x:int, offset_y:int)-> tuple:

    """
    Obtiene la celda en la que se hizo clic, considerando el offset y los márgenes.
    
    Args:
    x: Coordenada X del clic.
    y: Coordenada Y del clic.  
    filas: Número de filas del tablero.
    columnas: Número de columnas del tablero.
    ancho_casilla: Ancho de cada casilla del tablero.
    margen: Margen entre las casillas.
    offset_x: Desplazamiento en X del tablero.
    offset_y: Desplazamiento en Y del tablero.

    Returns:
    Una tupla (fila, columna) si el clic está dentro del área del tablero, o None si está fuera.

    """

    # Ajustar coordenadas restando el offset
    x_rel = x - offset_x
    y_rel = y - offset_y
    
    # Si el click está fuera del área del tablero
    if x_rel < 0 or y_rel < 0:
        return None
    
    # Calcular posición relativa considerando márgenes
    col = x_rel // (ancho_casilla + margen)
    fila = y_rel // (ancho_casilla + margen)
    
    # Verificar límites del tablero
    if 0 <= fila < filas and 0 <= col < columnas:
        return (fila, col)
    return None


def verificar_hundidos(matriz_disparos:list, posiciones_barcos:list) -> tuple:
    """
    Verifica si algún barco ha sido hundido en la matriz de disparos y devuelve el estado del hundimiento.
    
    Args:
    matriz_disparos: Matriz que representa los disparos realizados, donde 1 indica un disparo exitoso (hundido) y 2 indica un disparo fallido.
    posiciones_barcos: Diccionario que contiene las posiciones de los barcos, donde cada clave es

    Returns:
    Una tupla (hundido, tamaño_hundido) donde:
    - hundido: Booleano que indica si algún barco ha sido hundido.
    - tamaño_hundido: Entero que indica el tamaño del barco hundido.

    """
    hundido = False
    tamaño_hundido = 0

    for nombre_barco, lista_barcos in posiciones_barcos.items():
        for barco in list(lista_barcos):
            if all(matriz_disparos[f][c] == 1 for f, c in barco):
                hundido = True
                tamaño_hundido = len(barco)  # Obtenemos el tamaño del barco
                lista_barcos.remove(barco)
                break  # Salimos del bucle al encontrar el primer barco hundido
        if hundido:
            break
    
    return (hundido, tamaño_hundido)


def todos_barcos_hundidos(coordenadas_barcos:list, matriz_disparos:list) -> bool:
    
    """
    Verifica si todos los barcos han sido hundidos en la matriz de disparos.
    
    Args:
    coordenadas_barcos: Lista de tuplas con las coordenadas de los barcos.
    matriz_disparos: Matriz que representa los disparos realizados, donde 1 indica un disparo exitoso (hundido) y 2 indica un disparo fallido.

    Returns:
    True si todos los barcos están hundidos, False en caso contrario.

    """
    # Recorre las coordenadas de los barcos
    # y verifica si todas están marcadas como hundidas (1)
    for fila, columna in coordenadas_barcos:
        if matriz_disparos[fila][columna] != 1:
            return False
    return True


def mostrar_puntaje_pantalla(puntaje_jugador:str, PANTALLA:pygame.Surface):



    
    
    """
    Genera y muestra el texto en pantalla utilizando imágenes de letras, permitiendo que el jugador vea su nombre ingresado en la pantalla de registro de puntajes.
    
    Args:
    texto: Texto que se mostrará en pantalla.
    PANTALLA: Superficie de Pygame donde se dibujará el texto

    Returns:
    None

    """
    
    # Cargar imágenes de números y símbolos
    texto_simobolo_menos = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/simbolo_menos_png.png')
    texto_simobolo_menos = pygame.transform.scale(texto_simobolo_menos, (60, 70))
    texto_cero = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_0_png.png')
    texto_cero = pygame.transform.scale(texto_cero, (70, 70))
    texto_uno = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_1_png.png')
    texto_uno = pygame.transform.scale(texto_uno, (70, 70))
    texto_dos = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_2_png.png')
    texto_dos = pygame.transform.scale(texto_dos, (70, 70))
    texto_tres = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_3_png.png')
    texto_tres = pygame.transform.scale(texto_tres, (70, 70))
    texto_cuatro = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_4_png.png')
    texto_cuatro = pygame.transform.scale(texto_cuatro, (70, 70))
    texto_cinco = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_5_png.png')
    texto_cinco = pygame.transform.scale(texto_cinco, (70, 70))
    texto_seis = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_6_png.png')
    texto_seis = pygame.transform.scale(texto_seis, (70, 70))
    texto_siete = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_7_png.png')
    texto_siete = pygame.transform.scale(texto_siete, (70, 70))
    texto_ocho = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_8_png.png')
    texto_ocho = pygame.transform.scale(texto_ocho, (70, 70))
    texto_nueve = pygame.image.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_png/numero_9_png.png')
    texto_nueve = pygame.transform.scale(texto_nueve, (70, 70))


    # Posición base (como la tenías)
    pos_x = 810
    pos_y = 60
    
    # Convertir el puntaje a string
    str_puntaje = str(puntaje_jugador)
    
    # Calcular el ancho total del puntaje
    ancho_total = len(str_puntaje) * 75  # 75px por dígito (ajusta si es diferente)
    if '-' in str_puntaje:
        ancho_total -= 15  # Ajuste para el símbolo negativo que es más angosto
    
    # Calcular posición X inicial para centrar
    pos_x_inicial = (pos_x - ancho_total) // 2
    
    # Mostrar cada dígito
    for i, digito in enumerate(str_puntaje):
        if digito == '-':
            PANTALLA.blit(texto_simobolo_menos, (pos_x_inicial + i*75, pos_y))
        elif digito == '0':
            PANTALLA.blit(texto_cero, (pos_x_inicial + i*75, pos_y))
        elif digito == '1':
            PANTALLA.blit(texto_uno, (pos_x_inicial + i*75, pos_y))
        elif digito == '2':
            PANTALLA.blit(texto_dos, (pos_x_inicial + i*75, pos_y))
        elif digito == '3':
            PANTALLA.blit(texto_tres, (pos_x_inicial + i*75, pos_y))
        elif digito == '4':
            PANTALLA.blit(texto_cuatro, (pos_x_inicial + i*75, pos_y))
        elif digito == '5':
            PANTALLA.blit(texto_cinco, (pos_x_inicial + i*75, pos_y))
        elif digito == '6':
            PANTALLA.blit(texto_seis, (pos_x_inicial + i*75, pos_y))
        elif digito == '7':
            PANTALLA.blit(texto_siete, (pos_x_inicial + i*75, pos_y))
        elif digito == '8':
            PANTALLA.blit(texto_ocho, (pos_x_inicial + i*75, pos_y))
        elif digito == '9':
            PANTALLA.blit(texto_nueve, (pos_x_inicial + i*75, pos_y))