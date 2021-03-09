def tupla_float_int(x) :
    x = x[1:-1]       # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla

nota_conceitual = [float(x) for x in input().split()]
nota_laboratorio = [tupla_float_int(x) for x in input().split(' ')]
nota_prova = [float(x) for x in input().split()]
freq = int(input())

s = 0.0

for n in nota_conceitual:
	s += n

mac = s/float(len(nota_conceitual))

s = 0.0
p = 0.0

for t in nota_laboratorio:
	s += t[0]*t[1]
	p += t[1]

ml = s/p
mp = (nota_prova[0]*2 + nota_prova[1]*3)/5

print("Media das atividades conceituais: %.1f" %mac)
print("Media das tarefas de laboratorio: %.1f" %ml)
print("Media das provas: %.1f" %mp)

mfim = 0

if freq >= 75:
	if mp >= 5 and ml >= 5:
		melem = 0.6 * mp + 0.3 * ml + 0.1 * mac	
		mfim = max(5, melem)
		print("Aprovado(a) por nota e frequencia.")
	elif mp < 2.5 or ml < 2.5:
		mfim = min(mp, ml)
		print("Reprovado(a) por nota.")
	else:
		exame = float(input())
		print("Nota no exame: %.1f" %exame)
		mfim = (min(mp, ml) + exame)/2

		if mfim >= 5:
			print("Aprovado(a) por nota e frequencia.")
		else:
			print("Reprovado(a) por nota.")
else:
	mfim = min(mp, ml)
	print("Reprovado(a) por frequencia.")

print("Media final: %.1f" %mfim)