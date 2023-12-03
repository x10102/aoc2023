def get_power(game: str) -> bool:
    gamedata = game.strip()
    rounds = [r.strip() for r in gamedata.split(';')]
    min_r = min_g = min_b = 0
    for r in rounds:
        colors = r.split(', ')
        for c in colors:
            match c.split(' '):
                case [n, 'red']:
                    if int(n) > min_r:
                        min_r = int(n)
                case [n, 'green']:
                    if int(n) > min_g:
                        min_g = int(n)
                case [n, 'blue']:
                    if int(n) > min_b:
                        min_b = int(n) 
    return min_r * min_g * min_b

with open('input.txt') as infile:
    _sum = 0
    for line in infile:
        gameidstr, gamedata = line.split(':')
        gameid = int(gameidstr.split(' ')[-1])
        _sum += get_power(gamedata)
    print(_sum)