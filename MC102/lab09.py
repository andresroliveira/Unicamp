def transpose(m):
	n = len(m)
	tran = [[0 for i in range(n)] for j in range(n)]

	for i in range(n):
		for j in range(n):
			tran[i][j] = m[j][i]

	return tran

def verificaLinha(grid):
	for l in grid:
		c = 0
		for e in l:
			if e == -1:
				c += 1

		if c == len(l):
			return True

	return False

def verificaColuna(grid):
	grid = transpose(grid)

	return verificaLinha(grid)

def verificaDiagonal(grid):
	f = 0
	s = 0
	n = len(grid)

	for i in range(n):
		if grid[i][i] == -1:
			f += 1
		if grid[i][n - i - 1] == -1:
			s += 1

	return f == n or s == n

def bingo(grid):
	if verificaLinha(grid):
		return True
	if verificaColuna(grid):
		return True
	if verificaDiagonal(grid):
		return True

	return False

def classificar(tipo):
	if tipo == 'B':
		return 0
	if tipo == 'I':
		return 1
	if tipo == 'N':
		return 2
	if tipo == 'G':
		return 3
	if tipo == 'O':
		return 4
	return -1

def printMat(m):
	print("+----------------+")
	print("| B  I  N  G  O  |")
	print("+================+")

	m = transpose(m)

	for i in range(len(m)):
		print("| ", end = '')

		for j in range(len(m[i])):
			if m[i][j] != -1:
				print("%.2d " %m[i][j], end = '')
			else: 
				print("XX ", end = '')

		print('|')

	print("+----------------+")


def main():
	aux = []

	for i in range(5):
		lin = input().split()

		for j in range(len(lin)):
			if lin[j] == "XX":
				lin[j] = -1
			else:
				lin[j] = int(lin[j])

		aux.append(lin)

	grid = transpose(aux)

	printMat(grid)

	q = int(input())

	for _ in range(q):
		tipo, num = map(str, input().split('-'))
		print("%s-%s"%(tipo, num))
		num = int(num)
		tipo = classificar(tipo)

		# print("%s %d" %(tipo, num))

		if num in grid[tipo]:
			for i in range(len(grid[tipo])):
				if num == grid[tipo][i]:
					grid[tipo][i] = -1
					break

			printMat(grid)

			if bingo(grid):
				print("BINGO!")
				break

main()