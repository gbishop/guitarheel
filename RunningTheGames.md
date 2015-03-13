# Running Horse, Simon Says, and Free Play #

These games are run through the gamedemo.py class. You run the gamedemo file through terminal and the game you play and controllers you use is based off the parameters you pass in. The basic structure of this call is

```
python gamedemo.py <gamename> <instrument> <controller> <instrument> <controller>
```

The game names are: “horse”, “simonsays”, and “freeplay”

The instrument can be any of our avaliable instruments, but for now “electricguitar” is recommended.

The controller is either “keyboard”, or the id of the joystick you wish to you. If you’re using EMS adaptors and want to use more than one controller you will likely use the ids 0 and 2.

You don’t need to pass in the instrument and controller parameter. If you don’t it defaults to the keyboard, if you send in none or only one pair it will allow simonsays and freeplay to be played, but horse will not run

example:
```
python gamedemo.py freeplay electricguitar keyboard electricguitar 0
```