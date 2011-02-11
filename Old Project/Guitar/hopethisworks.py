from Guitar import Guitar
import pygame
PowerChord = [ pygame.mixer.Sound('PowerChord%d.ogg' % i) for i in [1, 4, 3, 2] ]
TestSounds = [pygame.mixer.Sound('HighNoNote.ogg'),pygame.mixer.Sound('HighGreenNote.ogg'), pygame.mixer.Sound('HighRedNote.ogg'), pygame.mixer.Sound('HighYellowNote.ogg'), pygame.mixer.Sound('HighBlueNote.ogg'), pygame.mixer.Sound('HighOrangeNote.ogg'),pygame.mixer.Sound('LowNoNote.ogg'),pygame.mixer.Sound('LowGreenNote.ogg'), pygame.mixer.Sound('LowRedNote.ogg'), pygame.mixer.Sound('LowYellowNote.ogg'), pygame.mixer.Sound('LowBlueNote.ogg'), pygame.mixer.Sound('LowOrangeNote.ogg')]

self.size = (width, height)
self.display = pygame.display.set_mode(self.size)
self.js = pygame.joystick.Joystick(0)
self.js.init()
self.mainGuitar = Guitar(self.js.get_id())
self.mainGuitar = setGreen(5)
self.mainGuitar = setRed(1)
self.mainGuitar = setYellow(0)
self.mainGuitar = setBlue(2)
self.mainGuitar = setOrange(3)
self.mainGuitar = setTwangerDown(14)
self.mainGuitar = setTangwerUp(12)
    
    
        