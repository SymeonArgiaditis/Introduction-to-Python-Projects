class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        if new_width < 0:
            raise ValueError("Width cannot be negative.")
        self.width = new_width

    def set_height(self, new_height):
        if new_height < 0:
            raise ValueError("Height cannot be negative.")
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**(0.5)

    def get_picture(self) -> str:

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""

        for j in range(0, self.height):
            for i in range(0, self.width):
                picture += '*'
            picture += '\n'
        return picture

    def get_amount_inside(self, shape) -> int:
        
        horizontal = self.width // shape.width
        vertical = self.height // shape.height

        return horizontal * vertical
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.height = side
        self.width = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        if side < 0:
            raise ValueError("Width cannot be negative.")
        self.set_side(side)

    def set_height(self, side):
        if side < 0:
            raise ValueError("Height cannot be negative.")
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"

#####

rect = Rectangle(10, 5)

print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

Rectangle(4, 8).get_amount_inside(Rectangle(3, 6))