import numpy as np


def son_combinacion_lineal(vectores):
    matriz = np.array(vectores)
    rango = np.linalg.matrix_rank(matriz)
    return rango < len(vectores)


vectores = []
for i in range(4):
    vector = input(f'Introduce las coordenadas del vector {i+1} separadas por comas: ')
    vector = [float(x) for x in vector.split(',')]
    vectores.append(vector)


if son_combinacion_lineal(vectores):
    print("Los vectores pueden expresarse como una combinación lineal.")
else:
    print("Los vectores no pueden expresarse como una combinación lineal.")