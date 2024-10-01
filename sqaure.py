import pygame 
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

class Sqaure():
    def __init__(self,color,dimensions):
        self.sqaure_surface = screen
        self.sqaure_color = color
        self.sqaure_dimensions = dimensions
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.sqaure_surface,self.sqaure_color,self.sqaure_dimensions)

run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    
    yellow_sqaure = Sqaure("yellow",(50,50,100,100))
    red_sqaure = Sqaure("red",(20,20,50,50))
    blue_sqaure = Sqaure("blue",(300,300,200,200))
    green_sqaure = Sqaure("green",(500,500,100,50))
    yellow_sqaure.draw()
    red_sqaure.draw()
    blue_sqaure.draw()
    green_sqaure.draw()
    pygame.display.update()

    


