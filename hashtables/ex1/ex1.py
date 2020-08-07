def get_indices_of_item_weights(weights, length, limit):
    num_indices = {}
    for (i, wt) in enumerate(weights):
        complement = limit - wt
        if complement in num_indices:
            complement_i = num_indices[complement]
            return (i, complement_i)
        else:
            num_indices[wt] = i

    return None