class Fatorial:
    
    def __init__(self):
        self.resultado = 1

    def calcular(self, numero):
        for i in range(1, numero + 1):
            self.resultado *= i
        returnvalue = self.resultado
        self.resultado = 1
        return returnvalue 
    
    
    def __str__(self):
        return f"Fatorial: resultado={self.resultado}"