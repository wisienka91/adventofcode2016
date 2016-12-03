# -*- coding: utf-8 -*-


class CodeCracker(object):

    def __init__(self):
        self.code = ''
        self.simple_keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.enhanced_keypad = [
            [None, None, 1, None, None],
            [None, 2, 3, 4, None],
            [5, 6, 7, 8, 9],
            [None, 'A', 'B', 'C', None],
            [None, None, 'D', None, None]
        ]

    def get_next_index(self, turn, keypad):
        keypad_length = len(keypad)
        if turn == 'U' and self.index[0] > 0 and keypad[
            self.index[0] - 1][self.index[1]] is not None:
            self.index = [self.index[0] - 1, self.index[1]]
        elif turn == 'R' and self.index[1] < keypad_length - 1 and keypad[
            self.index[0]][self.index[1] + 1] is not None:
            self.index = [self.index[0], self.index[1] + 1]
        if turn == 'D' and self.index[0] < keypad_length - 1 and keypad[
            self.index[0] + 1][self.index[1]] is not None:
            self.index = [self.index[0] + 1, self.index[1]]
        elif turn == 'L' and self.index[1] > 0 and keypad[
            self.index[0]][self.index[1] - 1] is not None:
            self.index = [self.index[0], self.index[1] - 1]

    def get_a_number(self, turns, pad='simple'):
        if pad == 'simple':
            keypad = self.simple_keypad
        elif pad == 'enhanced':
            keypad = self.enhanced_keypad
        for turn in turns:
            self.get_next_index(turn, keypad)
        return str(keypad[self.index[0]][self.index[1]])

    def crack_the_keypad(self, input_data):
        self.index = [1, 1]
        for line in input_data:
            turns = line.rstrip()
            self.code += self.get_a_number(turns)
        print('The code is: {0}'.format(self.code))

    def crack_the_enhanced_keypad(self, input_data):
        self.index = [2, 0]
        for line in input_data:
            turns = line.rstrip()
            self.code += self.get_a_number(turns, pad='enhanced')
        print('The code is: {0}'.format(self.code))



if __name__ == '__main__':
    input_file = open('day02.txt', 'r')
    input_data = input_file.readlines()
    CodeCracker().crack_the_keypad(input_data)
    CodeCracker().crack_the_enhanced_keypad(input_data)

