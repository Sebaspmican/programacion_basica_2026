estudiante=input("¡eres estudiantes?¿si/no?")
total=int(input("escribe el total de su compra "))
descuento= total*0.15

if estudiante == "si" or total >= 200000:
    print("Aplicas para el descuento, el descuento es: ", descuento)

else:
    print ("no aplica descuento")


