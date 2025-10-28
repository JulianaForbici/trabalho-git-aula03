# Programa para cálculo de nota

# Entrada das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"\nMédia do aluno: {media:.2f}")

# Verifica a situação do aluno
if media >= 7:
    print("Status: Aprovado ✅")
elif media >= 5:
    print("Status: Recuperação ⚠️")
else:
    print("Status: Reprovado ❌")
