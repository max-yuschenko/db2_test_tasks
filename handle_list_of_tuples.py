def handle_list_of_tuples(list):
    return sorted(list, key=lambda x: (x[0], x[1], x[2], x[3]))
