
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome : "))
    while True:
        pessoa['sexo'] = str(input("Digite [M/F] : ")).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        print("!ERRO! Digite Somente M ou F")
    pessoa['idade'] = int(input("Digite a idade : "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input("Deseja continuar? [S/N] : ")).upper()
        if resp in 'SN':
            break
        print("!ERRO! Digite Somente S ou N")
    if resp == 'N':
        break

print(galera)
print(f'Pessoas Cadastradas: {len(galera)}')
media = soma / len(galera) 
print(f'A Média das Idades é: {media:5.2f}')
