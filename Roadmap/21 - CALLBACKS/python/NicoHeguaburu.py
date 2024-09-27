import random
import time
import threading


def mi_callback():
    print("soy el callback")

def ejecutar_funcion_callback(funcion):
    print("antes de ejecutar el callback...")
    funcion()
    print("despues del callback...")

ejecutar_funcion_callback(mi_callback)

#Ejercicio Extra

def order_process(dish_name: str , callback_confirm, callback_ready ,callback_delivered):
    def process():
        callback_confirm(dish_name)
        time.sleep(random.randint(1,30))
        callback_ready(dish_name)
        time.sleep(random.randint(1,30))
        callback_delivered(dish_name)

    threading.Thread(target=process).start()    

def order_confirm(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado.")

def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} esta listo.")

def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")

order_process("barbacoa", order_confirm, order_ready, order_delivered)
order_process("salami", order_confirm, order_ready, order_delivered)
order_process("4 chease", order_confirm, order_ready, order_delivered)
