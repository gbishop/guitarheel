import pygame
pygame.mixer.init(44100, -16, 4, 512)
pygame.init()
size = (500, 500)
display = pygame.display.set_mode(size)
sound=pygame.mixer.Sound('notes/acoustic/acoustic1.ogg')
channel = sound.play()
while True:
    e = pygame.event.get()
    for event in e:
        if(not channel.get_busy()):
            channel = sound.play()
