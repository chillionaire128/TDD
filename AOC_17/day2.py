def get_input():
    path = 'inputs/day2.txt'
    input = []
    with open(path, 'r') as file:
        for line in file:
            row = line.split('\t')
            row[-1] = row[-1].replace('\n', '')
            input.append([int(num) for num in row])
    return input


def row_checksum(row):
    """
    Finds the diffrence between the largest and smallest numbers on a row
    """
    largest = row[0]
    smallest = row[0]
    for num in row:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest - smallest


def grid_checksum(grid):
    """
    Applies row_checksum to a grid and returns the total
    """
    result = 0
    for row in grid:
        result += row_checksum(row)
    return result


def find_even_divis(row):
    """
    :param row: Row of numbers, of witch only two are evenly divisible
    :return: The result of division of the only two evenly divisible numbers in the row
    """
    for a in row:
        for b in row:
            if a is not b and a % b == 0:
                first, second = a, b
                break
    return first / second


def total_even_divis(grid):
    """
    Returns even the total of find_even_divis applied on every row of a grid
    """
    result = 0
    for row in grid:
        result += find_even_divis(row)
    return result
