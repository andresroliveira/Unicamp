def mostra_vetor(vetor):
	tam = len(vetor)

	print("+-----" * tam + '+')

	for v in vetor:
		print("| %.3d " %v, end = '')
	print('|')

	print("+-----" * tam + '+')

def mostra_vetor_l_r(vetor, l, r, mid):
	print("      "*l + "+-----"*(mid-l) + "+=====" + "+-----"*(r-mid) + '+')

	print("      "*l, end = '')
	for i in range(l, r+1):
		v = vetor[i]
		c = ' '
		if v == vetor[mid]:
			c = '|'
		print("|%s%.3d%s" %(c, v, c), end = '')
	print('|')

	print("      "*l + "+-----"*(mid-l) + "+=====" + "+-----"*(r-mid) + '+')

def esta_ordenado(vetor):
	ordenado = vetor.copy()
	ordenado.sort()

	return ordenado == vetor

def busca_binaria(vetor, key):
	mostra_vetor(vetor)

	if not esta_ordenado(vetor):
		return -2

	l = 0
	r = len(vetor) - 1

	while l <= r:
		mid = (l + r) // 2

		mostra_vetor_l_r(vetor, l, r, mid)

		if vetor[mid] == key:
			return mid
		elif key < vetor[mid]:
			r = mid - 1
		else:
			l = mid + 1

	return -1

def main():
	key     = int(input())
	vetor   = list(map(int, input().split()))

	print("Elemento procurado: %.3d" %key)
	pos = busca_binaria(vetor, key)

	if pos == -2:
		print("Vetor nao estah ordenado")
	elif pos == -1:
		print("O elemento nao foi encontrado")
	else:
		print("O elemento estah na posicao %d" %pos)

if __name__ == "__main__":
	main()
