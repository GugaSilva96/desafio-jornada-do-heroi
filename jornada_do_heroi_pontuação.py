NomeDoPersonagem = input("Qual o nome do seu Herói?")
XP = int(input("Qual o nivel de XP do seu Herói"))

def verificar_nivel(XP):
    if XP < 1000:
        return "Ferro"
    elif 1001 <= XP <= 2000:
        return "Bronze"
    elif 2001 <= XP <= 5000:
        return "Prata"
    elif 6001 <= XP <= 7000:
        return "Ouro"
    elif 7001 <= XP <= 8000:
        return "Platina"
    elif 8001 <= XP <= 9000:
        return "Ascendente"
    elif 9001 <= XP <= 10000:
        return "Imortal"
    elif XP >= 10001:
        return "Radiante"
    else:
        return "XP inválido"

nivel = verificar_nivel(XP) 

print(f"O Herói de nome {NomeDoPersonagem} está no nível de {nivel}.")
