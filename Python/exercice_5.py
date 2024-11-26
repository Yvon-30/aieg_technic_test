def custom_sort(strings) :
    return sorted(strings, key=lambda x: (len(x), x))