import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

PowerChord = [ pygame.mixer.Sound('PowerChord%d.ogg' % i) for i in [1, 4, 3, 2] ]
class Game(object):
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)

        self.buttonMap = { 5:0, 1:1, 0:2, 2:3 }

        self.js = pygame.joystick.Joystick(0)
        self.js.init()

        self.snd = None
        self.chan = None

    def run(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button in self.buttonMap:
                    self.snd = PowerChord[self.buttonMap[event.button]]
                    
                elif event.button in [12, 14]: # twanger
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
g.run()
