from dataclasses import dataclass
from tracemalloc import start

lines = list()
parts = list()
gears = list()

@dataclass
class PartNo:
    startx: int
    endx: int
    y: int
    value: int

@dataclass
class Gear:
    x: int
    y: int

def check_for_sym(startx, endx, y):
    # Get start and end indices for the surrounding rectangle
    if y == 0:
        yrange = range(y, y+2)
    if y == len(lines) - 1:
        yrange = range(y-1, y+1)
    else:
        yrange = range(y-1, y+2)
    if endx == 139: # Lines are 140 chars long
        xrange = range(startx-1, endx+1)
    elif startx == 0:
        xrange = range(startx, endx+2)
    else:
        xrange = range(startx-1, endx+2)
    for y in yrange:
        for x in xrange:
            if not lines[y][x].isnumeric() and lines[y][x] != '.':  # Check for a symbol
                return True
    return False
    

with open('input.txt') as inputfile:
    lines = [l.strip() for l in inputfile.readlines()]

_sum = 0
for lidx, l in enumerate(lines):
    current_n = ''
    startx = 0
    endx = 0
    for idx, c in enumerate(l):
        if c == '.':    # Skip
            continue
        elif c.isnumeric(): # Start processing the number
            if not current_n:   # Not currently parsing a number
                startx = idx
            current_n += c  # Append the current digit
            if idx == 139 or not l[idx+1].isnumeric():  # Check if another digit follows or if we're at EOL
                endx = idx
                if check_for_sym(startx, endx, lidx):  # Check near the bounds of the number for a symbol
                    _sum += int(current_n)
                    parts.append(PartNo(startx, endx, lidx, current_n)) # Add it to the part list
                current_n = ''
        elif c == '*':
            gears.append(Gear(idx, lidx))   # Add it to the gear list

_ratiosum = 0
for g in gears:
    matchingparts = []
    for p in parts:
        # Skip if we're not within +-1 on the y axis
        if not g.y-2 < p.y < g.y+2:
            continue
        if g.x-len(str(p.value))-1 < p.startx < g.x+2:  # Check if we're close enough on the x axis, taking into account the length of the number
            matchingparts.append(p)
    if len(matchingparts) == 2:
        _ratiosum += int(matchingparts[0].value) * int(matchingparts[1].value)  # Calculate the "ratio" and add to the solution

print(_ratiosum)