class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = []
            for y in range(self.height):
                for x in range(self.width):
                    picture.append('*')
                picture.append('\n')
            picture = ''.join(picture)  
            return picture
        
    def get_amount_inside(self, other_shape):
        a1 = self.get_area()
        a2 = other_shape.get_area()
        value = a1 // a2
        return value
    
    def __str__(self):
        str_out = f"Rectangle(width={self.width}, height={self.height})"
        return str_out
        
        
    
class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = self.width
        
        
    def set_side(self, width):
        self.width = width
        self.height = self.width
        
    def set_height(self, height):
        self.height = height
        self.width = height
        
    def set_width(self, width):
        self.width = width
        self.height = width
        
    def __str__(self):
        str_out = f"Square(side={self.width})"
        return str_out
        
