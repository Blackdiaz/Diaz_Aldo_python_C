año_actual = 2022

nombre = input("¿Cuál es tu nombre(s)? ")
apellido1 = input("¿Cuál es tu primer apellido? ")
apellido2 = input("¿Cuál es tu segundo apellido? ")
año_nacimiento = int(input("¿En qué año naciste? "))
mes_dia_nacimiento = input("¿En qué mes y día naciste? (en el siguiente formato 'mm-dd') ")

# Impresión A
nombre_completo_mayusculas = (nombre + " " + apellido1 + " " + apellido2).upper()
print("Este es tu nombre completo en mayúsculas: " + nombre_completo_mayusculas)

# Impresión B
nombre_completo_minusculas = (nombre + " " + apellido1 + " " + apellido2).lower()
print("Este es tu nombre completo en minúsculas: " + nombre_completo_minusculas)

# Impresión C
fecha_nacimiento = mes_dia_nacimiento + "-" + str(año_nacimiento)
print("Esta es tu fecha de nacimiento: " + fecha_nacimiento)

# Impresión D
edad = año_actual - año_nacimiento
print("Esta es tu edad: " + str(edad))

# Impresión E
vocales = ['a', 'e', 'i', 'o', 'u']
nombre_completo = nombre + apellido1 + apellido2
cantidad_vocales = sum([1 for letra in nombre_completo.lower() if letra in vocales])
print("Tu nombre completo tiene " + str(cantidad_vocales) + " vocales.")

# Impresión F
cantidad_letras = len(nombre_completo.replace(" ", ""))
print("Tu nombre completo tiene " + str(cantidad_letras) + " letras.")

# Impresión G
es_entero = isinstance(edad, int)
print("¿Tu edad es un carácter de tipo número? " + str(es_entero))

# Impresión H
es_alfanumerico = nombre_completo.isalnum()
print("¿Tu nombre completo es un carácter de tipo alfanumérico? " + str(es_alfanumerico))

# Impresión I
edad_en_10_anios = edad + 10
print("Tu edad en 10 años será: " + str(edad_en_10_anios))

# Impresión J
edad_en_20_anios = edad + 20
media_edades = (edad + edad_en_20_anios) / 2
print("La media de tu edad actual y tu edad en 20 años es: " + str(media_edades))
