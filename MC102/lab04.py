lim_ouro = float(input())
lim_prata = float(input())
lim_bronze = float(input())

ouro = 0
prata = 0
bronze = 0
maior = -1

nota = float(input())

while nota != -1:
    if nota >= lim_ouro:
        ouro += 1
    elif nota >= lim_prata:
        prata += 1
    elif nota >= lim_bronze:
        bronze += 1

    maior = max(maior, nota)

    nota = float(input())

if ouro == 0:
    print("Nenhum participante recebeu medalha de ouro!")
else:
    print("Medalha(s) de ouro: %d" %ouro)

if prata == 0:
    print("Nenhum participante recebeu medalha de prata!")
else:
    print("Medalha(s) de prata: %d" %prata)

if bronze == 0:
    print("Nenhum participante recebeu medalha de bronze!")
else:
    print("Medalha(s) de bronze: %d" %bronze)

print("Maior nota: %.1f" %maior)

