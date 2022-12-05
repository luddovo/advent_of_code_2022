
total = 0
totals = []
for line in open("input.txt","r"):
    try:
        total += int(line.strip())
    except ValueError:
        totals.append(total)
        total = 0
totals.sort()
print(sum(totals[-3:]))
