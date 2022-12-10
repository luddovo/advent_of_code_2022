
# version a normal human would write

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

# version a crazy human would write


print(max([sum(int(x) for x in l.split()) for l in ''.join(open('input.txt')).split('\n\n')[:-1]]))

