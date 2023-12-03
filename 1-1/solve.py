with open('input.txt') as file:
    calvals = list()
    for line in file:
        nums = list(filter(str.isnumeric, line))    # Filter out all non-numeric chars
        calvals.append(int(f"{nums[0]}{nums[-1]}")) # Put the first and last digit together
    print(sum(calvals))