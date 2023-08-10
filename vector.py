class Vector:
    def __init__(self, x=None, y=None,tuple=None):
        if tuple:
            self.x = tuple[0]
            self.y = tuple[1]
        elif x == None or None == y:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    def divide_by_int(self,number):
        return Vector(self.x // number, self.y // number)
    
    def __str__(self):
        if self.x == 1 and self.y == 0:
            return "right"
        elif self.x == -1 and self.y == 0:
            return "left"
        elif self.x == 0 and self.y == -1:
            return "up"
        elif self.x == 0 and self.y == 1:
            return "down"
        elif self.x == 0 == self.y:
            return "stop"
        
        return f"(Vector: {self.x}, {self.y})"
    
    def tuple(self):
        return self.x,self.y
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __floordiv__(self,other):
        return Vector(self.x // other.x, self.y // other.y)
    
    def __truediv__(self,other):
        return self.__floordiv__(other)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")
    
    def __delitem__(self, index):
        if index == 0:
            self.x = 0
        elif index == 1:
            self.y = 0
        else:
            raise IndexError("Index out of range")