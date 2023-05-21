def countingsort(sequence, power):

    size = len(sequence)
    occurences = [0]*10  # 10 buckets

    # compute the occurences
    for i in range(size):
        bucket = (sequence[i] // power) % 10
        occurences[bucket] += 1

    # cumulate the occurences
    for i in range(1, 10):
        occurences[i] += occurences[i-1]

    output = [0]*size
    i = size - 1

    # bucket-based sorting for the current power
    while i >= 0:
        # take the last element
        elem = sequence[i] 
        bucket = (sequence[i] // power) % 10
        occurences[bucket] -= 1 
        newPosition = occurences[bucket]
        output[newPosition] = elem  # no-override by construction
        i -= 1

    return output
    

def radixsort(sequence):

    if len(sequence) <= 1:
        return sequence

    # get the max element
    maxElem = max(sequence)
    # count the max number of digits
    digits = 1
    while maxElem > 0:
        maxElem /= 10
        digits += 1

    # perform counting sort for each digit
    power = 1
    output = sequence
    while digits > 0:
        output = countingsort(output, power)
        power *= 10
        digits -= 1

    return output


"""
Time: O(nd) 
Space: O(n + d)
Where d is the number of digits
"""
