
balota = int(input('Ingrese el valor de su compra: '));
balotaRoja = (balota * 10) / 100;
balotaVerde = (balota * 15) / 100;
balotaAzul = (balota * 20) / 100;
balotaAmarilla = (balota * 50) / 100;
balotaNegra = (balota * 100) / 100;

if balota >= 50000:
    descuento = input('Que boleta saco? : ');
    if descuento == 'roja':
        print(f"Su descuento es del 10%: {balotaRoja}");
    elif descuento == 'verde':
        print(f"Su descuento es del 15%: {balotaVerde}");
    elif descuento == 'azul':
        print(f"Su descuento es del 20%: {balotaAzul}");
    elif descuento == 'amarillo':
        print(f"Su descuento es del 50%: {balotaAmarilla}");
    elif descuento == 'negra':
        print(f"Su descuento es del 100%: {balotaNegra} ES GRATIS!!!");
else: 
    print('Lo siento no participas');

    print(f"su presupuesto es de {balota}");
    print(f"su presupuesto es de {balota}");


