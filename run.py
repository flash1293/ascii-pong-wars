import random
import math
import time

size = 30

def rotate_random(vec):
    angle = random.random() * 2 * math.pi
    return [math.cos(angle) * vec[0] - math.sin(angle) * vec[1], math.sin(angle) * vec[0] + math.cos(angle) * vec[1]]

day_pos = [5, 5]
night_pos = [size - 5, size - 5]
day_vec = rotate_random([random.random() * 2 - 1, random.random() * 2 - 1])
night_vec = rotate_random([random.random() * 2 - 1, random.random() * 2 - 1])
world = [[1 if i < size/2 else 0 for i in range(size)] for j in range(size)]

def paint():
    global world, day_pos, night_pos, day_vec, night_vec
    # clear terminal screen
    print('\033[H\033[J')

    # print border
    print('+' + ' - ' * size + '+')

    for i in range(size):
        print('|', end='')
        for j in range(size):
            if i == round(day_pos[0]) and j == round(day_pos[1]):
                print(' D ', end='')
            elif i == round(night_pos[0]) and j == round(night_pos[1]):
                print(' N ', end='')
            elif world[i][j] == 0:
                print('   ', end='')
            else:
                print(' * ', end='')
        print('|')

    print('+' + ' - ' * size + '+')

def safe_get_tile(x, y):
    global world
    x = round(x)
    y = round(y)
    if x < 0 or x >= size or y < 0 or y >= size:
        return -1
    return world[x][y]

def move():
    global world, day_pos, night_pos, day_vec, night_vec

    # move day and night
    day_pos[0] += day_vec[0]
    day_pos[1] += day_vec[1]
    night_pos[0] += night_vec[0]
    night_pos[1] += night_vec[1]

    # bounce day and night off the walls
    if day_pos[0] < 0 or day_pos[0] > size:
        day_vec[0] = -day_vec[0]
        day_pos[0] = max(0, min(size-1, day_pos[0]))
    if day_pos[1] < 0 or day_pos[1] > size:
        day_vec[1] = -day_vec[1]
        day_pos[1] = max(0, min(size-1, day_pos[1]))
    if night_pos[0] < 0 or night_pos[0] > size:
        night_vec[0] = -night_vec[0]
        night_pos[0] = max(0, min(size-1, night_pos[0]))
    if night_pos[1] < 0 or night_pos[1] > size:
        night_vec[1] = -night_vec[1]
        night_pos[1] = max(0, min(size-1, night_pos[1]))
    
    # bounce day off 0 tile in the world, bounce night off 1 tile in the world and flip the tile
    if safe_get_tile(day_pos[0], day_pos[1]) == 0:
        if random.random() < 0.5:
            day_vec[0] = -day_vec[0]
        else:
            day_vec[1] = -day_vec[1]
        world[round(day_pos[0])][round(day_pos[1])] = 1
    if safe_get_tile(night_pos[0], night_pos[1]) == 1:
        if random.random() < 0.5:
            night_vec[0] = -night_vec[0]
        else:
            night_vec[1] = -night_vec[1]
        
        world[round(night_pos[0])][round(night_pos[1])] = 0


def main(): 
    while True:
        paint()
        move()
        time.sleep(0.06)

if __name__ == '__main__':
    main()