import pygame
import sys
from guitar import Guitar
pygame.mixer.pre_init(22050, -16, 1, 128)
pygame.init()
TestSounds = [pygame.mixer.Sound('HighNoNote.ogg'),pygame.mixer.Sound('HighGreenNote.ogg'), pygame.mixer.Sound('HighRedNote.ogg'), pygame.mixer.Sound('HighYellowNote.ogg'), pygame.mixer.Sound('HighBlueNote.ogg'), pygame.mixer.Sound('HighOrangeNote.ogg'),pygame.mixer.Sound('LowNoNote.ogg'),pygame.mixer.Sound('LowGreenNote.ogg'), pygame.mixer.Sound('LowRedNote.ogg'), pygame.mixer.Sound('LowYellowNote.ogg'), pygame.mixer.Sound('LowBlueNote.ogg'), pygame.mixer.Sound('LowOrangeNote.ogg')]

PowerChord = [ pygame.mixer.Sound('GuitarChord%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]

CAcoustic = []
CAcoustic.extend([pygame.mixer.Sound('mid_%s.ogg' % str) for str in ['D', 'E', 'F', 'G', 'A', 'B']])
CAcoustic.extend([pygame.mixer.Sound('low_%s.ogg' % str) for str in ['E', 'F', 'G', 'A', 'B']])
CAcoustic.append(pygame.mixer.Sound('mid_C.ogg'))

NiceAcoustic = [pygame.mixer.Sound('major_%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
acoustic = [pygame.mixer.Sound('acoustic%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]

RockGuitar = [pygame.mixer.Sound('rock%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
minor = [pygame.mixer.Sound('minor%d.ogg' % i) for i in [2,1,3,4,5,6,2,1,3,4,5,6]]
sax = [pygame.mixer.Sound('sax%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
trumpet = [pygame.mixer.Sound('trumpet%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
nylon = [pygame.mixer.Sound('nylon%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
organ = [pygame.mixer.Sound('organ%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
rhodes = [pygame.mixer.Sound('Rhodes%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]
piano = [pygame.mixer.Sound('piano%d.ogg' % i) for i in [1,2,3,4,5,6,1,2,3,4,5,6]]


class GuitarMakerEmulator(object):
    def makeGuitar(self, js):
        self.joyStick = js
        for s in CAcoustic:
          print s
        self.sounds = [PowerChord, CAcoustic, NiceAcoustic, RockGuitar, minor, nylon, sax, trumpet,  organ, rhodes, piano]
        self.maxSound = len(self.sounds)
        self.sound = None
        self.channel = None
        self.newGuitar = Guitar(js.get_id())
        self.newGuitar.setGreen(5)
        self.newGuitar.setRed(1)
        self.newGuitar.setYellow(0)
        self.newGuitar.setBlue(2)
        self.newGuitar.setOrange(3)
        self.newGuitar.setTwangerDown(14)
        self.newGuitar.setTwangerUp(12)
        self.newGuitar.setSoundList(self.pickSound())
        return self.newGuitar
        
    def pickSound(self):
        self.currentSound = 0
        self.previousSound = -1
        while True:
          if(not self.currentSound == self.previousSound):
              if(self.currentSound == self.maxSound):
                  self.currentSound = 0
              elif(self.currentSound == -1):
                self.currentSound = self.maxSound - 1
              self.previousSound = self.currentSound
                
              self.sound = self.sounds[self.currentSound]
              self.play()
          self.event = pygame.event.wait()
          if self.event.type == pygame.QUIT:
              sys.exit(0)
          if self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_UP:
              self.currentSound += 1
          elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_DOWN:
              self.currentSound -= 1
          elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_RETURN:
              self.channel.stop()
              return self.sounds[self.currentSound]  
              
          if self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 14:
              self.currentSound += 1
          elif self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 12:
              self.currentSound -= 1
          elif self.event.type == pygame.JOYBUTTONDOWN and self.event.button == 5:
              self.channel.stop()
              return self.sounds[self.currentSound]
            
    def play(self):
      if not self.channel:
        self.channel = pygame.mixer.find_channel(False)
      self.channel.play(self.sound[0])
      