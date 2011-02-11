import pygame
pygame.mixer.pre_init(22050, -16, 1, 64)
pygame.init()
from guitarEventHandler import GuitarEventHandler
from guitarsetup import GuitarSetUp
from DrumLoop import DrumLoop


class Game(object):
    def __init__(self,width, height):
        self.size = (width, height)
        self.channel = pygame.mixer.find_channel(False)
        display = pygame.display.set_mode(self.size)
        self.gs = GuitarSetUp()
        self.geh = GuitarEventHandler(self.gs.setUpGuitars())
        self.dl = DrumLoop()
        
    def play(self):
        self.dl.playDrum()
        while True:
            self.event = pygame.event.wait()
            if self.event.type == pygame.QUIT:
                break
            else:
                self.geh.handleEvent(self.event)

g = Game(680,480)
g.play()