#clase cotxe
class Cotxe:
    
    #constructor
    def __init__(self, marca, model, any_fabricació, color, preu):
        #inicialitzar els atrubits d'aquesta classe
        self.marca = marca
        self.model = model
        self.any_fabricació = any_fabricació
        self.color = color
        self.preu = preu

    #Getters i setters
    def getMarca(self):
        return self.marca
    def setMarca(self, new_marca):
        self.marca = new_marca

    def getModel(self):
        return self.model
    def setModel(self, new_model):
        self.model = new_model

    def getAny_fabricació(self):
        return self.any_fabricació
    def setAny_fabricació(self, new_any_fabricació):
        self.marca = new_any_fabricació

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color

    def getPreu(self):
        return self.preu
    def setPreu(self, new_preu):
        self.preu = new_preu
    
        