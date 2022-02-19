import pygame
import os


class Ball:

    def __init__(self, width, height, x, y, vx, vy, ax, ay):
        self.BALL_IMAGE = pygame.image.load(os.path.join('assets', 'football.png'))
        self.WIDTH, self.HEIGHT = width, height
        self.BALL = pygame.transform.scale(self.BALL_IMAGE, (self.WIDTH, self.HEIGHT))
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.ax, self.ay = ax, ay


class FootGame:
    
    def __init__(self):

        self.WIDTH, self.HEIGHT = 1920, 1080
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.BACKGROUND_IMAGE = pygame.image.load(os.path.join('assets', 'background.jpg'))
        self.BACKGROUND = pygame.transform.scale(self.BACKGROUND_IMAGE, (self.WIDTH, self.HEIGHT))

        self.BALL_HEIGHT, self.BALL_WIDTH = 50, 50
        self.ball_x, self.ball_y = 0, self.HEIGHT/2
        self.ball_vx, self.ball_vy = 700, 800
        self.ball_ax, self.ball_ay = 0, 980
        self.ball_restitution = 1
        self.BALL = Ball(self.BALL_HEIGHT, self.BALL_WIDTH, self.ball_x, self.ball_y, self.ball_vx, self.ball_vy, self.ball_ax, self.ball_ay)
        self.FPS = 240
        self.time=0

        self.EYE_WIDTH, self.EYE_HEIGHT = 50, 50
        self.EYE_X_CENTRE_1, self.EYE_Y_CENTRE_1 = 0.5*self.WIDTH, 0.5*self.HEIGHT
        self.EYE_X_RANGE, self.EYE_Y_RANGE = 55, 55
        self.EYE_X_CENTRE_2, self.EYE_Y_CENTRE_2 = 0.68*self.WIDTH, 0.55*self.HEIGHT
    
    def draw_eyes(self, x, y): 
        rec1 = pygame.Rect(self.EYE_X_CENTRE_1-self.EYE_WIDTH*1.5, self.EYE_Y_CENTRE_1-self.EYE_HEIGHT/2, self.EYE_WIDTH*3, self.EYE_HEIGHT*2)
        rec2 = pygame.Rect(self.EYE_X_CENTRE_2-self.EYE_WIDTH*1.5, self.EYE_Y_CENTRE_2-self.EYE_HEIGHT/2, self.EYE_WIDTH*3, self.EYE_HEIGHT*2)
        pygame.draw.ellipse(self.WIN, (255,255,255), rec1)
        pygame.draw.ellipse(self.WIN, (255,255,255), rec2)

        pygame.draw.circle(self.WIN, (0,0,0), (self.EYE_X_CENTRE_1 - self.EYE_WIDTH*0.35 + self.BALL.x * self.EYE_X_RANGE / self.WIDTH, self.EYE_Y_CENTRE_1 + self.BALL.y * self.EYE_Y_RANGE / self.HEIGHT), self.EYE_HEIGHT/2)
        pygame.draw.circle(self.WIN, (0,0,0), (self.EYE_X_CENTRE_2 - self.EYE_WIDTH*0.35 + self.BALL.x * self.EYE_X_RANGE / self.WIDTH, self.EYE_Y_CENTRE_2 + self.BALL.y * self.EYE_Y_RANGE / self.HEIGHT), self.EYE_HEIGHT/2)


    def draw_window(self):
        self.WIN.fill((0,0,0))
        self.WIN.blit(self.BACKGROUND, (0,0))
        self.WIN.blit(self.BALL.BALL, (self.BALL.x, self.BALL.y))
        #self.WIN.blit(self.EYE.EYE, (self.EYE.x, self.EYE.y))
        self.draw_eyes(self.BALL.x, self.BALL.y)
        pygame.display.update()
    
    def ball_bounce_sound(self):
        pygame.mixer.init()
        bounce = pygame.mixer.Sound(os.path.join('assets', 'bounce.wav'))
        bounce.set_volume(0.2)
        pygame.mixer.Sound.play(bounce)

    def change_ball_pos(self):

        self.BALL.x, self.BALL.y = self.BALL.x + self.BALL.vx/self.FPS, self.BALL.y + self.BALL.vy/self.FPS

    def change_ball_vel(self):
        
        collide_check_x, collide_check_y = (self.BALL.x > self.WIDTH - self.BALL.WIDTH and self.BALL.vx > 0) or (self.BALL.x < 0 and self.BALL.vx < 0), (self.BALL.y > self.HEIGHT - self.BALL.HEIGHT and self.BALL.vy > 0) or (self.BALL.y < 0 and self.BALL.vy < 0)

        outside_window_x, outside_window_y = self.BALL.x > self.WIDTH - self.BALL.WIDTH or self.BALL.x < 0, self.BALL.y > self.HEIGHT - self.BALL.HEIGHT or self.BALL.y < 0

        if collide_check_x: #and (self.BALL.vx > 1 or self.BALL.vx < -1):
            self.BALL.vx = int(-self.BALL.vx * self.ball_restitution)
            self.ball_bounce_sound()
        
        if collide_check_y: #and (self.BALL.vy > 1 or self.BALL.vy < -1):
            self.BALL.vy = int(-self.BALL.vy * self.ball_restitution)
            self.ball_bounce_sound()

        if not (outside_window_x or outside_window_y):
            self.BALL.vx, self.BALL.vy = self.BALL.vx + self.BALL.ax/self.FPS, self.BALL.vy + self.BALL.ay/self.FPS

        
    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            self.time+=1/self.FPS
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_window()
            self.change_ball_pos()
            self.change_ball_vel()
            #self.EYE.move(self.BALL.x, self.BALL.y)
        pygame.quit()

if __name__ == '__main__':
    ins = FootGame()
    ins.main()





