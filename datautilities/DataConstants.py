import pygame.key

class Constants(object):
    SPOKEN_NAME = 'SPOKEN_NAME'
    OPEN = 'OPEN'
    GREEN = 'GREEN'
    RED = 'RED'
    YELLOW = 'YELLOW'
    BLUE = 'BLUE'
    ORANGE = 'ORANGE'
    TWANGERDOWN = 'TDOWN'
    TWANGERUP = 'TUP'
    SHAKE = 'SHAKE'
    START = 'START'
    SELECT = 'SELECT'
    TEST_GUITAR_MAP = {
        -1: OPEN,
        5: GREEN,
        1: RED,
        0: YELLOW,
        2: BLUE,
        3: ORANGE,
        14: TWANGERDOWN,
        12: TWANGERUP,
        4:SHAKE,
        9: START,
        8: SELECT,
    }
    
    KEYBOARD_GUITAR_MAP = {
        -1: OPEN,
        pygame.K_a: GREEN,
        pygame.K_s: RED,
        pygame.K_d: YELLOW,
        pygame.K_f: BLUE,
        pygame.K_g: ORANGE,
        pygame.K_SPACE: TWANGERDOWN,
        pygame.K_SPACE: TWANGERUP,
        pygame.K_1: SHAKE,
        pygame.K_q: START,
        pygame.K_w: SELECT,        
    }
