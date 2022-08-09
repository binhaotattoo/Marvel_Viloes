#exercicio Vilões Caneca
class MarvelViloes:
    def __init__(self, nome , poderes, perigo):
            self.nome = nome
            self.poderes = poderes
            self.perigo = int(perigo)  
            
    def setNome (self, nome):
        self.nome = nome
        
    def setPoderes (self, poderes):
        self.poderes = poderes
        
    def setPerigo (self, perigo):
        self.perigo = perigo        
    
    def getNome (self):
        return  self.nome
    
    def getPoderes (self):
        return  self.poderes
    
    def getPerigo (self):
        return  self.perigo
    
    def dominar_mundo(self, perigo):
        if perigo <= 2:
            return "Vilão Morto"
        if perigo > 2 and perigo < 5:
            return "Vilão Preso"
        else:
            return "Vilão Dominou o Mundo"
        
            