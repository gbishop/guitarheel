#~ #from guitar import Guitar
import pygame
#~ #PowerChord = [ pygame.mixer.Sound('PowerChord%d.ogg' % i) for i in [1, 4, 3, 2] ]
#~ TestSounds = [pygame.mixer.Sound('HighNoNote.ogg'),pygame.mixer.Sound('HighGreenNote.ogg'), pygame.mixer.Sound('HighRedNote.ogg'), pygame.mixer.Sound('HighYellowNote.ogg'), pygame.mixer.Sound('HighBlueNote.ogg'), pygame.mixer.Sound('HighOrangeNote.ogg'),pygame.mixer.Sound('LowNoNote.ogg'),pygame.mixer.Sound('LowGreenNote.ogg'), pygame.mixer.Sound('LowRedNote.ogg'), pygame.mixer.Sound('LowYellowNote.ogg'), pygame.mixer.Sound('LowBlueNote.ogg'), pygame.mixer.Sound('LowOrangeNote.ogg')]

size = (680, 480)
display = pygame.display.set_mode(size)
display = pygame.display.set_mode(size)
#~ js = pygame.joystick.Joystick(0)k
#~ js.init()
#~ mainGuitar = Guitar(js.get_id())
#~ mainGuitar.setGreen(5)
#~ mainGuitar.setRed(1)
#~ mainGuitar.setYellow(0)
#~ mainGuitar.setBlue(2)
#~ mainGuitar.setOrange(3)
#~ mainGuitar.setTwangerDown(14)
#~ mainGuitar.setTwangerUp(12)
#~ mainGuitar.setSoundList(TestSounds)

from GuitarMaker import GuitarMaker
from guitar import Guitar
#~ import pygame
js = pygame.joystick.Joystick(0)
js.init()
gm = GuitarMaker()
mainGuitar = gm.makeGuitar(js)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    else:
        mainGuitar.handleButton(event)