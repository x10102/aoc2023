record = 207139412091014
time = 47847467

recordtimes = 0
for t in range(time+1):
    if (time - t)*t > record:
        recordtimes += 1

print(recordtimes)