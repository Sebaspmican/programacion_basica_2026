edad=int(input("ingresa tu edad:"))
licencia=input("¿tiene licencia de conducir?(si/no)")
if edad >= 18 and licencia== "si":
    print("¡Puedes conducir!, maneja con cuidado")

else:
    print("No puedes conducir, necesitas tener al menos 18 años y una licencia de conducir valida")
