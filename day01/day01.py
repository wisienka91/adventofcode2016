# -*- coding: utf-8 -*-


class BunnyHQFinder(object):

    def __init__(self):
        self.directions = ['N', 'E', 'S', 'W']
        self.previous_turn = self.directions[0]
        self.blocks = [0, 0]
        self.visited = set()
        self.found_twice = False

    def get_next_direction(self, turn):
        direction = ''
        compass_rose = self.directions.index(self.previous_turn)
        if turn == 'R':
            direction = self.directions[
                (compass_rose + 1) % len(self.directions)]
        else:
            direction = self.directions[
                (compass_rose - 1) % len(self.directions)]
        self.previous_turn = direction
        return direction

    def move(self, direction, distance):
        if direction == 'N':
            self.blocks[1] += distance
        elif direction == 'E':
            self.blocks[0] += distance
        elif direction == 'S':
            self.blocks[1] -= distance
        elif direction == 'W':
            self.blocks[0] -= distance

    def move_around(self, move):
        turn, distance = move[0], int(move[1:])
        new_direction = self.get_next_direction(turn)
        self.move(new_direction, distance)

    def move_around_with_caution(self, move):
        turn, distance = move[0], int(move[1:])
        new_direction = self.get_next_direction(turn)
        for i in range(distance):
            self.move(new_direction, 1)
            crossing = (self.blocks[0], self.blocks[1])
            if crossing in self.visited:
                self.found_twice = True
                break
            else:
                self.visited.add(crossing)

    def find_headquarters(self, input_data):
        for move in input_data:
            self.move_around(move)
        result = abs(self.blocks[0]) + abs(self.blocks[1])
        print('Easter Bunny Headquarters was {0} blocks away '\
              'around {1} block...'.format(result, self.blocks))

    def find_headquarters_twice(self, input_data):
        for move in input_data:
            self.move_around_with_caution(move)
            if self.found_twice:
                break
        result = abs(self.blocks[0]) + abs(self.blocks[1])
        print('Easter Bunny Headquarters is {0} blocks away '\
              'around {1} block...'.format(result, self.blocks))


if __name__ == '__main__':
    input_file = open('day01.txt', 'r')
    input_data = input_file.readline().strip('\n').split(', ')
    BunnyHQFinder().find_headquarters(input_data)
    BunnyHQFinder().find_headquarters_twice(input_data)

