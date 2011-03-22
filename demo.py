import pygame
from sounds.SoundBoxes import GuitarSoundBox
pygame.mixer.init(44100, -16, 2, 512)
pygame.init()

uk = 'notes/ukulele/'
a = [uk+'C.ogg', uk+'D.ogg', uk+'E.ogg', uk+'F.ogg', uk+'G.ogg', uk+'A.ogg']
gsb = GuitarSoundBox(a, 1)

guitar = pygame.joystick.Joystick(0)
guitar.init()
guitar_map = {
    -1: GuitarSoundBox.NO_NOTE,
    5: GuitarSoundBox.GREEN_NOTE,
    1: GuitarSoundBox.RED_NOTE,
    0: GuitarSoundBox. YELLOW_NOTE,
    2: GuitarSoundBox.BLUE_NOTE,
    3: GuitarSoundBox.ORANGE_NOTE,
    }
    
guitar_fret_state = {
    GuitarSoundBox.NO_NOTE: 1,
    GuitarSoundBox.GREEN_NOTE: 0,
    GuitarSoundBox.RED_NOTE: 0,
    GuitarSoundBox.YELLOW_NOTE: 0,
    GuitarSoundBox.BLUE_NOTE: 0,
    GuitarSoundBox.ORANGE_NOTE: 0,
    }
evt = pygame.event.Event(0)

while(evt.type != pygame.QUIT):
    evt = pygame.event.wait()
    if(evt.type == pygame.JOYBUTTONDOWN):
        if(evt.button == 9):
            evt = pygame.event.Event(pygame.QUIT)
        elif(evt.button in guitar_map):
            guitar_fret_state[guitar_map[evt.button]] = 1
        elif(evt.button == 14 or evt.button == 12):
            #play sound
            for i in [5,4,3,2,1,0]:
                if(guitar_fret_state[i] == 1):
                    gsb.play(i)
                    break
    elif(evt.type == pygame.JOYBUTTONUP):
        if(evt.button in guitar_map):
            guitar_fret_state[guitar_map[evt.button]] = 0
