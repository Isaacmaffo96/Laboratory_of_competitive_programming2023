import sys

for i, line in enumerate(sys.stdin):
    arr = [int(x) for x in line.split()]
    print("line {}, sum {}".format(i, sum(arr)))
