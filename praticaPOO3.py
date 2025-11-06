class pato:
    def quack(self):
        print("O pato faz quack!")

class pessoa:
    def quack(self):
        print("A Pessoa imitou um pato: quack!")

    def comer(self):
        print("A Pessoa está comendo!")

def fazer_quack(obj):
    obj.quack()

p = pato()
h = pessoa()

fazer_quack(p)
fazer_quack(h)

class gravação:
    def quack(self):
        print("Som gravado:Quack quack!")

class robo:
    def quack(self):
        print("Robo:Q-U-A-C-K em som metálicco!")

        objetos = [pato(),pessoa(),gravação(),robo()]

        for obj in objetos:
            obj.quack