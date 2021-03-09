n = int(input())

vet = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5]

for i in range(len(vet)):
	t = 0

	while(n >= vet[i]):
		n -= vet[i]
		t += 1

	s = "nota" if (vet[i] > 100) else "moeda"

	print("%d %s(s) de R$ %d,%.2d." %(t, s, vet[i]//100, vet[i]%100))
