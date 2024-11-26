def are_anagrams(chaine1, chaine2):
    chaine1 = chaine1.replace(" ", "").lower()
    chaine2 = chaine2.replace(" ", "").lower()

    return sorted(chaine1) == sorted(chaine2)