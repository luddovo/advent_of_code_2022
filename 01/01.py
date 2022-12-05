
max_total = 0
total = 0
for line in open("input.txt","r"):
    try:
        total += int(line.strip())
    except ValueError:
        if total > max_total:
            max_total = total
        total = 0
print(max_total)
