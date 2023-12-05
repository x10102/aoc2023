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
seeds = {}

def parse_seeds(inp):
   for s in inp.split(':')[-1].strip().split(' '):
        seeds[int(s)] = {
            'seed': int(s),
            'soil': 0,
            'fertilizer': 0,
            'water': 0,
            'light': 0,
            'temperature': 0,
            'humidity': 0,
            'location': 0
        }

def map_to_range(inp: int, type: str):
    for r in maptree[type]['ranges']:
        if inp in r.fromrange:
            return r.torange_start + (inp-r.fromrange_start)
    return inp

def parse_ranges(inp):
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
                    rangemap(fr, fr+lr-1, range(fr, fr+lr), tr, tr+lr-1, range(tr,tr+lr)))

with open('input.txt') as infile:
    lines = [l.strip() for l in infile.readlines()]
    parse_seeds(lines[0])
    parse_ranges(lines[1:])
    for seed in seeds.keys():
        last = seed
        for dest, tree in maptree.items():
            seeds[seed][dest] = last = map_to_range(last, dest)
print(min([s['location'] for s in seeds.values()]))