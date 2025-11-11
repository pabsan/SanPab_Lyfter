products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

totals = {}

for prod in products:
    if totals.get(prod.get('category')) is None:
        totals[prod.get('category')] = prod.get('price')
    else:
        totals[prod.get('category')] = totals[prod.get('category')] + prod.get('price') 

print(totals)