#clase colibrí
class Colibri:
    
    #constructor
    def __init__(self, especie, color, edat, pes, velocitat):
        #inicialitzar els atrubits d'aquesta classe
        self.especie = especie
        self.color = color
        self.edat = edat
        self.pes = pes
        self.velocitat = velocitat

    #Getters i setters
    def getEspecie(self):
        return self.especie
    def setEspecie(self, new_especie):
        self.especie = new_especie

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color

    def getEdat(self):
        return self.edat
    def setEdat(self, new_edat):
        self.edat = new_edat

    def getPes(self):
        return self.pes
    def setPes(self, new_pes):
        self.pes = new_pes

    def getVelocitat(self):
        return self.velocitat
    def setVelocitat(self, new_velocitat):
        self.velocitat = new_velocitat
