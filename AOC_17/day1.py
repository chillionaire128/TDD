
def add_sequential(sequence):
    """
    Takes in a sequence and returns the sum of every number that is equal to the next one in the sequence
    """
    result = 0
    length = (len(sequence) - 1)
    for i, num in enumerate(sequence):
        check = i + 1
        if check > length:
            check = 0
        if num == sequence[check]:
            result += num
    return result


def add_halfway(sequence):
    """
    Takes in a sequence and returns the total of numbers that repeat themselfs halfway around the circular list
    """
    result = 0
    length = (len(sequence) - 1)
    for i, num in enumerate(sequence):
        check = i + (len(sequence) / 2)
        if check > length:
            check = (check % len(sequence))
        check = int(check)
        if num == sequence[check]:
            result += num
    return result
