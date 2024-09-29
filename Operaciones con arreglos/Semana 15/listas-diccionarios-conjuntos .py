
#crear un diccionario de persona

persona={
    "Nombre":"<Israel>",
    "Apellido":"<Azogue>",
    "Edad":28,
    "Ciudad":"Ambato",
}
#obtener valores
print("Nombre :", persona["Nombre"])
print("Apellido :", persona["Apellido"])
print("Edad :", persona["Edad"])
print("Ciudad :", persona["Ciudad"])


# Modificar clave
persona["Ciudad"] = "Baños"
print(persona)

#agregar un nuevo par clave
persona["profesion"]= "Ingeniero en Sistemas"
print(persona)

#eliminar un par clave
del persona["Edad"]
print(persona)




