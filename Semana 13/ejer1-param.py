def imprimir_parametros(func):
    def wrapper(*args, **kwargs):
        print("Llamada a la función con los siguientes parámetros:")
        print("Posicionales:", args)
        print("Nombrados:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@imprimir_parametros
def calcula_area_rectangulo(base, altura):
    return base * altura

@imprimir_parametros
def saluda(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

# Ejemplo de uso
area = calcula_area_rectangulo(5, 10)
print("Área del rectángulo:", area) # Área del rectángulo: 50
mensaje = saluda("Ana", saludo="Buenos días")
print(mensaje) # Buenos días, Ana!