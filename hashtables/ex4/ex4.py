def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    result = []

    for thing in a:
        if thing != 0:
            cache[thing] = 1

            if -thing in cache:
                result.append(abs(thing))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
