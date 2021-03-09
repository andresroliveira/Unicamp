from forca import lista_palavras, cenas_forca
global incorreta
global solucao

def quadro(tentativa):
	print()	
	print(cenas_forca[tentativa])

	print("Palavra: %s" %solucao[0],end = '')

	for i in range(1, len(solucao)):
		print("  " + solucao[i], end='')
	print()

	if len(incorreta) > 0:
		print("Tentativa(s) incorreta(s):", end = '')
		for i in incorreta:
			print(end=' ')
			print(end=i)
		print()


sel = int(input("Escolha um numero entre 0 e 49: "))

if sel < 0 or sel >= 50:
	print("Numero invalido.")
	exit()


palavra = lista_palavras[sel]
n = len(palavra)

tentativa = 0
acertada = 0

incorreta = []
solucao = ['_' for i in range(n)]
conj = set()

# print(cenas_forca[0])

while tentativa < 6 and acertada != n:
	quadro(tentativa)
	letra = input("Proxima letra: ")

	if letra in conj:
		print("Voce jah escolheu esta letra.")
		# quadro(tentativa)
		continue

	conj.add(letra)

	if letra in palavra:
		for i in range(n):
			if letra == palavra[i]:
				solucao[i] = letra
				acertada += 1
	else:
		tentativa += 1
		incorreta.append(letra)

	# quadro(tentativa)

quadro(tentativa)

if acertada == n:
	print("Palavra encontrada!")
else:
	print("Palavra oculta: %s" %palavra)