import pygame
pygame.init()
joy = pygame.joystick.Joystick(0)
joy.init()
while True:
	evt = pygame.event.wait()
	print evt