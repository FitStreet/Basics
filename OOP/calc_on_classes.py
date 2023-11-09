class Calc:

    def add(self,x,y):
        return x + y

    def razn(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x // y
    
    def delen(self, x, y):
        return x * y
    

        
operation = Calc()
print(operation.add(3,4))
print(operation.razn(3,4))
print(operation.mul(3,4))
print(operation.delen(3,4))