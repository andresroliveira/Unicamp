def mostra(vet):
	maior = max(vet)
	n = len(vet)

	print('.' * (n + 2))

	for cont in range(maior):
		print('.', end = '')
		for e in vet:
			if(maior-cont <= e):
				print('|', end = '')
			else:
				print(' ', end = '')

		print('.')

	print('.' * (n + 2))

def ordena(vet):
	mostra(vet)

	for i in range(len(vet) - 1):
		for j in range(i+1, len(vet)):
			if(vet[i] > vet[i + 1]):
				vet[i], vet[i + 1] = vet[i + 1], vet[i]
				mostra(vet)

	# print(vet)

def outro_ordena(vet):
	mostra(vet)

	ord = False

	while not ord:
		ord = True

		for i in range(len(vet) - 1):
			if(vet[i] > vet[i + 1]):
				vet[i], vet[i + 1] = vet[i + 1], vet[i]
				ord = False
				mostra(vet)

def bubbleSort (vet):
	mostra(vet)
	for i in range(len(vet) - 1):
		for j in range(0, len(vet) - i - 1):
			if vet[j] > vet[j + 1]:                
				vet[j], vet[j + 1] = vet[j + 1], vet[j]
				mostra(vet)

def main():
	vet = list(map(int, input().split()))

	bubbleSort(vet)

if __name__ == "__main__":
	main()