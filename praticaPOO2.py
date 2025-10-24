class jogo:
    def __init__(self, nome, gênero, publicadora, geração, console) -> str:
        self.nome = nome
        self.gênero = gênero
        self.publicadora = publicadora
        self.geração = geração
        self.console = console

    def apresentar(self):
        return f"O jogo {self.nome} é do gênero {self.gênero}, feito pela públicadora {self.publicadora} pro console {self.console} na {self.geração} geração"
    
class MM2(jogo):
     def __init__(self,nome,gênero,publicadora,geração,console,Bossrush, Style) -> str:
        super().__init__(nome,gênero,publicadora,geração,console)
        self.Bossrush = Bossrush
        self.Style = Style

        def apresentar(self):
            base = super().apresentar()
            if Bossrush == 's':
                return f"{base}, o Jogo tem uma Boss Rush no final, aonde se enfrentam todos os chefões uma atraz do outro!"
            elif Style == 's':
                return f"{base}, o Jogo tem uma barra de estila que mede a criatividade de sus combos!"


class DMC(jogo):
     def __init__(self,nome,gênero,publicadora,geração,console,Bossrush, Style) -> str:
        super().__init__(nome,gênero,publicadora,geração,console)
        self.Bossrush = Bossrush
        self.Style = Style

        def apresentar(self):
            base = super().apresentar()
            if Bossrush == 's':
                return f"{base}, o Jogo tem uma Boss Rush no final, aonde se enfrentam todos os chefões uma atraz do outro!"
            elif Style == 's':
                return f"{base}, o Jogo tem uma barra de estila que mede a criatividade de sus combos!"

class HFR(jogo):
     def __init__(self,nome,gênero,publicadora,geração,console,Bossrush, Style) -> str:
        super().__init__(nome,gênero,publicadora,geração,console)
        self.Bossrush = Bossrush
        self.Style = Style

        def apresentar(self):
            base = super().apresentar()
            if Bossrush == 's':
                return f"{base}, o Jogo tem uma Boss Rush no final, aonde se enfrentam todos os chefões uma atraz do outro!"
            elif Style == 's':
                return f"{base}, o Jogo tem uma barra de estila que mede a criatividade de sus combos!"
            
mm2=MM2('Megaman 2','Ação e Plataforma','Capcom','Segunda','Nintendo Enterteinment System', 's', 'n')
dmc=DMC('Devil may Cry','Hack and Slash','Capcom','Sexta','Playstation 2', 'n', 's')
hfr=HFR('Hi-Fi Rush','Ação','Bethesda','Nona','Xbox series X/S,Playstation 5', 's', 's')    
        
print(mm2.apresentar())
print(dmc.apresentar())
print(hfr.apresentar())

