"""
class Persona:
    def __init__(self, nome: str, cognome: str, ssn: str) -> None:
        self._nome: str = nome
        self._cognome: str = cognome
        self._ssn: str = ssn

    def get_ssn(self) -> str:

        return self._ssn

    def funzione1(self):
        pass



    def get_name(self):
        
        This function returns a person's name
        input: none
        return: self.name: str, the function returns the person's name
        
        return self._nome
    
    def set_name(self, nome:str) -> None:
        
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        return: None
        
        raise Exception("Non puoi modificare il nome")



persona1: Persona = Persona(nome="Valerio", cognome="Gamba", ssn="GMBVLR03T01H501D")
persona2: Persona = Persona(nome="Giorgia", cognome="Carnabuci", ssn="GRGCRNBC05T01H501D")
print(persona2.get_ssn())
print(persona1._nome,persona1._cognome,persona1._ssn)
print(persona2._nome,persona2._cognome,persona2._ssn)

class Student:
    def __init__(self, name:str,StudyProgram:str) -> None:
        self.name:str = name
        self.StudyProgram:str = StudyProgram
    def printnfo(self) -> str:
        return self.name,self.StudyProgram
studente1: Student = Student(name="Alpha",StudyProgram="Program1")
studente2: Student = Student(name="Bravo",StudyProgram="Program2")
studente3: Student = Student(name="Charlie",StudyProgram="Program3")

print(studente1.printnfo())
print(studente2.printnfo())
print(studente3.printnfo())


class Animal:
    def __init__(self,name:str,color:str,type:str) -> None:
        self.name:str = name
        self.color:str = color
        self.type:str = type

    def setlegs(self) ->int:
        self.legs:int = input("Number of legs: ")
        return self.legs

    def getlegs(self) -> int:
        print(self.legs)

    def printanimal(self):
        print(self.name,self.color,self.type,self.legs)

Animale1: Animal = Animal(name="Toni",color="grey",type="pigeon")
Animale2: Animal = Animal(name="Cerberus",color="brown",type="dog")

Animale1.setlegs()
Animale2.setlegs()
Animale1.getlegs()
Animale2.getlegs()
Animale1.printanimal()
Animale2.printanimal()
"""

class Food:
    def __init__(self,name:str,price:str,description:str) -> None:
        self.name:str = name
        self.price:str = price
        self.description:str = description
class Menu:
    def __init__(self,menu:list = []) -> None:
        self.menu:str = menu
    def addFood(self) -> list:
        self.menu.append()


product1:Food = Food(name="Chicken",price="5€",description="Meat")
product2:Food = Food(name="Apple",price="1€",description="Fruit")
product3:Food = Food(name="Spaghetti",price="1,5€",description="Pasta")
