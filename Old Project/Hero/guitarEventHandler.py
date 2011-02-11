import pygame
pygame.init()
from guitar import Guitar

class GuitarEventHandler(object):
    def __init__(self, guitars):
        self.guitarList = guitars
            
    def handleEvent(self, event):
      if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
          self.guitarList[event.joy].handleButton(event)