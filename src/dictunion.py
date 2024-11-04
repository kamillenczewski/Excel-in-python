def dict_union(all_keys, keys_and_values, default_item):
    new_keys_and_values = {}

    for key in all_keys:
        if key in keys_and_values:
            new_keys_and_values[key] = keys_and_values[key]
        else:
            new_keys_and_values[key] = default_item

    return new_keys_and_values