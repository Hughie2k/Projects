import pygame
import os

class Stone:

    def __init__(self, x, y, colour, bg):
        self.MASS = 10
        self.RADIUS = 50
        self.COLOUR = colour
        self.BG = bg

        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.ax, self.ay = 0, 0

    
    def change_stone_vectors(self, fps):
        self.x, self.y = self.x + self.vx / fps, self.y + self.vy / fps
        self.vx, self.vy = self.vx + self.ax / fps, self.vy + self.ay / fps

    def draw(self):
        pygame.draw.circle(self.BG, self.COLOUR, (self.x, self.y), self.RADIUS)

class Strip:

    def __init__(self):
        self.WIDTH, self.HEIGHT = 1300, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 144
        self.STONES_PER_SIDE = 8
        self.COLOUR1, self.COLOUR2 = (255, 0, 0), (0, 255, 0)

        self.STONES = []
        self.current_stone = 0
        self.make_stones(self.STONES_PER_SIDE, self.COLOUR1, self.COLOUR2)        

    def draw_window(self):
        self.WIN.fill((118,181,211))
        for stone in self.STONES:
            stone.draw()
        pygame.display.update()
        
    def make_stones(self, num, colour1, colour2): 
        colours = (colour1, colour2)
        for i in range(2 * num):
            self.STONES.append(Stone(0, 0, colours[i>=num], self.WIN))

    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_window()
            
if __name__ == '__main__':
    ins = Strip()
    ins.main()