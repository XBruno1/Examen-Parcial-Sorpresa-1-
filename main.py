import math

# Crear los puntos A, B, C y D

A = (2, 3)
B = (5, 5)
C = (-3, -1)
D = (0, 0)

# Imprimir los puntos

print("Punto A:", A)
print("Punto B:", B)
print("Punto C:", C)
print("Punto D:", D)

# Función para determinar el cuadrante de un punto

def determinar_cuadrante(punto):
    x, y = punto
    if x > 0 and y > 0:
        return "Primer cuadrante"
    elif x < 0 and y > 0:
        return "Segundo cuadrante"
    elif x < 0 and y < 0:
        return "Tercer cuadrante"
    elif x > 0 and y < 0:
        return "Cuarto cuadrante"
    else:
        return "Sobre un eje o el origen"

# Consultar a qué cuadrante pertenecen los puntos A, C y D

print("Cuadrante de A:", determinar_cuadrante(A))
print("Cuadrante de C:", determinar_cuadrante(C))
print("Cuadrante de D:", determinar_cuadrante(D))

# Función para calcular el vector entre dos puntos

def calcular_vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

# Consultar los vectores AB y BA

vector_AB = calcular_vector(A, B)
vector_BA = calcular_vector(B, A)
print("Vector AB:", vector_AB)
print("Vector BA:", vector_BA)

# (Optativo) Función para calcular la distancia entre dos puntos

def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Consultar la distancia entre los puntos A y B, y B y A

distancia_AB = calcular_distancia(A, B)
distancia_BA = calcular_distancia(B, A)
formula_distancia = "√((x2 - x1)^2 + (y2 - y1)^2)"
print("Fórmula de la distancia:", formula_distancia)
print("Distancia entre A y B:", distancia_AB)
print("Distancia entre B y A:", distancia_BA)

# (Optativo) Determinar cuál de los puntos A, B o C está más lejos del origen

distancia_A_origen = calcular_distancia(A, D)
distancia_B_origen = calcular_distancia(B, D)
distancia_C_origen = calcular_distancia(C, D)

punto_mas_lejos = max(
    (distancia_A_origen, "A"),
    (distancia_B_origen, "B"),
    (distancia_C_origen, "C"),
    key=lambda x: x[0]
)
print(f"El punto más lejos del origen es {punto_mas_lejos[1]} con una distancia de {punto_mas_lejos[0]}")

# Crear un rectángulo utilizando los puntos A y B

base = abs(B[0] - A[0])
altura = abs(B[1] - A[1])
area = base * altura

# Consultar la base, altura y área del rectángulo

print("Base del rectángulo:", base)
print("Altura del rectángulo:", altura)
print("Área del rectángulo:", area)
