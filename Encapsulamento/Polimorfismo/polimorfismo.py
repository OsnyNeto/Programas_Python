print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6]))
print(len((1, 2, 3, 4, 5, 6)))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))
print(len(range(0, 10)))
#print(len(100))  # TypeError

class Passaro:
    def voar(self):
        print('Passaro está voando')

class Pardal(Passaro):
    def voar(self):
       super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)