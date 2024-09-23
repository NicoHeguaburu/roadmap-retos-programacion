from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


fecha_a = datetime.now()
fecha_b = datetime(2002, 7, 12, 0, 0)

def calc_edad(fecha_actual, fecha_nacimiento):
    edad = fecha_actual - fecha_nacimiento
    print(f"tu edad es de {edad.days // 365}")

calc_edad(fecha_a, fecha_b)



print(f"usted nacio en el año {fecha_b.year}, en el mes {fecha_b.month} dia {fecha_b.day}")

print(f"usted nacio un dia {fecha_b.strftime("%A")}")

print(f"usted nacio el dia {fecha_b.strftime("%j")} del año {fecha_b.year}")

print(f"usted nacio en el mes de {fecha_b.strftime("%B")}")

print(f"le faltan {(365 - int(fecha_a.strftime("%j"))) + (int(fecha_b.strftime("%j")))} dias para que cumpla años")

