import pygame
from guitar import Guitar
pygame.mixer.pre_init(44100,-16,1,512)
pygame.init()
TestSounds = [pygame.mixer.Sound('HighNoNote.ogg'),pygame.mixer.Sound('HighGreenNote.ogg'), pygame.mixer.Sound('HighRedNote.ogg'), pygame.mixer.Sound('HighYellowNote.ogg'), pygame.mixer.Sound('HighBlueNote.ogg'), pygame.mixer.Sound('HighOrangeNote.ogg'),pygame.mixer.Sound('LowNoNote.ogg'),pygame.mixer.Sound('LowGreenNote.ogg'), pygame.mixer.Sound('LowRedNote.ogg'), pygame.mixer.Sound('LowYellowNote.ogg'), pygame.mixer.Sound('LowBlueNote.ogg'), pygame.mixer.Sound('LowOrangeNote.ogg')]
PowerChord = [ pygame.mixer.Sound('PowerChord%d.ogg' % i) for i in [6, 5, 4, 3,2,1,6,5,4,3,2,1]]


class GuitarMaker(object):
    def makeGuitar(self, js):
        self.joyStick = js
        self.newGuitar = Guitar(js.get_id)
        self.setButton(0,self.newGuitar.setGreen)
        self.setButton(1,self.newGuitar.setRed)
        self.setButton(2,self.newGuitar.setYellow)
        self.setButton(3,self.newGuitar.setBlue)
        self.setButton(4,self.newGuitar.setOrange)
        self.setButton(5,self.setTwangerDown)
        self.setButton(6,self.setTwangerUp)
        self.newGuitar.setSoundList(TestSounds)
        return self.newGuitar
            
            
    def setButton(self, index, setMethod):
        self.buttonSet = False
        while not self.buttonSet:
            print "Enter %d button" % (index)
            self.event = pygame.event.wait()
            if self.event.type == pygame.QUIT:
                break
            elif self.event.type == pygame.JOYBUTTONDOWN:
                if self.event.joy.get_id == self.joystick.get_id:
                    setMethod(event.button)
                    self.buttonSet = True
        
            
        