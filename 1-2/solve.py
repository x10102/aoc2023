import regex as re

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

r_calvals = r"(zero|one|two|three|four|five|six|seven|eight|nine|\d{1})"

def getval(string: str) -> int:
    """
    Convert a string to a digit
    """
    
    if string.isnumeric():
        return int(string)
    else:
        return digits[string]

with open('input.txt') as file:
    calvals = list()
    for line in file:
        vals = [getval(m) for m in re.findall(r_calvals, line, overlapped=True)]    # Find all numerical strings using regex and convert to ints
        v1 = vals[0]
        v2 = vals[-1]
        calvals.append(int(f"{v1}{v2}")) # Put the first and last value together
    print(sum(calvals))
