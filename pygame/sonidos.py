import pygame.mixer as mixer

# Musica y efectos de sonido

def musica_ambiental (condicion:bool):

    """
    Reproduce una musica ambiental en el menu de fondo mientras se ejecuta el juego.
    
    Args:
    condicion: Determina si se reproduce la musica ambiental o no. Si es True, se reproduce la musica ambiental, si es False no se reproduce.

    Returns:
    None

    """
    
    if condicion:
        mixer.music.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_musica/musica_ambiental.mp3')
        mixer.music.set_volume(0.4)
        mixer.music.play(-1)  
        mixer.music.play()


def efecto_boton (condicion):

    """
    Reproduce un efecto de sonido al presionar un boton en el menu.
    
    Args:
    condicion: Determina si se reproduce el efecto de sonido o no. Si es True, se reproduce el efecto de sonido, si es False no se reproduce.

    Returns:
    None

    """

    if condicion:
        efecto_button = mixer.Sound('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_musica/ruido_boton.mp3')
        efecto_button.set_volume(0.4)
        efecto_button.play()


def musica_jugando (condicion:bool):

    """
    reproduce la música ambiental del juego, permitiendo que el jugador escuche música mientras juega.
    
    Args:
    condicion: Determina si se reproduce la musica ambiental o no. Si es True, se reproduce la musica ambiental, si es False no se reproduce.

    Returns:
    None

    """
    
    if condicion:   
        mixer.music.load('C:/Users/alanb/OneDrive/Desktop/UTN Alan/Programacion/pygame/segundo_parcial/pygame/recursos_musica/musica_jugando.mp3')
        mixer.music.set_volume(0.4)  
        mixer.music.play(-1)
