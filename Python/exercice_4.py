def find_missing_number(nbr):
    n = len(nbr) + 1
    total_nbr = sum(range(min(nbr), max(nbr) + 1))
    return total_nbr - sum(nbr)
