import pygame
pygame.mixer.pre_init(22050, -16, 1, 128)
pygame.init()
sound = pygame.mixer.Sound('mid_C.ogg')


class Game(object):
    def __init__(self,width, height):
        self.size = (width, height)
        display = pygame.display.set_mode(self.size)
        self.channel = pygame.mixer.find_channel(False)
        self.js = pygame.joystick.Joystick(0)
        self.js.init()
        
    def play(self):
        while True:
            self.event = pygame.event.wait()
           #self.channel.play(sound)
            if self.event.type == pygame.QUIT:
                break
            elif self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 14:
                self.channel.play(sound)
g = Game(680,480)
g.play()