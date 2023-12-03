def is_valid_game(game: str) -> bool:
    gamedata = game.strip() # Strip leading whitespace
    rounds = [r.strip() for r in gamedata.split(';')]   # Games separated by a semicolon
    for r in rounds:
        colors = r.split(', ')
        for c in colors:
            match c.split(' '): # Extract the color and value
                case [n, 'red']:
                    if int(n) > 12:
                        return False
                case [n, 'green']:
                    if int(n) > 13:
                        return False
                case [n, 'blue']:
                    if int(n) > 14:
                        return False 
    return True

with open('input.txt') as infile:
    _sum = 0
    for line in infile:
        gameidstr, gamedata = line.split(':')   # Split the game ID from the game description
        gameid = int(gameidstr.split(' ')[-1])  # Get the actual ID number
        if(is_valid_game(gamedata)):
            _sum += gameid
    print(_sum)