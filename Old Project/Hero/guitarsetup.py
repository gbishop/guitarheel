import pygame
from GuitarMakerEmulator import GuitarMakerEmulator
from guitar import Guitar
pygame.init()

class GuitarSetUp(object):
    def setUpGuitars(self):
        self.gm = GuitarMakerEmulator()
        self.guitarList = []
        print pygame.joystick.get_count()
        for id in range(pygame.joystick.get_count() - pygame.joystick.get_count()/2):
            self.js = pygame.joystick.Joystick(id)
            self.js.init()
            print self.js.get_name()
            self.guitarList.append(self.gm.makeGuitar(self.js))
            
        return self.guitarList