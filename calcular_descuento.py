def calculador():
    print("\nHola, esta función te ayudará a calcular un descuento para un cliente,\ndependiendo de que tan cara o barata sea su compra.")

    while True:
        try:
            pago = float(input("¿Cuál es la factura del total de hoy, por favor? "))
            break
        except:
            print("Debes ingresar un número")
            continue


    if pago == 0:
        print("No se puede calcular un porcentaje sobre cero")
    elif  0 < pago < 150:
        descuento = 18
        print(f"Tu  descuento del total de ${pago} es de {descuento}%")
        print(f"Tu factura final es: ${pago - (pago*descuento / 100)}")
    elif 150 < pago < 300:
        descuento = 25
        print(f"Tu  descuento del total de ${pago} es de {descuento}%")
        print(f"Tu factura final es: ${ pago - (pago*descuento / 100)}")
    elif 300 < pago < 600:
        descuento = 40
        print(f"Tu  descuento del total de ${pago} es de {descuento}%")
        print(f"Tu factura final es: ${pago - (pago*descuento / 100)}")
    elif pago > 600:
        descuento = 50
        print(f"Tu  descuento del total de ${pago} es de {descuento}%")
        print(f"Tu factura final es: ${pago - (pago*descuento / 100)}")
    else:
        print("No se puede aplicar un descuento sobre un número negativo")



calculador()