import random

balota = int(input('Ingrese el valor de su compra: '));
balotaRoja = (balota * 10) / 100;
balotaVerde = (balota * 15) / 100;
balotaAzul = (balota * 20) / 100;
balotaAmarilla = (balota * 50) / 100;
balotaNegra = (balota * 100) / 100;

balotas = ['roja', 'verde', 'azul', 'amarilla', 'negra'];

if balota >= 50000:
    descuento = random.choice(balotas)
    if descuento == 'roja':
        print(f"Su descuento es del 10%: {balotaRoja}");
        print(f"El precio que debe pagar es de: {balota - balotaRoja}");
        print(f"su balota es: {descuento}");
    elif descuento == 'verde':
        print(f"Su descuento es del 15%: {balotaVerde}");
        print(f"El precio que debe pagar es de: {balota - balotaVerde}");
        print(f"su balota es: {descuento}");
    elif descuento == 'azul':
        print(f"Su descuento es del 20%: {balotaAzul}");
        print(f"El precio que debe pagar es de: {balota - balotaAzul}");
        print(f"su balota es: {descuento}");
    elif descuento == 'amarillo':
        print(f"Su descuento es del 50%: {balotaAmarilla}");
        print(f"El precio que debe pagar es de: {balota - balotaAmarilla}");
        print(f"su balota es: {descuento}");
    elif descuento == 'negra':
        print(f"Su descuento es del 100%: {balotaNegra} ES GRATIS!!!");
else: 
    print('Lo siento no participas');


print(f"su presupuesto es de {balota}");