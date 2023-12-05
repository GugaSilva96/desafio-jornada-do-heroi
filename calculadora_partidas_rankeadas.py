quantidade_vitorias = int(input("Informe a quantidade de vitórias: "))
quantidade_derrotas = int(input("Informe a quantidade de derrotas: "))

def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"
    else:
        nivel = "Nível indefinido"

    mensagem = f"O Herói tem um saldo de {saldo_vitorias} está no nível de {nivel}"
    return mensagem

resultado = calcular_nivel(quantidade_vitorias, quantidade_derrotas)
print(resultado)
