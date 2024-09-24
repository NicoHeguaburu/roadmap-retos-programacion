import re

def find_numbers(text: str) -> list:
    return re.findall(r"\D+", text)


print (find_numbers("este es el ejercicio 16  1313  99123"))


#EXTRA

def validar_email(email: str) -> bool:
    exprecion_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(exprecion_email, email))

print(validar_email("nicoheguaburu02@gmail.com"))
print(validar_email("nico,heguaburu02@gmail.com"))


def validar_telef(telef: str) -> bool:
    exprecion_telef = r"^[0-9]{8,8}+$"
    return bool(re.match(exprecion_telef, telef)) 

print(validar_telef(str(98769876)))
print(validar_telef(str(987698762313)))


def validar_url(url: str) -> bool:
    exprecion_url = r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$"
    return bool(re.match(exprecion_url, url))

print(validar_url("https://www.youtube.com"))
print(validar_url("https://wwww.youtube.com"))
