jugador = input("Ingrese su nombre: ")
print(f"Bienvenido al juego de preguntas! {jugador}")

contador = 0

pregunta1 = int(input("Cuant es la suma de 89 + 56?"))
pregunta2 = input("Como se llama el anumal que dice miau?")
pregunta3 = int(input("Cuantas patas tienen los insectos?"))
pregunta4 = input("Cual es el color de la frutilla?")

# Preguntas al usuario
if pregunta1 == 145:
    contador += 1 
if pregunta2 == "gato":
    contador += 1
if pregunta3 == 6:
    contador += 1 
if pregunta4 == "rojo" and "Rojo":
    contador += 1

## Puntajes

if contador == 4:
    print("Excelente!!! Puretasoo!!")
elif contador >= 2:
    print("Muy bien!") 
else:
    print("Puede mejorar!")
