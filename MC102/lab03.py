tipo = input()
char = input()

if(tipo == 'Q'):
	lado = int(input())

	if(lado < 3):
		print("Dimensao incorreta.")
		exit()

	print(lado * char)

	for i in range(lado-2):
		print(char + (lado-2)*' ' + char)

	print(lado * char)

elif(tipo == 'R'):
	largura = int(input())
	altura = int(input())

	if(largura < 3 or altura < 3):
		print("Dimensao incorreta.")
		exit()

	print(largura * char)

	for i in range(altura-2):
		print(char + (largura-2)*' ' + char)

	print(largura * char)


elif(tipo == 'P'):
	largura = int(input())
	altura = int(input())

	if(largura < 3 or altura < 3):
		print("Dimensao incorreta.")
		exit()

	print(largura * char)

	for i in range(altura-2):
		print((i+1)*' ' + char + (largura-2)*' ' + char)

	print((altura-1)*' ' + largura * char)


elif(tipo == 'L'):
	lado = int(input())

	if(lado < 3):
		print("Dimensao incorreta.")
		exit()

	print((lado-1) * ' ' + char)

	for i in range(1,lado-1):
		print((lado-i-1)*' ' + char + (2*i - 1)* ' ' + char)

	# print(char + (lado*2 - 3)*' ' + char)

	for i in range(lado-1,0,-1):
		print((lado-i-1)*' ' + char + (2*i - 1)* ' ' + char)

	print((lado-1) * ' ' + char)

elif(tipo == 'C'):
	lado = int(input())

	if(lado < 3):
		print("Dimensao incorreta.")
		exit()

	print(lado*' ' + lado*char)

	for i in range(lado-2):
		print(lado*' ' + char + (lado - 2)*' ' + char)

	print((3*lado) * char)

	for i in range(lado-2):
		print(char + (lado - 2)*' ' + char + char + (lado - 2)*' ' + char + char + (lado - 2)*' ' + char)

	print((3*lado) * char)

	for i in range(lado-2):
		print(lado*' ' + char + (lado - 2)*' ' + char)	

	print(lado*' ' + lado*char)

else:
	print("Objeto incorreto.")
