import sys

for i, line in enumerate(sys.stdin):
    arr = [int(x) for x in line.split()]
    sys.stdout.write(str(i) + " ")
    sys.stdout.write(str(sum(arr)) + "\n")
