import pygame
import random
import time
from datautilities.DataConstants import Constants
from games.AbstractGame import AbstractGame
from datautilities.DataConstants import Constants

class TwoPlayerFreePlay(AbstractGame):
    """A free play game for Two Players
    
    Authors: Logan Wilkerson
    """
    
    def __init__(self, channel_manager, guitar_one, guitar_two):
        """ Constructor for TwoPlayerFreePlay
        
        channel_manager -- the ChannelManager for the game
        guitar_one -- player one's guitar
        guitar_two -- player two's guitar
        """
        AbstractGame.__init__(self)
        self.channel_manager = channel_manager
        self.guitar_one = guitar_one
        self.guitar_two = guitar_two
        self.guitars = [self.guitar_one, self.guitar_two]
        
    def update(self, evt=None):
        if evt is not None:
            for guitar in self.guitars:
                if guitar.isEventSource(evt):
                    button = guitar.handleEvent(evt)
                    if button is Constants.START:
                        return [self.end_status, 'menu']
        return [self.running_status]
        
class Horse(AbstractGame):
    """A game of Horse for two players
    
    Authors: Logan Wilkerson
    """
    
    play_phase = 'PLAY'
    return_phase = 'RETURN'
    final_phase = 'FINAL'
    done_phase = 'DONE'
    def __init__(self, channel_manager, guitar_one, guitar_two, start_count, display):
        """Constructor for Horse
        
        channel_manager -- the ChannelManager for the game
        guitar_one -- player one's guitar
        guitar_two -- player two's guitar
        """
        AbstractGame.__init__(self)
        self.channel_manager = channel_manager
        self.guitars = [guitar_one, guitar_two]
        self.start_count = start_count
        self.max_count = start_count
        self.display = display
        self.background = pygame.Surface(self.display.get_size())
        self.background.fill((0,0,0))
        self.font = pygame.font.Font(None, 24)
        self.white = (255,255,255)
        
        self.cur_player = 0
        self.player_names = ['Player 1', 'Player 2']
        self.player_scores = [0, 0]
        self.horse_board = ['H', 'O', 'R', 'S', 'E']
        self.phase = Horse.play_phase
        self.cur_states = []
        self.return_states = []
        
        self.display.blit(self.background, (0,0))
        pygame.display.update()
        print 'Welcome to Horse!'
        pygame.display.set_caption("Horse!")
        print 'Player 1 please enter your notes.'
        self.message = self.font.render('Player 1 please enter your notes.', 1, self.white)
         
        
    def update(self, evt=None):
        if evt is not None:
            for g in self.guitars:
                g.handleEvent(evt, False)
            if self.phase is Horse.play_phase:
                if not self.guitars[self.cur_player].isEventSource(evt):
                    if self.guitars[self.cur_player - 1].isEventSource(evt):
                        self.guitars[self.cur_player - 1].handleEvent(evt, False)
                    return [self.running_status]
                else: #player guitar is source
                    button = self.guitars[self.cur_player].handleEvent(evt)
                    if self.guitars[self.cur_player].isPlay(evt, button):
                        self.cur_states.append(self.guitars[self.cur_player].getNote())
                        if len(self.cur_states) is self.max_count:
                            print self.cur_states
                            print 'That\'s enough ' + self.player_names[self.cur_player] + ' Return ' + self.player_names[self.cur_player - 1]
                            self.message = self.font.render(
                                            'That\'s enough ' + self.player_names[self.cur_player] +
                                            ' Return ' + self.player_names[self.cur_player - 1],
                                            1,
                                            self.white
                                            )
                                            
                            self.max_count += 1
                            self.phase = Horse.return_phase
            elif self.phase is Horse.return_phase:
                if not self.guitars[self.cur_player - 1].isEventSource(evt):
                    self.guitars[self.cur_player].handleEvent(evt,False)
                    return [self.running_status]
                else: #returning player is source
                    button = self.guitars[self.cur_player - 1].handleEvent(evt)
                    if self.guitars[self.cur_player - 1].isPlay(evt, button):
                        self.return_states.append(self.guitars[self.cur_player - 1].getNote())
                        if not self.cur_states[0:len(self.return_states)] == self.return_states:
                            print 'Wrong ' + self.player_names[self.cur_player - 1] + ' ' + self.player_names[self.cur_player] + ' can you repeat?'
                            self.message = self.font.render('Wrong ' +
                                            self.player_names[self.cur_player - 1] +
                                            ' ' + self.player_names[self.cur_player] +
                                            ' can you repeat?',
                                             1,
                                             self.white
                                            )
                                            
                            self.phase = Horse.final_phase
                            self.return_states = []                            
                        else:
                            if len(self.cur_states) is len(self.return_states):
                                #win
                                print 'Very good ' + self.player_names[self.cur_player - 1] + ' Now play your counter song.'
                                self.message = self.font.render('Very good '
                                                + self.player_names[self.cur_player - 1] +
                                                ' Now play your counter song.',
                                                1,
                                                self.white
                                                )
                                                
                                self.phase = Horse.play_phase
                                self.return_states = []
                                self.cur_states = []
                                if self.cur_player is 0:
                                    self.cur_player = 1
                                else:
                                    self.cur_player = 0
                            else:
                                #keep playing
                                pass 
            elif self.phase is Horse.final_phase: #final phase
                if not self.guitars[self.cur_player].isEventSource(evt):
                    self.guitars[self.cur_player].handleEvent(evt,False)
                    return [self.running_status]
                else:
                    button = self.guitars[self.cur_player].handleEvent(evt)
                    if self.guitars[self.cur_player].isPlay(evt, button):
                        self.return_states.append(self.guitars[self.cur_player].getNote())
                        if not self.cur_states[0:len(self.return_states)] == self.return_states:
                            print 'Wrong ' + self.player_names[self.cur_player] + ' ' + self.player_names[self.cur_player - 1] + '\'s turn now.'
                            self.message = self.font.render('Wrong ' +
                                            self.player_names[self.cur_player] +
                                            ' ' + self.player_names[self.cur_player - 1] +
                                            '\'s turn now.',
                                            1,
                                            self.white
                                            )
                                            
                            self.phase = Horse.play_phase
                            self.return_states = []
                            self.cur_states = []
                            self.max_count = self.start_count
                            if self.cur_player is 0:
                                self.cur_player = 1
                            else:
                                self.cur_player = 0
                        else: #win for cur player
                            if len(self.cur_states) is len(self.return_states):
                                print 'Very good ' + self.player_names[self.cur_player] + '.'
                                self.player_scores[self.cur_player - 1] += 1
                                self.message = self.font.render('Very good ' + self.player_names[self.cur_player] + '.', 1, self.white)
                                print 'Player 1 '
                                print self.horse_board[0:self.player_scores[0]]
                                print 'Player 2 '
                                print self.horse_board[0:self.player_scores[1]]
                                for score in self.player_scores:
                                    if score is 5:
                                        self.phase = Horse.done_phase
                                if not self.phase is Horse.done_phase:
                                    print 'Time to make up for it other player.'
                                    self.message = self.font.render('Time to make up for it other player.', 1, self.white)
                                    if self.cur_player is 0:
                                        self.cur_player = 1
                                    else:
                                        self.cur_player = 0
                                    self.phase = Horse.play_phase
                                    self.max_count = self.start_count
                                    self.cur_states = []
                                    self.return_states = []
                    else:
                        pass
        else:
            self.updateDisplay()
            if self.phase is Horse.done_phase:
                if self.player_scores[0] < self.player_scores[1]:
                    print 'Player 1 wins!'
                    self.message = self.font.render('Player 1 wins!', 1, self.white)
                else:
                    print 'Player 2 wins!'
                    self.message = self.font.render('Player 2 wins!', 1, self.white)
                return [self.end_status]
        return [self.running_status]
    
    def updateDisplay(self):
        self.display.blit(self.background, (0,0))
        pos = self.message.get_rect(centerx=self.display.get_width()/2)
        self.display.blit(self.message, pos)
        player1message = self.font.render('Player 1 score: ' +
                            ''.join(self.horse_board[0:self.player_scores[0]]),
                            1,
                            self.white
                            )
                            
        pos1 = player1message.get_rect(bottomleft=(0,self.display.get_height()))
        self.display.blit(player1message, pos1)
        player2message = self.font.render('Player 2 score: ' +
                            ''.join(self.horse_board[0:self.player_scores[1]]),
                            1,
                            self.white
                            )
                            
        pos2 = player2message.get_rect(bottomright=(self.display.get_width(), self.display.get_height()))
        self.display.blit(player2message, pos2)
        pygame.display.update()


class SimonSays(AbstractGame):
    """A game of Simon Says for one player
    
    Authors: Logan Wilkerson,
    """
    
    simon_phase = 'SIMON'
    play_phase = 'PLAY'
    end_phase = 'END'
    def __init__(self, channel_manager, guitar_one, start_count, display):
        """Constructor for SimonSays
        
        channel_manager -- the ChannelManager for the game
        guitar_one -- player one's guitar
        start_count -- the starting amount of notes
        display -- the game display
        """
        AbstractGame.__init__(self)
        self.channel_manager = channel_manager
        self.guitar = guitar_one
        self.start_count = self.max_count = start_count
        self.phase = SimonSays.simon_phase
        self.display = display
        
        self.background = pygame.Surface(self.display.get_size())
        self.font = pygame.font.Font(None, 30)
        
        self.white = (255,255,255)
        
        self.cur_states = []
        self.return_states = []
        
        self.background.fill((0,0,0))
        self.display.blit(self.background, (0,0))
        pygame.display.update()
        pygame.display.set_caption('Simon Says!')
        self.message = self.font.render(
                        'Please listen to the notes.',
                        1,
                        self.white
                    )
                        
    def update(self, evt=None):
        if evt is None:
            return self.updateWithoutEvent()
        else:
            return self.updateWithEvent(evt)
            
    def updateWithEvent(self, evt):
        if self.phase is SimonSays.play_phase:
            if self.guitar.isEventSource(evt):
                button = self.guitar.handleEvent(evt)
                if button is Constants.START:
                    return [self.end_status]
                if self.guitar.isPlay(evt, button):
                    self.return_states.append(self.guitar.getNote())
                    if not self.cur_states[0:len(self.return_states)] == self.return_states:
                        self.message = self.font.render(
                                        'That\'s wrong. You lose. You got %i points.' % (len(self.cur_states) - 1),
                                        1,
                                        self.white
                                    )
                        self.phase = SimonSays.end_phase
                    elif len(self.return_states) is len(self.cur_states):
                        self.message = self.font.render(
                                        'Very good player!',
                                        1,
                                        self.white,
                                    )
                        self.return_states = []
                        self.phase = SimonSays.simon_phase
        if self.phase is SimonSays.end_phase:
            button = self.guitar.handleEvent(evt)
            if button is Constants.START:
                return [self.end_status]
                
        return [self.running_status]
        
    def updateWithoutEvent(self):
        self.display.blit(self.background, (0,0))
        pos = self.message.get_rect(
                centerx = self.display.get_width() / 2,
                centery = self.display.get_height() / 2,
            )
        self.display.blit(self.message, pos)
        pygame.display.update()
        if self.phase is SimonSays.simon_phase:
            self.runSimonPhase()
        return [self.running_status]
        
    def runSimonPhase(self):
        time.sleep(1)
        nextNote = random.choice(self.guitar.getNotes())
        self.cur_states.append(nextNote)
        while len(self.cur_states) < self.start_count:
            nextNote = random.choice(self.guitar.getNotes())
            self.cur_states.append(nextNote)
        channel = self.guitar.getSoundBox().channel
        print self.cur_states
        for note in self.cur_states:
            self.guitar.playNote(note)
            while channel.get_busy():
                events = pygame.event.get()
                for evt in events:
                    if self.guitar.isEventSource(evt):
                        self.guitar.handleEvent(evt, False)
        self.phase = SimonSays.play_phase
        self.message = self.font.render('Now play it back.', 1, self.white)
        
