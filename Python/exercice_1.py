def sum_of_digits(n) :
    if n < 0:
        raise ValueError("n doit être positif")
    return sum(int(chiffre) for chiffre in str(n))