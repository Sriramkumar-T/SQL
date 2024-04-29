class phone:
    def __init__(self,brand,price,charger):
        self.brand=brand
        self.price=price
        self.charger=charger
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("charger:",self.charger)
samsung=phone("samsung","120000","c type")
samsung.display()
        
