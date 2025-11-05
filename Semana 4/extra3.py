celcius_temp = int(input("Ingrese temperatura en Celsius: "))

fahrenheit = (celcius_temp * (9/5)) + 32
kelvin = celcius_temp + 273.15

print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")