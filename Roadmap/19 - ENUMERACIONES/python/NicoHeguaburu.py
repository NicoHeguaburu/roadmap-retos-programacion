from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDSESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day(number: int):
    print(Weekday(number).name)


get_day(6)


#DIFICULTAD EXTRA

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    CANCELADO = 3
    ENTREGADO = 4


class Order:

    status = OrderStatus.PENDIENTE

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDIENTE:
            self.status = OrderStatus.ENVIADO
            print("se envio el pedido")
        elif self.status == OrderStatus.CANCELADO:
            print("el pedido esta cancelado crea uno nuevo")
        else:
            print("el pedido ya fue enviado")

    def deliver(self):
        if self.status == OrderStatus.ENVIADO:
            self.status = OrderStatus.ENTREGADO
            print("el pedido a sido entregado")
        elif self.status == OrderStatus.CANCELADO:
            print("el pedido esta cancelado crea uno nuevo")
        else:
            print("el pedido no estaba en camino o ya fue entregado")

    def cancel(self):
        self.status = OrderStatus.CANCELADO
        print("el pedido fue cancelado")

    def display_status(self):
        print(f"el estado del pedido es {self.status.name}")




order_1 = Order(1)

order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.display_status()

order_1.cancel()

order_1.display_status()


order_2 = Order(2)
order_2.ship()
order_2.deliver()
order_2.display_status()
order_2.cancel()
order_2.display_status()
