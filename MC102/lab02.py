nota = min(float(input()), float(input()), float(input())) >= 7.0
ferias = (input() == "Sim") 
ferias = (input() == "Sim") and ferias
data = min(int(input()), int(input())) < 11
valor = (float(input()) + float(input())) <= 10000.0

if not nota:
	print("NAO. As notas da Carla nao foram suficientes.")
elif not ferias:
	print("NAO. O casal nao esta de ferias.")
elif not data:
	print("NAO. Nenhum 13o salario foi liberado a tempo.")
elif not valor:
	print("NAO. O valor total e muito alto.")
else:
	print("SIM!!!")
