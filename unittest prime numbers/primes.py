import math


def ifPrime(x):
    if type(x) != int or x < 2: return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

# **********************************************
# nazwa funkcji:  ifPrime
# argumenty:      x - liczba całkowita
# typ zwracany:   bool, True lub False
# informacje:     sprawdzenie, czy liczba całkowita x jest liczbą pierwszą
# autor:          Maksim Fedoseev, Yevhenii 
# **********************************************