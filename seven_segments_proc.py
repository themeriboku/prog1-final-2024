import turtle
class Screen_num:
    def __init__(self, color):
        self.color = color

    def draw(self, digit):
        if digit == 0:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.penup()
    
        if digit == 1:
           turtle.goto(50, 100)
           turtle.pendown()
           turtle.right(90)
           turtle.forward(100)
           turtle.forward(100)
           turtle.left(90)
           turtle.penup()

    
        if digit == 2:
           turtle.goto(-50, 100)
           turtle.pendown()
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.forward(100)
           turtle.penup()

        if digit == 3:
           turtle.goto(-50, 100)
           turtle.pendown()
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.forward(-100)
           turtle.left(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.left(90)
           turtle.penup()

        if digit == 4:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.forward(-100)
            turtle.forward(-100)
            turtle.right(90)
            turtle.penup()

        if digit == 5:
           turtle.goto(-50, 100)
           turtle.pendown()
           turtle.forward(100)
           turtle.forward(-100) 
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.left(90)
           turtle.penup()

        if digit == 6:
           turtle.goto(-50, 100)
           turtle.pendown()
           turtle.forward(100)
           turtle.forward(-100) 
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.left(90)
           turtle.goto(-50, 0)
           turtle.pendown()
           turtle.right(90)
           turtle.forward(100)
           turtle.left(90)
           turtle.penup()
    
        if digit == 7:
           turtle.goto(-50, 100)
           turtle.pendown()
           turtle.forward(100)
           turtle.forward(-100)
           turtle.goto(50, 100)
           turtle.pendown()
           turtle.right(90)
           turtle.forward(100)
           turtle.forward(100)
           turtle.left(90)
           turtle.penup()
        

        if digit == 8:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.forward(100)
            turtle.right(90)
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.forward(100)
            turtle.penup()

        if digit == 9:
            turtle.goto(-50, 100)
            turtle.pendown()
            turtle.forward(100)
            turtle.forward(-100) 
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.left(90)
            turtle.goto(50, 100)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.penup()
    
    def clear(self):
          turtle.clear()
        
    def my_delay(dt):
        import time
        start =  time.time()
        while time.time() - start < dt:
            pass

    
