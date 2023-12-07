records = []
times = []

def load_input():
    global records, times
    with open('input.txt') as infile:
        lines = infile.readlines()
        times = [int(a) for a in lines[0].split(' ')[1:] if a]
        records = [int(a) for a in lines[1].split(' ')[1:] if a]

recordtimes = [0] * 4
load_input()
for idx, time in enumerate(times):
    for t in range(time+1):
        if (time - t)*t > records[idx]:
            recordtimes[idx] += 1
total = recordtimes[0]
for a in recordtimes[1:]:
    total *= a
print(total)