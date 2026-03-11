jugador = input("Ingrese su nombre: ")
print(f"Bienvenido al juego de preguntas! {jugador}")

contador = 0

pregunta1 = int(input("Cuant es la suma de 89 + 56?"))
pregunta2 = input("Como se llama el artefacto que vuela para transportar gente?")
pregunta3 = int(input("Cuantas patas tienen los insectos?"))
pregunta4 = input("Cual es el color de la frutilla?")

# Preguntas al usuario
if pregunta1 == 145:
    contador + 1 
elif pregunta2 == "avión":
    contador + 1
elif pregunta3 == 6:
    contador + 1 
elif pregunta4 == "rojo" and "Rojo":
    contador + 1
else: 
    print("Terminaron las preguntas")

## Puntajes
puntaje_total = 4

if contador == puntaje_total:
    print("Excelente!!! Puretasoo!!")
elif contador >= puntaje_total:
    print("Muy bien!")
else:
    print("Puede mejorar!")
