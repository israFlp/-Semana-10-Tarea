# Crear  un nuevo archivo llamado my_notes.txt.
my_notes = "my_notes.txt"

#Modo de apertura: open w
my_notes = open("my_notes.txt", "w")

#Metodo write(): escribir una linea a la vez
my_notes.write("Linea 1: Tomar un descanso. \n")
my_notes.write("Linea 2: Ir al cine los fines de semana. \n")
my_notes.write("Linea 3: Tomar un cafe. \n")

#Metodo writelines() escribir una lista de lineas
lineas = ["Linea 3: Hacer deporte.\n", "Linea 4: Comer saludable todos los dias.\n"]
my_notes.writelines(lineas)

my_notes.close()

#Abre el archivo my_notes.txt.
my_notes = open("my_notes.txt", "r")

#Lee el contenido del archivo linea por linea utilizando el metodo adecuado
# Metodo 1. read()
print("Metodo 1: read()")
print("___________")
print(my_notes.read())
my_notes.close()

# Metodo 2. readlines()
my_notes = open("my_notes.txt", "r")
print("Metodo 2: readlines()")
print("___________")
for linea in my_notes.readlines():
    print(linea.rstrip("\n"))
my_notes.close()