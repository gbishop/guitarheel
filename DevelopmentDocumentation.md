# Introduction #

This document contains some basic information to get started with GuiTarHeel


# Getting Started With Guitar Heel #

In order to get started with the GuiTarHeel code base, you’ll first need to download and install python and pygame. We used python 2.6 and pygame 1.9.1 to develop the game. Python can be found here: www.python.org and pygame can be found at: www.pygame.org. Both the language python and the libraries are completely free to use.

You will also want to aquire a Guitar hero controller and a USB adapter for that controller. It is both possible and easy to play any of the GuiTarHeel games with a keyboard, but we find the guitar controller much more fun! Heads up though, if you use a PS2 adapter that has two controller ports, it will also register as two joysticks on your computer. If you see 2 joysticks when you only plugged in one, this is the reason.

# Structure of a Game #

The very core our GuiTarHeel is the minigame, and easy game extends the AbstractGame class inside the games module. Extending these games requires two things. One: That the first line in your games

```
__init__ function be AbstractGame.__init__(self)
```

This insures that your game will be set up with the right variables for use by the main loop. Two: Your game must extend the update method. You can find the information on this method in the AbstractGame class, but in general the method will return an array with the “running status” of the game so the main loop will know whether or not the game is still running. Inside the update loop you can handle all your game logic and display updates. The main loop guarantees that it will clear the event queue and pass all the events to update, then call update without an event before repeating the process again.

You can add any minigame you want by simple following the AbstractGame rules. Though a menu would need to be altered to allow for your new game to be selected. Any information about a game such as data storage (high scores, etc) and difficulty as kept inside its game class. Any outside classes it needs will be mentioned inside the documentation for that game.

# Making Noise #

The majority of noise making should be handled by SoundBoxes. The main SoundBox currently developed is the AdvGuitarSoundBox that handles all the sound playing for guitars. However, feel free to develop any new sound boxes for games.

Generally a SoundBox should have its own channel in order to play sounds to avoid sound overlap, and the number of different problems that can pop up with pygame sounds. This process is facilitated by the ChannelManager class in the sound module. The channel manage makes it easy for an object to reserve and unreserve a channel for use. If a sound box checks itself in to reserve a method it can be sure no other class will be able to use the channel without specifically requesting it. Check out the ChannelMangers documentation for more information.

# Controlling the Music #

A majority of the controls are currently handled through the guitar class. You’ll see this inside the instruments model, and the controlling mappings are contained inside the Constants class inside the datautilities module. A guitar makes noise using it’s own AdvSoundBox, and it’s all important button map. Be sure to read the Guitar class’s documentation for using the guitar.

# Game Data and You #

Outside data is particular important to GuiTarHeel. We devised our own simple file format to store information about the different possible collections of notes for each instrument.

Notes themselves should be stored inside the notes file which is inside the main directory. Inside the notes file you’ll find files named after different instruments. These file names are **important** and you will use these names to refer to the instruments both in the instrument data file AND inside the game. If a instrument isn’t being picked up this is a simple yet easy to make error to check. Inside easy instrument file are the instruments notes and these can be named whatever you want.

Inside the data file you’ll find notedata.dat. In this file is where you tell the game what instrument is which, and what note belows to which frets. It even allows for chords! The file syntax is simple, but its explained in the file, and that’s where you should go to understand the system.

This file is read by the class NoteDataReader inside the DataProcessors class inside the datautilities module.

# Current Game #

The games as the stand haven't all be tied together for numerous reasons. TwoPlayerFreePlay, SimonSays, and Horse all follow the recommended design, while SoundCatch does not. However, sound catcher currently works as a stand alone game which could be ported over to run in the recommended design.

You can see how the games are run by playing gamedemo.py and by looking inside the games classes themselves.

# What now? #

Much of the game has been documented, and if you have trouble the first step would be to try the games source code documentation. But now your best bet is to go out and make a small