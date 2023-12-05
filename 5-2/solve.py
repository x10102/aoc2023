from dataclasses import dataclass

@dataclass
class rangemap():
    fromrange_start: int
    fromrange_end: int
    fromrange: range
    torange_start: int
    torange_end: int
    torange: range

maptree = {}
"""
{
    "soil": {
        "from": "seed",
        "ranges": [
            [rangemap1]...
            [rangemapX]
        ]
    }
}
"""

def is_range_overlapping(start1, start2, length):
    first, last = min(start1, start2), max(start1, start2)
    return first+length >= last

def find_starting_range(rng):
    def sorted_ranges(r):
        return sorted(r, key=lambda a: a.torange_start)
    rindex = 0
    while True:
        current_start, current_end = sorted_ranges[rindex].fromrange_start, sorted_ranges[rindex].fromrange_end
        

def parse_seeds(inp):
    print('Begin parse seeds')
    nums = [int(i) for i in inp.split(':')[-1].strip().split(' ')]
    print(nums)
    pairs = list(zip(nums[::2], nums[1::2])) # Take the pairs
    print(pairs)
    for start, length in pairs:
        for s in range(start, start+length):
            yield s

def map_to_range(inp: int, type: str):
    for r in maptree[type]['ranges']:
        if inp in r.fromrange:
            r.lowest_tried = inp
            return r.torange_start + (inp-r.fromrange_start)
    return inp

def parse_ranges(inp):
    print(f'Begin parse ranges')
    current_src = ''
    current_dest = ''
    for line in inp:
        match line.split(' '):
            case [mtype, "map:"]:
                current_src, _, current_dest = mtype.split('-')
                maptree[current_dest] = {
                    'from': current_src,
                    'ranges': []
                }
            case [torange, fromrange, lrange]:
                fr, tr, lr = int(fromrange), int(torange), int(lrange)
                maptree[current_dest]['ranges'].append(
                    rangemap(fr, fr+lr-1, range(fr, fr+lr), tr, tr+lr-1, range(tr,tr+lr), 999999999999))
    print('End parse ranges')


lowlocation = 99999999999999999999999999999999
iteration = 0
with open('input.txt') as infile:
    lines = [l.strip() for l in infile.readlines()]
    parse_ranges(lines[1:])
    find_starting_range()
    exit()
    for seed in parse_seeds(lines[0]):
        iteration += 1
        last = seed
        soil = map_to_range(seed, 'soil')
        fert = map_to_range(soil, 'fertilizer')
        water = map_to_range(fert, 'water')
        light = map_to_range(water, 'light')
        temp = map_to_range(light, 'temperature')
        hum = map_to_range(temp, 'humidity')
        loc = map_to_range(hum, 'location')
        if loc < lowlocation:
            lowlocation = loc
        if iteration % 10000 == 0:
            print(f'Iteration {iteration}; Lowest: {lowlocation}')
        
print(lowlocation)
