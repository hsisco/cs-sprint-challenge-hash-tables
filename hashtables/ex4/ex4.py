def has_negatives(a):
    cache = {}          # Create a cache
    result = []         # Create the array of results

    for num in a:       # Add all positive numbers to the hash table
        if num >= 0:
            cache[num] = num 

    for num in a:       # Check if the positive number in the hash table has a negative value
        if num < 0 and -num in cache:
            result.append(-num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
