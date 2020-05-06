import random
from scipy.stats import gamma


class Beta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def generate_var(self):
        while 1:
            # generez doua variabile aleatoaren in intervalul (0,1)
            u1 = random.random()
            u2 = random.random()
            v = u1 ** (1/self.a)
            t = u2 ** (1/(self.b - 1))
            if v + t < 1:
                return v


beta = Beta(0.75, 4)
print("Media variabilei Beta: ")
# print(0.75/(0.75 + 4))
print(beta.generate_var())

s = 0
for i in range(1000):
    s = s + beta.generate_var()
print("Media generarii a 1000 de variabile Beta: ")
print(s/1000)

print("Beta cu gamma:")
var1 = gamma.rvs(0.75, 1, 1)
var2 = gamma.rvs(4, 1, 1)
print(var1/(var1 + var2))



