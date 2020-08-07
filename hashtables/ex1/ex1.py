def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}                             # Create a dictionary

    for i in range(length):                     # Iterate through the array
        difference = limit - weights[i]         # Find the weight limit
        if difference in hash_table:            # Check if a key with the difference exists
            return (i, hash_table[difference])  # If YES return the matching items in a tuple
        else:
            hash_table[weights[i]] = i          # If NO add it to hash table, with value of index

    return None                                 # If it doesn't exist return None