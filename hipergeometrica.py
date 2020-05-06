import random


class Hipergeometrica:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def generate_var(self):
        x = 0
        j = 0
        a = self.a
        b = self.b
        n = self.n
        p = a/n
        while 1:
            u = random.random()
            if u < p:
                x = x + 1
                a = a - 1
            n = n - 1
            p = a/n
            j = j + 1
            # daca am terminat extractiile returnez numarul de bile albe extrase si ies din functie
            if j == n:
                return x


val1 = float(input("Numarul de bile albe:  "))
val2 = float(input("Numarul de bile negre:  "))
val3 = float(input("Numar de extrageri:  "))

print()
hipergeom = Hipergeometrica(val1, val2, val3)
print("Numarul de bile albe extrase (variabila hipergeometrica): ")
xg = hipergeom.generate_var()
print((val1/(val1 + val2)) * val3)
print(xg)

sx = 0
for i in range(1000):
    sx = sx + hipergeom.generate_var()

print("Media generarii a 1000 de variabile hipergeometrice: ")
print(sx/1000)

