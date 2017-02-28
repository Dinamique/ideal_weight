altura = float (input ("Digite a sua altura: "))
sexo = input ("Digite o seu sexo ('M' para masculino e 'F' para feminino): ")
if "M" in sexo:
	pesoideal =  (72.7 * altura) - 58
	print ("Seu peso ideal é de %s Kg" % pesoideal)
	peso = input ("Digite o seu peso em Kg: ")
	if float (peso) > pesoideal:
		print ("Você está acima do peso!")
	elif float (peso) == pesoideal:
		print ("Você está dentro do peso!")
	else:
		print ("Você está abaixo do peso!")
if "F" in sexo:
	pesoideal = (62.1 *altura) - 44.7 
	print ("Seu peso ideal é de %s Kg" % pesoideal)
	peso = input ("Digite o seu peso em Kg: ")
	if float (peso) > pesoideal:
		print ("Você está acima do peso!")
	elif float (peso) == pesoideal:
		print ("Você está dentro do peso!")
	else:
		print ("Você está abaixo do peso!")