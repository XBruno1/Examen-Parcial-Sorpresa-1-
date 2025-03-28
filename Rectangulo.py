import math

class Rectangulo:
    def _init_(self, punto_inicial=(0, 0), punto_final=(0, 0)):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):

        # La base es la diferencia en el eje x entre los dos puntos
        
        return abs(self.punto_final[0] - self.punto_inicial[0])

    def altura(self):

        # La altura es la diferencia en el eje y entre los dos puntos

        return abs(self.punto_final[1] - self.punto_inicial[1])

    def area(self):

        # El área es base * altura

        return self.base() * self.altura()

# Ejemplo de uso
rectangulo = Rectangulo((1, 2), (4, 6))
print("Base:", rectangulo.base())
print("Altura:", rectangulo.altura())
print("Área:", rectangulo.area())