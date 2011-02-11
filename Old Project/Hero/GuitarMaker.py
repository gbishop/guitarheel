import pygame
import sys
from guitar import Guitar
pygame.mixer.pre_init(22050, -16, 1, 128)
pygame.init()
TestSounds = [pygame.mixer.Sound('HighNoNote.ogg'),pygame.mixer.Sound('HighGreenNote.ogg'), pygame.mixer.Sound('HighRedNote.ogg'), pygame.mixer.Sound('HighYellowNote.ogg'), pygame.mixer.Sound('HighBlueNote.ogg'), pygame.mixer.Sound('HighOrangeNote.ogg'),pygame.mixer.Sound('LowNoNote.ogg'),pygame.mixer.Sound('LowGreenNote.ogg'), pygame.mixer.Sound('LowRedNote.ogg'), pygame.mixer.Sound('LowYellowNote.ogg'), pygame.mixer.Sound('LowBlueNote.ogg'), pygame.mixer.Sound('LowOrangeNote.ogg')]

PowerChord = [ pygame.mixer.Sound('GuitarChord%d.ogg' % i) for i in [6, 5, 4, 3,2,1,6,5,4,3,2,1]]

MajorMinorAcoustic = [pygame.mixer.Sound('Acoustic_Cm.mid'),pygame.mixer.Sound('Acoustic_Cm.mid'), pygame.mixer.Sound('Acoustic_Am.mid'), pygame.mixer.Sound('Acoustic_Gm.mid'), pygame.mixer.Sound('Acoustic_Em.mid'), pygame.mixer.Sound('Acoustic_Dm'),pygame.mixer.Sound('Acoustic_C.mid'),pygame.mixer.Sound('Acoustic_C.mid'), pygame.mixer.Sound('Acoustic_A.mid'), pygame.mixer.Sound('Acoustic_G.mid'), pygame.mixer.Sound('Acoustic_E.mid'), pygame.mixer.Sound('Acoustic_D')]



class GuitarMaker(object):
    def makeGuitar(self, js):
        self.joyStick = js
        self.soundMap = {0:TestSounds, 1:PowerChord}
        self.newGuitar = Guitar(js.get_id())
        self.setButton(0,self.newGuitar.setGreen)
        self.setButton(1,self.newGuitar.setRed)
        self.setButton(2,self.newGuitar.setYellow)
        self.setButton(3,self.newGuitar.setBlue)
        self.setButton(4,self.newGuitar.setOrange)
        self.setButton(5,self.newGuitar.setTwangerDown)
        self.setButton(6,self.newGuitar.setTwangerUp)
        self.newGuitar.setSoundList(self.soundMap[0])
        return self.newGuitar
            
            
    def setButton(self, index, setMethod):
        self.buttonSet = False
        breakout = False
        print "Hold Down %d button" % (index)
        while not self.buttonSet or breakout:
            self.event = pygame.event.wait()
            if self.event.type == pygame.QUIT:
                sys.exit(0)
            elif self.event.type == pygame.JOYBUTTONDOWN:
                self.possibleButton = self.event.button
                if self.event.joy == self.joyStick.get_id():
                    print "Press enter to varify for %d" % (self.possibleButton)
                    self.event = pygame.event.wait()
                    if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_RETURN:
                        setMethod(self.possibleButton)
                        self.buttonSet = True
                    elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_D:
                        breakout = True
        
            
        