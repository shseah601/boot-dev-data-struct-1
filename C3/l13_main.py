def count_names(list_of_lists, target_name):
    total_count = 0
    for names in list_of_lists:
        for name in names:
            if name == target_name:
                total_count += 1
    return total_count

