def get_indices_of_item_weights(weights, length, limit):
    cache = {}                              # Create a cache

    for i in range(length):                 # Iterate through array
        difference = limit - weights[i]     # Find the weight limit
        if difference in cache:             # Check if a key with the difference exists
            return (i, cache[difference])   # If YES return the matching items in a tuple
        else:
            cache[weights[i]] = i           # If NO add it to cache, with value of index

    return None                             # If it doesn't exist return None