#Realice un programa que permita calcular y mostrar el máximo común divisor de dos valores previamente ingresados.

print("")
print("Realice un programa que permita calcular y mostrar el máximo común divisor de dos valores previamente ingresados.")
print("")
while True:
	try:
		#Solicitamos al usuario el ingreso de los dos números
		num1 = int(input("Ingrese el primer número: "))
		num2 = int(input("Ingrese el segundo número: "))
		
		#Asignamos el mayor y menor a las variables a y b respectivamente
		a = max(num1, num2)
		b = min(num1, num2)
		
		#Declaramos la variable que guardará el resultado
		resultado = 0
		
		#Se crea el ciclo que hará las iteraciones
		while (b != 0):
		#Este proceso se repetirá hasta que b sea diferente de cero
		
			#Asignamos al resultado el valor de b, si la división es exacta el mcd será el menor de los dos números ingresados,
			#caso contrario la variable resultado irá guardando el valor del resto entre a y b de la iteración anterior.
			resultado = b
			
			#Asignamos a b el valor del resto de la división entre a y b, de forma que b siempre será el divisor
			#de la siguiente iteración.
			b = a % b
			
			#El dividendo de la próxima iteración, la variable a será el resto de la iteración anterior.
			a = resultado
		
		#Mostramos el resultado por pantalla
		print("El máximo común divisor de ", num1," y ", num2," es ", resultado)
	except ValueError:
		print("Ingreso no válido, intente nuevamente por favor")