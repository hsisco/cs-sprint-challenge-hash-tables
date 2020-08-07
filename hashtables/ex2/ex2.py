#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}                                                  # Create a cache
    route = [None] * length                                     # Create array with None as key value pairs

    for i in range(length):                                     # Iterate through array
        cache[tickets[i].source] = tickets[i].destination       # Add the destinations to hash table 
        if tickets[i].source == "NONE" and route[0] == None:    # If the current ticket index has a source of None ...
            route[0] = tickets[i].destination                   # ... this is the first flight

    # Check the value of the starting location to construct the entire route 
    for ticket in range(length):                            # Iterate through array
        if ticket > 0 and route[ticket - 1] is not None:    # If the ticket isn't the first AND the last index is not None ...
            route[ticket] = cache[route[ticket - 1]]   # ... Set destination to the ticket

    return route