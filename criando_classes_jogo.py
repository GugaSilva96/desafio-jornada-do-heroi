class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        
        mensagem = f"o {self.tipo} {self.nome} atacou usando {ataque}"
        print(mensagem)


# Exemplo de uso da classe Heroi
heroi1 = Heroi("Kratos", 30, "guerreiro")
heroi1.atacar()

heroi2 = Heroi("Gandalf", 1000, "mago")
heroi2.atacar()

heroi3 = Heroi("Bruce Lee", 35, "monge")
heroi3.atacar()

heroi4 = Heroi("Naruto", 28, "ninja")
heroi4.atacar()