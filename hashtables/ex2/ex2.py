#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    route = [None] * length

    for thing in tickets:
        cache[thing.source] = thing.destination

    destination = cache['NONE']

    for flying in range(length):
        
        route[flying] = destination

        destination = cache[destination]

    return route
