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

def printMat(MATRIZ, n):
	print("+----------------+ " * (n-1) + "+----------------+")
	print("| B  I  N  G  O  | " * (n-1) + "| B  I  N  G  O  |")
	print("+================+ " * (n-1) + "+================+")

	grid = MATRIZ.copy()
	# print(grid)

	for i in range(len(grid)):
		grid[i] = transpose(grid[i])

	for i in range(5):
		for j in range(n):
			if j != 0:
				print(end = ' ')

			print('|', end = ' ')

			for e in grid[j][i]:
				if e == -1:
					print('XX', end = ' ')
				else:
					print('%.2d' %e, end = ' ')

			print('|', end = '')
		print()
	print("+----------------+ " * (n-1) + "+----------------+")

def leituraBingo():
	aux = []	

	for i in range(5):
		lin = input().split()

		for j in range(len(lin)):
			if lin[j] == "XX":
				lin[j] = -1
			else:
				lin[j] = int(lin[j])

		aux.append(lin)

	return transpose(aux)

def consulta(grid, tipo, num):
    if num in grid[tipo]:
        for i in range(len(grid[tipo])):
            if num == grid[tipo][i]:
                grid[tipo][i] = -1
                break
                
        if bingo(grid):
            return (grid, 2)
        return (grid, 1)
    return (grid, 0)

def main():
	n = int(input())

	grid = []

	for _ in range(n):
		grid.append(leituraBingo())

	printMat(grid, n)

	q = int(input())

	for _ in range(q):
		tipo, num = map(str, input().split('-'))
		print("%s-%s"%(tipo, num))
		num = int(num)
		tipo = classificar(tipo)

		mostra = False
		foi = False

		for i in range(n):
			grid[i], c = consulta(grid[i], tipo, num)

			if(c == 1):
				mostra = True
			if(c == 2):
				foi, mostra = True, True

		if(mostra):
			printMat(grid, n)
		if(foi):
			print("BINGO!")
			break

if __name__== '__main__':
    main()
