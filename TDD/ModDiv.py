class ModDiv:
    
    def __init__(self):
        self.result = 0
        
    def mod(self, a, b):
        if a < b:
            return a
        else:
            return self.mod(a - b, b)

    def div(self, a, b):
        if a < b:
            return 0
        else:
            return 1 + self.div(a - b, b)