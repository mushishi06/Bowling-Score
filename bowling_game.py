# -*- coding: utf-8 -*- #
"""Python3 Bowling Game."""
import random


class BowlingGame():
    """Main class for Bowling Game."""

    def __init__(self, player="Player 1"):
        """Initialize the board, name."""
        self.player = player
        self.rolls = []
        self.frames = [['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', '', '']]
        self.score = ['', '', '', '', '', '', '', '', '', '']
        self.current_roll = 0
        self.curr_last_frame = 0
        self.current_fram = 0

    def total_score(self):
        """Return the current score."""
        return self.score[self.current_fram]

    def scoresheet(self):
        """Print the scoreSheet."""
        print(self.player)
        sep = "___________________________________________"
        print(sep)
        print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10  |")
        pins = "|"
        for frame in self.frames:
            if frame[0] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                frame_one = ' '
            elif frame[0] == 0:
                frame_one = '-'
            elif frame[0] == 10:
                frame_one = 'X'
            else:
                frame_one = frame[0]
            if frame[1] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                frame_two = ' '
            elif int(frame[1]) == int(0):
                frame_two = '-'
            elif frame[1] == 10:
                if len(frame) == 3:
                    frame_two = 'X'
                else:
                    frame_one = 'X'
            elif (frame[0] + frame[1]) == 10:
                frame_two = '/'
            else:
                frame_two = frame[1]

            pins += str(frame_one) + "|" + str(frame_two) + "|"
            if len(frame) == 3:
                if not frame[1]:
                    pins += ' |'
                else:
                    if frame[2] == 0:
                        pins += '-|'
                    elif frame[2] == 10:
                        pins += 'X|'
                    else:
                        pins += str(frame[2]) + "|"
        print(pins)
        print("|   |   |   |   |   |   |   |   |   |     |")
        print(self.score)
        print(sep)

    def roll(self, pins):
        """Emulate the Ball launch."""
        self.rolls.append(pins)
        if self.current_fram < 9:
            self.frames[self.current_fram][self.current_roll % 2] = pins
            if self._is_spare(self.frames[self.current_fram - 1]):
                if self.current_fram < 2:
                    self.score[self.current_fram - 1] = 10 + self.frames[self.current_fram][0]
                else:
                    self.score[self.current_fram - 1] = self.score[self.current_fram - 2] + 10 + self.frames[self.current_fram][0]
            self.calcul_strike(self.current_fram)
            if pins == 10 and self.current_fram < 9:
                self.current_roll += 1
            self.current_roll += 1
            if not self.current_roll % 2 and self.current_fram < 9:
                self.current_fram += 1
        else:
            self.frames[9][self.curr_last_frame] = pins
            if self._is_spare(self.frames[self.current_fram - 1]):
                self.score[self.current_fram - 1] = self.score[self.current_fram - 2] + 10 + self.frames[self.current_fram][0]
            self.calcul_strike(self.current_fram)
            self.curr_last_frame += 1

    def ranroll(self):
        """Call the roll function with a random number [0-10]."""
        limit_max = 10 - (self.frames[self.current_fram][0]) if self.current_roll % 2 else 10
        self.roll(random.randint(0, limit_max))

    def number_strike(self, curr_fr=0, nb_strike=0):
        """Give the number of strike raw."""
        if curr_fr > 0 and self._is_strike(self.frames[curr_fr - 1]) and not self.score[curr_fr - 1]:
            nb_strike = self.number_strike(curr_fr - 1, nb_strike + 1)
        return nb_strike

    def calcul_strike(self, curr_fr=0):
        """Calcul for strike particular case."""
        nb_strike = self.number_strike(self.current_fram)
        if nb_strike == 2:
            self.score[curr_fr - 2] = int(self.score[curr_fr - 3]) + 20 + self.frames[curr_fr][0] if (self.score[curr_fr - 3]) != '' else 30
        elif nb_strike == 1 and not self._is_strike(self.frames[curr_fr]) and self._is_frame_completed(self.frames[curr_fr]):
            if curr_fr - 1 == 0:
                self.score[0] = 10 + self._get_total_frame(self.frames[curr_fr])
            else:
                self.score[curr_fr - 1] = self.score[curr_fr - 2] + 10 + self._get_total_frame(self.frames[curr_fr])
            if not self._is_spare(self.frames[curr_fr]):
                self.score[curr_fr] = self.score[curr_fr - 1] + self._get_total_frame(self.frames[curr_fr])
        elif nb_strike == 0 and not self._is_strike(self.frames[curr_fr]) and self._is_frame_completed(self.frames[curr_fr]):
            if not self._is_spare(self.frames[curr_fr]):
                if curr_fr - 1 >= 0:
                    prev_score = self.score[curr_fr - 1]
                else:
                    prev_score = 0
                self.score[curr_fr] = prev_score + self._get_total_frame(self.frames[curr_fr])

    def calcul_score(self, current_fram):
        """."""
        # bonus = 10
        if current_fram == 0 and not self._is_strike(self.frames[current_fram]) and not self._is_spare(self.frames[current_fram]):
            self.score[current_fram] = self._get_total_frame(self.frames[current_fram])
        elif current_fram == 0 and (self._is_spare(self.frames[current_fram]) or self._is_strike(self.frames[current_fram])):
            pass
        elif current_fram >= 1 and (self._is_spare(self.frames[current_fram]) or self._is_strike(self.frames[current_fram])):
            self.score[self.current_fram] = self.score[current_fram - 1] + self._get_total_frame(self.frames[current_fram])
            # if self._is_strike(self.frames[current_fram - 1]):
            #     self.score[self.current_fram] = self.score[self.current_fram - 1] + bonus + self._get_total_frame(self.frames[current_fram])
            # if not self._is_strike(self.frames[current_fram - 1]):
            #     self.score[self.current_fram] = self.score[self.current_fram - 1] + self._get_total_frame(self.frames[current_fram])

        elif current_fram >= 1 and self._is_strike(self.frames[current_fram - 1]):
            self.score[self.current_fram - 1] = 10
        else:
            self.score[self.current_fram] = self.score[current_fram - 1] + self._get_total_frame(self.frames[current_fram])

    def _is_spare(self, frame):
        """Define if the frame is a spare."""
        return frame[0] != 10 and (frame[0] + frame[1] == 10)

    def _is_strike(self, frame):
        """Define if the frame is a strike."""
        return frame[0] == 10

    def _get_total_frame(self, frame):
        """Give the some of the frame."""
        if frame[0] != 10:
            return frame[0] + frame[1]
        return 10

    def _is_frame_completed(self, frame):
        """Validate if the frame is completed."""
        if frame[0] != 10:
            return frame[0] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and frame[1] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return True
