"""Task 1"""
class Product:
    base_price = 20000
    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color

    def has_garantiya(self, year):
        if self.year + 2 < year:
            return "Ваша гарантия истекла"
        else:
            return "Гарантия действительна"
    @classmethod    
    def change_price(cls, rate):
        cls.base_price += int(cls.base_price * rate / 100)
        return cls.base_price


# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 

"""Task 2"""


