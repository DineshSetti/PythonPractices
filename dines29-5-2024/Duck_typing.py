class India:
    def capital(self):
        print("karnataka")
class Usa:
    def capital(self):
        print("california")
def name(obj):
    obj.capital()

obj1=India()
name(obj1)
obj2=Usa()
name(obj2)