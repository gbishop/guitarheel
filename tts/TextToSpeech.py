import os

speak = None
initiated = False
linux = 'posix'
windows = 'nt'

def init():
    global initiated
    if not initiated:
        initiated = True
        global speak
        opsys = os.name
        if opsys is linux:
            speak = linuxtts
        else:
            speak = windowstts
    


def linuxtts(text):
    os.system("espeak " + "'" + text + "'")
    
def windowsttx(text):
    pass
