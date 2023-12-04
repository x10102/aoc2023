totalpoints = 0
with open('input') as infile:
    for line in infile:
        linename, linedata = line.split(':')
        lineidx = int(linename.split(' ')[-1]) # Get the line index number
        winning = [int(i) for i in linedata.split('|')[0].strip().replace('  ', ' ').split(' ')] # Get first part of data, strip and normalize whitespace, extract ints
        got = [int(i) for i in linedata.split('|')[1].strip().replace('  ', ' ').split(' ')] # Same for the numbers we got
        matchcount = sum([got.count(x) for x in winning]) # Count the matches between the two lists
        if matchcount == 0:
            continue
        elif matchcount == 1:
            totalpoints += 1
        elif matchcount > 1:
            totalpoints += 2**(matchcount-1) # Multiply by two for each match after 1
print(totalpoints)