def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    result = []

    for thing in a:
        if thing != 0: #dont want to include 0
            cache[thing] = 1 #adding the number to the cache

            if -thing in cache: #if the number has both
                result.append(abs(thing)) #add the number to result []
                #The abs() takes only one argument, a number whose absolute value is to be returned.
                #The append() method adds a single item to the end of the list.

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
