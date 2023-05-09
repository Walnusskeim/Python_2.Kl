
class Car:
    def __int__(self,type,power):
        self.typ = type   #self.typ -> definieren des Attributes typ
        self.power = power

    def go(self):
        #Zugriff auf Attribute in allen Methoden der Klasse möglich
        print(f"Ich fahre einen {self.typ} mit {self.leistung} PS.")

melvins_auto = Car("Honda Civic" , 99)
muslims_auto = Car("BMW M2" , 317)

muslims_auto.go()
melvins_auto.go()