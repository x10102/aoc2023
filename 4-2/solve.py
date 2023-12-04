from functools import lru_cache

cards = []

@lru_cache(maxsize=512) # Cache the result to cut down the runtime from about a billion years to a few seconds
def process_card(card: str) -> int:
    linename, linedata = card.split(':')
    lineidx = int(linename.split(' ')[-1]) # Get the line index number
    winning = [int(i) for i in linedata.split('|')[0].strip().replace('  ', ' ').split(' ')] # Get first part of data, strip and normalize whitespace, extract ints
    got = [int(i) for i in linedata.split('|')[1].strip().replace('  ', ' ').split(' ')] # Same for the numbers we got
    matchcount = sum([got.count(x) for x in winning]) # Count the matches between the two lists
    if matchcount == 0:
        return []
    elif matchcount == 1:
        return [cards[lineidx]]
    elif matchcount > 1:
        return cards[lineidx:min(lineidx+matchcount, 218)]

with open('input') as infile:
    cards = infile.readlines()

for c in cards:
    cards.extend(process_card(c))

print(len(cards))