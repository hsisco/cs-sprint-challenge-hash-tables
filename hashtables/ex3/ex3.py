def intersection(arrays):
    cache = {}                      # Create a cache
    result = []                     # Create the array of results

    for i in arrays:
        for num in i:               # Iterate through array of arrays ...
            if num not in cache:    # .. checking for num against cache
                cache[num] = 1
            else:
                cache[num] +=1    

    # If num has occurred in every array ...
    occurrance = [num for num in cache.keys() if cache[num] == len(arrays)]
    result = result + occurrance    # .. add it to result

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
