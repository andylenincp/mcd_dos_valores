#Haga un programa que permita calcular y mostrar el máximo común divisor de dos valores previamente ingresados.

print("")
print("Haga un programa que permita calcular y mostrar el máximo común divisor de dos valores previamente ingresados.")
print("")
while True:
	try:
		print("")
		# Definición de la función
		def mcd(a, b):
			sobra = 0
			while(b > 0):
				sobra = b
				b = a % b
				a = sobra
			return a
 
		# solicitamos los dos números
		num1 = int(input("Ingrese el primer número: "))
		num2 = int(input("Ingrese el segundo número: "))
		print("El máximo común divisor de ", num1," y ", num2," es ", mcd(num1, num2))
	except ValueError:
		print("Ingreso no válido, intente nuevamente por favor")