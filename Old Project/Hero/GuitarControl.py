import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

PowerChord = [ pygame.mixer.Sound('PowerChord%d.ogg' % i) for i in [1, 4, 3, 2] ]
class Game(object):
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)
        
        self.green = 5
        self.red = 1
        self.yellow = 0
        self.blue = 2
        self.orange = 3
        self.rock = 4
        self.twangerDown = 14
        self.twangerUp = 12
        self.select = 8
        self.start = 9
        self.currentButton = self.green

        self.buttonMap = { self.green:0, self.red:1, self.yellow:2,  self.blue:3, self.orange:4 }
        self.buttonDownMap = {self.green:False, self.red:False, self.yellow:False, self.blue:False, self.orange:False}
#        self.inverseButtonMap = { 0:self.green, 1:self.red, 2:self.yellow, 3:self.blue, 4:self.orange }

        self.js = pygame.joystick.Joystick(0)
        self.js.init()

        self.snd = None
        self.chan = None
        
    def run2(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == self.start:
                    exit()
                if self.isFretButton(event.button):
                    self.buttonDownMap[event.button] = True
                    if self.buttonMap[self.currentButton] <= self.buttonMap[event.button]:
                        self.clearSound()
                        self.setSound(event.button)
                    
                elif event.button in [self.twangerUp, self.twangerDown]:
                    self.stopSound()
                    if self.snd:
                        self.chan = self.snd.play()
                        
            elif event.type == pygame.JOYBUTTONUP:
                    if self.isFretButton(event.button):
                        self.buttonDownMap[event.button] = False
                        if self.buttonMap[self.currentButton] == self.buttonMap[event.button]:
                            self.clearSound()
                            for i in [self.green, self.red, self.yellow, self.blue, self.orange]:
                                if self.buttonDownMap[i] == True:
                                    self.setSound(i)
            
            else:
                continue
                        
                    
    def setSound(self, button):
        self.snd = PowerChord[self.buttonMap[button]]
        self.currentButton = button
        
    def clearSound(self):
        self.fadeSound()
        self.snd = None
        self.currentButton = self.green
        
    def clearStopSound(self):
        self.stopSound()
        self.snd = None
        self.currentButton = self.green
        
    def stopSound(self):
        if self.chan:
            self.chan.stop()
            
    def fadeSound(self):
        if self.chan:
            self.chan.fadeout(500)
            
    def isFretButton(self, button):
        return button in self.buttonMap

    def run(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button in self.buttonMap:
                    self.snd = PowerChord[self.buttonMap[event.button]]
                    
                elif event.button in [self.twangerUp, self.twangerDown]: # twanger
                    if self.snd:
                        self.chan = self.snd.play()

                else:
                    print event.button

            elif event.type == pygame.JOYBUTTONUP:
                if self.chan:
                    self.chan.stop()
            else:
                continue
            
            # clear the display
            #self.display.fill((0,0,0))

            # draw here
            
            # show it
            #pygame.display.flip()

g = Game(640,480)
g.run2()
