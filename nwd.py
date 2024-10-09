def NWD(a, b):
    while a != b:
        if a > b:
            a -=b
        else:
            b -= a
    return a

isValid = False
while not isValid:  
    try:
        a, b = map(int, input("Podaj a i b: ").split())
        if a <= 0 or b <= 0:
            print("Liczby muszą być większe od zera. Spróbuj ponownie.")
            continue
        isValid = True
    except ValueError:
        print("Nieprawidłowe dane wejściowe. Spróbuj ponownie.")

print(f"NWD({a}, {b}) = {NWD(a, b)}")

# **************************************************************************
# nazwa funkcji:      NWD
# opis funkcji:       Zwraca największy wspólny dzielnik dwóch podanych liczb naturalnych większych of zera
# parametry:
