import time
import asyncio

# async def imprimirNombre(Nombre, duracion):
#     print(Nombre)
#     time.sleep(duracion)
#     print(Nombre)


# asyncio.run (imprimirNombre("Nicolás", 5))
# asyncio.run (imprimirNombre("pepe", 2))



async def funcion_a(tiempo):
    await asyncio.sleep(tiempo)
    print("A")

async def funcion_b(tiempo):
    await asyncio.sleep(tiempo)
    print("B")

async def funcion_c(tiempo):
    await asyncio.sleep(tiempo)
    print("C")

async def funcion_d(tiempo):
    await asyncio.sleep(tiempo)
    print("D")


async def main():
    await asyncio.gather(
        funcion_c(3),
        funcion_b(2),
        funcion_a(1)
    )

asyncio.run(main())
asyncio.run(funcion_d(1))