import pygame

pygame.mixer.init(44100, -16, 4, 512)
pygame.init()

class Game(object):
    
    def __init__(self, width, height):
        self.size = (width, height)
        display = pygame.display.set_mode(self.size)
        
    def play(self):
        joy = pygame.joystick.Joystick(0)
        joy.init()
        while True:
            evt = pygame.event.wait()
            print 'joy' in evt.dict
            
        
        
        
g = Game(680, 480)
g.play()
