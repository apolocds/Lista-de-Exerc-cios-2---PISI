# Coleta de dados do usuário
nome = str(input("Qual é o seu nome? "))
idade = int(input("Quantos anos você tem? "))
cidade = str(input("De qual cidade você é? "))
livros_lidos = int(input("Quantos livros você leu no último ano? "))
horas_estudo = int(input("Quantas horas você dedica aos estudos por semana? "))

# 1. Mensagem personalizada:
print(f"\nBem-vindo(a), {nome} de {cidade}, que tem {idade} anos!")

# 2. Estimativa de leitura:
livros_futuros = livros_lidos * 5
print(f"\nNos próximos 5 anos, você poderia ler aproximadamente {livros_futuros} livros, mantendo o mesmo ritmo de leitura.")

# 3. Cálculo de estudo em anos:
horas_por_ano = horas_estudo * 52
print(f"\nVocê dedica {horas_estudo} horas por semana aos estudos, o que equivale a aproximadamente {horas_por_ano} horas de estudo por ano.")

# 4. Cálculo de idade em décadas:
decadas = idade // 10
anos_restantes = idade % 10
print(f"\nVocê tem {decadas} décadas e {anos_restantes} anos.")

# 5. Idade futura:
idade_objetivo = int(input("\nCom quantos anos você gostaria de alcançar um objetivo pessoal (exemplo: graduação)? "))
anos_para_objetivo = idade_objetivo - idade
print(f"\nFaltam {anos_para_objetivo} anos para você atingir a idade de {idade_objetivo}.")

print(f"\nFim do programa, sucesso na sua vida {nome}!")