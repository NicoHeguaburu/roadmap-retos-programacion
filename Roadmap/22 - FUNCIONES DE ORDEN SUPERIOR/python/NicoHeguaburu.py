from datetime import datetime 

def apply_func(func, x):
    return func(x)
x = apply_func(len, "nicolachooo")
print(x)



def apply_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
multi = apply_multiplier(2)
print(multi(9))

# otras funciones de orden superior son map() filter() sorted() reduce()


#Ejercicio extra

estudiantes = [
    {"Nombre": "Nicolás", "Nacimiento": "12-07-2002", "Calificaciones": {"Matematicas": 8, "Fisica": 12, "Quimica": 9}},
    {"Nombre": "Pedro", "Nacimiento": "08-04-2002", "Calificaciones": {"Matematicas": 3, "Fisica": 6, "Quimica": 4}},
    {"Nombre": "Marcos", "Nacimiento": "02-12-2002", "Calificaciones": {"Matematicas": 11, "Fisica": 4, "Quimica": 5}},
    {"Nombre": "Maxi", "Nacimiento": "09-12-2002", "Calificaciones": {"Matematicas": 6, "Fisica": 10, "Quimica": 8}},
    {"Nombre": "Lucia", "Nacimiento": "27-07-2002", "Calificaciones": {"Matematicas": 5, "Fisica": 3, "Quimica": 12}},
    {"Nombre": "Fernando", "Nacimiento": "28-10-2002", "Calificaciones": {"Matematicas": 8, "Fisica": 5, "Quimica": 2}},
    {"Nombre": "Julieta", "Nacimiento": "20-01-2002", "Calificaciones": {"Matematicas": 8, "Fisica": 7, "Quimica": 7}}
]

def caluclar_promedios():
    for alumno in estudiantes:
        calificaciones = list(map(int, alumno["Calificaciones"].values()))
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio del alumno {alumno["Nombre"]} es de {promedio}")
    
caluclar_promedios()

def mejores_estudiantes():
    mejores = list(filter(lambda alumno: (sum(alumno["Calificaciones"].values()) / len(alumno["Calificaciones"])) >= 8, estudiantes))   
    for alumno in mejores:
        print(f"{alumno["Nombre"]} integra la lista de mejor de la clase con promedio de {sum(alumno["Calificaciones"].values()) / len(alumno["Calificaciones"])}")

mejores_estudiantes()

def ordenar_estudiantes_edad():
    estudiantes_ordenados = sorted(estudiantes, key=lambda alumno: datetime.strptime(alumno["Nacimiento"], "%d-%m-%Y"))
    for alumno in estudiantes_ordenados:
        print(f"{alumno['Nombre']} - {alumno['Nacimiento']}")

ordenar_estudiantes_edad()

def mejor_estudiante_materia():
    matematicas = []
    fisica = []
    quimica = []

    for alumno in estudiantes:
        matematicas.append({alumno["Nombre"]: alumno["Calificaciones"]["Matematicas"]})
        fisica.append({alumno["Nombre"]: alumno["Calificaciones"]["Fisica"]})
        quimica.append({alumno["Nombre"]: alumno["Calificaciones"]["Quimica"]})


    mejor_matematicas = max(matematicas, key=lambda x: list(x.values())[0])

    mejor_fisica = max(fisica, key=lambda x: list(x.values())[0])

    mejor_quimica = max(quimica, key=lambda x: list(x.values())[0])

    print(f"Mejor estuidante en Matematicas: {mejor_matematicas}")
    print(f"Mejor estuidante en Fisica: {mejor_fisica}")
    print(f"Mejor estuidante en Quimica: {mejor_quimica}")


mejor_estudiante_materia()