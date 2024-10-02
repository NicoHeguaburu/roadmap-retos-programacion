def print_call(func):
    def print_func():
        print(f"La funcion {func.__name__} a sido llamada")
    return print_func



@print_call
def func1():
    pass

@print_call
def func2():
    pass

@print_call
def func3():
    pass

func1()
func2()
func3()



#Ejercicio EXTRA:

def call_counter(func):
    def counter():
        counter.call_count += 1
        print(f"La funcion {func.__name__} se a llamado {counter.call_count}")
        return func
    counter.call_count = 0
    return counter


@call_counter
def func4():
    pass

@call_counter
def func5():
    pass

def func6():
    pass

@call_counter
def func7():
    pass



func4()
func4()
func5()
func5()
func5()
func6()
