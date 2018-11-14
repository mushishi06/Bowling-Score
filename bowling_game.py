# -*- coding: utf-8 -*- #

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
        self.current_fram = 0

    def scoresheet(self):
        """Print the scoreSheet."""
        print(self.player)
        sep = "___________________________________________"
        print(sep)
        print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10  |")
        pins = "|"
        for frame in self.frames:
            if not frame[0]:
                frame_one = ' '
            elif frame[0] == 0:
                frame_one = '-'
            elif frame[0] == 10:
                frame_one = 'X'
            else:
                frame_one = frame[0]
            if not frame[1]:
                frame_two = ' '
            elif frame[1] == 0:
                frame_two = '-'
            elif frame[1] == 10:
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
                    pins += str(frame[2]) + "|"
        print(pins)
        print("|   |   |   |   |   |   |   |   |   |     |")
        print(self.score)
        print(sep)

    def roll(self, pins):
        """Emulate the Ball launch."""
        print("debug: pins = ", pins)
        self.rolls.append(pins)
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
            # self.calcul_score(self.current_fram)
            self.current_fram += 1

    def ranroll(self):
        limit_max = 10 - (self.frames[self.current_fram][0]) if self.current_roll % 2 else 10
        self.roll(random.randint(0, limit_max))

    def calcul_strike(self, curr_fr=0, nb_strike=0):

        print("debug: curr_fr ", curr_fr)
        if curr_fr > 0 and self._is_strike(self.frames[curr_fr - 1]) and not self.score[curr_fr - 1]:
            nb_strike = self.calcul_strike(curr_fr - 1, nb_strike + 1)
        else:
            return nb_strike
        print("debug: nb_strike = ", nb_strike)
        if nb_strike == 2:
            print("debug: enternb 2 - ", curr_fr, nb_strike)
            self.score[curr_fr - 1] = int(self.score[self.current_fram - nb_strike]) + 30 if (self.score[self.current_fram - nb_strike]) != '' else 30
        elif nb_strike == 1:
            print("debug: enternb 1 - ", curr_fr, nb_strike)
        elif nb_strike == 0:
            print("debug: enternb 0 - ", curr_fr, nb_strike)

    def calcul_score(self, current_fram):
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
        return (frame[0] != 10 and frame[0] + frame[1] == 10)

    def _is_strike(self, frame):
        return frame[0] == 10

    def _get_total_frame(self, frame):
        return frame[0] + frame[1]
