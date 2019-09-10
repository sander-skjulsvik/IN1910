class Human():
    def __init__(self):
        print("Calling Human constructur")
        
class Machine():
    def __init__(self):
        print("Calling Machine constructor")
        
class Cyborg(Human,Machine):
    def __init__(self):
        print("Calling Cyborg constructor")
        super().__init__()
        
c1 = Cyborg()