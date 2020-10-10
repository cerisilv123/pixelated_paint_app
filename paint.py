#Importing Modules 
import pygame
import math

# Declaring Colours as Global Constants
WHITE = (255, 255, 255) 
GREEN = (0, 200, 0 ) #1
BLUE = (0, 0, 128) #2
RED = (200, 0, 0 ) #3
BLACK = (0, 0, 0) #4
PURPLE = (102, 0, 102) #5
SHADOW = (192, 192, 192) #0

class Canvas:
    def __init__(self):
        self.pixel_height = 20
        self.pixel_width = 20
        self.rows = 30
        self.columns = 30
        self.colour_selected = 0
        self.mouse_position = 0,0
        self.mouse_clicked = False
        self.grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     ]

    def display_canvas(self, screen):
        # Display grid on the Canvas
        screen.fill(WHITE)
        for x in range(self.rows):
            for y in range(self.columns):
                if self.grid[x][y] == 0:
                    pygame.draw.rect(screen,SHADOW,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height), 1)
                if self.grid[x][y] == 1:
                    pygame.draw.rect(screen,GREEN,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height))
                if self.grid[x][y] == 2:
                    pygame.draw.rect(screen,BLUE,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height))
                if self.grid[x][y] == 3:
                    pygame.draw.rect(screen,RED,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height))
                if self.grid[x][y] == 4:
                    pygame.draw.rect(screen,BLACK,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height))
                if self.grid[x][y] == 5:
                    pygame.draw.rect(screen,PURPLE,(x * self.pixel_width, y * self.pixel_height,self.pixel_width, self.pixel_height))

    def display_colour_selection(self, screen):
        # Display colour selection to the right of the Canvas
        pygame.draw.rect(screen, GREEN, (600, 0, self.pixel_width * 5, self.pixel_height * 5))
        pygame.draw.rect(screen, BLUE, (600, 100, self.pixel_width * 5, self.pixel_height * 5))
        pygame.draw.rect(screen, RED, (600, 300, self.pixel_width * 5, self.pixel_height * 5))
        pygame.draw.rect(screen, BLACK, (600, 400, self.pixel_width * 5, self.pixel_height * 5))
        pygame.draw.rect(screen, PURPLE, (600, 500, self.pixel_width * 5, self.pixel_height * 5))
        print(self.colour_selected)

    def update_grid_colours(self):
        # Function to upgrade colours on Grid
        if self.mouse_clicked == True and self.mouse_position[0] < 600:
            position_y = math.floor(self.mouse_position[1] / 20) 
            position_x = math.floor(self.mouse_position[0] / 20) 
            self.grid[position_x][position_y] = self.colour_selected

    def return_colour_selected(self, screen):
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 0 and self.mouse_position[1] < 100 and self.mouse_clicked == True:
            self.colour_selected = 1
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 100 and self.mouse_position[1] < 200 and self.mouse_clicked == True:
            self.colour_selected = 2
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 200 and self.mouse_position[1] < 300 and self.mouse_clicked == True:
            self.colour_selected = 0
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 300 and self.mouse_position[1] < 400 and self.mouse_clicked == True:
            self.colour_selected = 3
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 400 and self.mouse_position[1] < 500 and self.mouse_clicked == True:
            self.colour_selected = 4
        if self.mouse_position[0] > 600 and self.mouse_position[0] < 700 and self.mouse_position[1] > 500 and self.mouse_position[1] < 600 and self.mouse_clicked == True:
            self.colour_selected = 5
              
    def get_user_input(self, clicked):
        #Changing Variable
        self.mouse_clicked = clicked

    def get_cursor_position(self):
        #Getting position of Mouse on Canvas
        self.mouse_position = pygame.mouse.get_pos()
              
def main():

    pygame.init()

    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Paint")

    #Creating Class Objects
    canvas = Canvas()

    #Creating clock to control Frames Per Second (FPS)
    clock = pygame.time.Clock()

    running = True
    while running:

        #Handling all user events that occur in program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                canvas.get_user_input(clicked)

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
                canvas.get_user_input(clicked)


        #Main Program Code Below

        canvas.display_canvas(screen)
        canvas.display_colour_selection(screen)
        canvas.get_cursor_position()
        canvas.return_colour_selected(screen)
        canvas.update_grid_colours()
        
        #-----------------------#
        
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
    
