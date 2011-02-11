import pygame
from guitartest import Guitar
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
PowerChord = [ pygame.mixer.Sound('GuitarChord%d.ogg' % i) for i in [1,2,3,4,5,6] ]
joyBindings = [5,1,0,2,3,6,4,14,12,8,9]
g = Guitar(joyBindings, PowerChord)
self.size = (640, 480)
self.display = pygame.display.set_mode(self.size)
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    elif g.isGuitarEvent(event):
        g.handleEvent(event)