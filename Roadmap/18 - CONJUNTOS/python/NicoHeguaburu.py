data = [1, 2, 3, 4, 5]
data.append(6)#elemento al final
data.insert(0, 0)#elemento al inicio
data.extend([7, 8, 9])
data[5:5] = [5000, 5001]
del data[6]
data[5] = 7060
if 7060 in data:
    print("se encuentra el elemento")
data = []



#ejercicio extra

conjunto_a = [1,2,3,4,5,6]
conjunto_b = [5,6,7,8,9,10]


def union (conjunto_x: list, conjunto_y: list) -> list:
    conjunto_resultado = conjunto_x.copy()
    for elemento in conjunto_y:
        if elemento not in conjunto_resultado:
            conjunto_resultado.append(elemento)
    return conjunto_resultado




def interseccion(conjunto_x: list, conjunto_y: list) -> list:
    conjunto_resultado = []
    for elemento in conjunto_x:
        if elemento in conjunto_y:
            conjunto_resultado.append(elemento)
    return conjunto_resultado


def diferencia(conjunto_x: list, conjunto_y: list) -> list:
    conjunto_resultado = []
    for elemento in conjunto_x:
        if elemento not in conjunto_y:
            conjunto_resultado.append(elemento)
    return conjunto_resultado




def diferencia_simetrica(conjunto_x: list, conjunto_y: list) -> list:
    conjunto_union = union(conjunto_x, conjunto_y)
    conjunto_interesccion = interseccion(conjunto_x, conjunto_y)
    conjunto_resultado = [elemento for elemento in conjunto_union if elemento not in conjunto_interesccion]
    return conjunto_resultado


print(union(conjunto_a, conjunto_b))
print(union(conjunto_b, conjunto_a))

print(interseccion(conjunto_a, conjunto_b))
print(interseccion(conjunto_b, conjunto_a))

print(diferencia(conjunto_a, conjunto_b))
print(diferencia(conjunto_b, conjunto_a))

print(diferencia_simetrica(conjunto_a, conjunto_b))
print(diferencia_simetrica(conjunto_b, conjunto_a))
