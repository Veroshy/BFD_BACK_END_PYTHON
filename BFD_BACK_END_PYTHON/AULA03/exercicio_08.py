import datetime

hora_atual = datetime.datetime.now()
nome_usuario = input("Digite o seu nome:")

print(f'olá, {nome_usuario} Agora são {hora_atual.strftime("%H:%M")}hora.')