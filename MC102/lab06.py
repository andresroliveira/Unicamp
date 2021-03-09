def add(dicionario, time, pontuacao, vitoria, saldo, gol):
	if not(time in dicionario):
		dicionario[time] = [0, 0, 0, 0]

	dicionario[time][0] += pontuacao
	dicionario[time][1] += vitoria
	dicionario[time][2] += saldo
	dicionario[time][3] += gol

def compara(a, b):
	if(a[0] != b[0]):
		return a[0] > b[0]

	if(a[1] != b[1]):
		return a[1] > b[1]

	if(a[2] != b[2]):
		return a[2] > b[2]

	return a[3] > b[3]

dicionario = {}
n = int(input())

for _ in range(n*(n-1)):
	entrada = input().split(' ')
	time_a = entrada[0]
	gols_a = int(entrada[1])
	time_b = entrada[3]
	gols_b = int(entrada[4])   

	if(gols_a > gols_b):
		add(dicionario, time_a, 3, 1, gols_a - gols_b, gols_a)
		add(dicionario, time_b, 0, 0, gols_b - gols_a, gols_b)
	elif(gols_b > gols_a):
		add(dicionario, time_a, 0, 0, gols_a - gols_b, gols_a)
		add(dicionario, time_b, 3, 1, gols_b - gols_a, gols_b)
	else:
		add(dicionario, time_a, 1, 0, 0, gols_a)
		add(dicionario, time_b, 1, 0, 0, gols_b)

maior = [-1, -1, -1, -1]
vencedor = ""

for t in sorted(dicionario):
	atu = dicionario[t]
	print(t, atu[0], atu[1], atu[2], atu[3])

	if(compara(atu, maior)):
		maior = atu
		vencedor = t

print("Vencedor: %s" %vencedor)