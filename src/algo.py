from collections import deque
from random import randrange, randint
import visual

#global var
total_volume = 0
area_number = 0
area_volume = []

def output_str():
    s = ''
    s += 'V = '+ str(total_volume) + '\n'
    s += 'n = '+ str(area_number) + '\n'
    for e in reversed(area_volume):
        s += str(e) + '  '
    return s

def auto_input():
    s = ''
    for _ in range(randint(1, 50)):
        if randrange(-10, 10) == 0:
            s += '_'
        elif randrange(-10, 10) < 0:
            s += '\\'
        else:
            s += '/'
    return s

def calc_total_volume(Slopes, Steeps, Checkpoints):
    global total_volume
    while Slopes and Steeps:
        start_point = Slopes.pop()
        end_point = Steeps.popleft()

        Checkpoints.append((start_point, end_point))

        total_volume += (end_point - start_point)

    #clear remaining steeps if no slopes are left
    if not Slopes:
        Steeps.clear()

def calc_area_volume(Checkpoints):
    global area_number
    if not Checkpoints:
        return

    temp_volume = 0
    pos = Checkpoints[-1][0]

    while Checkpoints:
        start_index, end_index = Checkpoints.pop()

        if start_index < pos:
            area_volume.append(temp_volume)
            temp_volume = 0
            area_number += 1
            pos = start_index

        temp_volume += (end_index - start_index)

        if not Checkpoints:
            area_volume.append(temp_volume)
            area_number += 1

def main(s):
    #reset global var before processing
    global total_volume, area_number, area_volume
    total_volume = 0
    area_number = 0
    area_volume = []

    #init containers
    Slopes = []
    Steeps = deque()
    Checkpoints = deque()

    #start processing
    hadSlope = False
    hadSteep = False
    for i in range(len(s)):
        if s[i] == '/':
            if hadSlope:
                Steeps.append(i)
                hadSteep = True

        if s[i] == '\\':
            if hadSteep:
                calc_total_volume(Slopes, Steeps, Checkpoints)
                hadSteep = False
            Slopes.append(i)
            hadSlope = True

        if i + 1 == len(s):
            calc_total_volume(Slopes, Steeps, Checkpoints)

    #calc area volumes
    calc_area_volume(Checkpoints.copy())

    #plot the graph
    return visual.main(s, Checkpoints)

if __name__ == "__algo__":
    main()
