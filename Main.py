import pygame.font, random

from Help import *

class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, PIPE_X, PIPE_Y, PIPE_WIDTH, PIPE_HEIGHT)
        self.img = img
        self.is_passed = False

class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, Bird_X, Bird_Y, Bird_Width, Bird_Height)
        self.img = img

def fit(img, width, height, rotate=False):
    if rotate: output = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(img), 180), (width, height))
    else: output = pygame.transform.scale(pygame.image.load(img), (width, height))

    return output

def create_pipe():
    global Time

    min_top_y = -150  # Clamp top pipe Y to avoid too high pipes
    max_top_y = -40  # Adjust for your game
    random_y = random.randint(min_top_y, max_top_y)
    opening = HEIGHT/4.2

    pipe_U = Pipe(fit(PIPE, 50, 300, True))
    pipe_U.y = random_y
    Pipes.append(pipe_U)

    pipe_D = Pipe(fit(PIPE, 50, 300))
    pipe_D.y = pipe_U.y + PIPE_HEIGHT + opening
    Pipes.append(pipe_D)

    Time = max(Time - Delay, 500)

def draw():
    win.blit(pygame.image.load(BACKGROUND), (0, 0))
    win.blit(pygame.image.load(BASE), (0, 520))
    win.blit(Player_working, (Bird_X, Bird_Y))

    for pipe in Pipes:
        win.blit(pipe.img, pipe)

    text = f"Score: {int(Score)}"

    if Game_over: text = f"Game Over: {int(Score)}"

    render = Font.render(text, True, "white")
    win.blit(render, (5, 5))

def move():
    global Bird_Y, Velocity_Bird, Score, Game_over, PLAYER

    Velocity_Bird += Gravity
    Bird_Y = min(max(Bird_Y + Velocity_Bird, 0), HEIGHT)

    if Bird_Y > HEIGHT:
        Game_over = True
        return

    for pipe in Pipes:
        pipe.x += Velocity_Pipe

        if not pipe.is_passed and pipe.y > 0 and Bird_Center > pipe.right:
            Score += 1
            pipe.is_passed = True

        offset = (int(pipe.x - Bird_X), int(pipe.y - Bird_Y))

        if bird_mask.overlap(pipe_mask, offset):
            Game_over = True

    if Pipes and Pipes[0].right < -2:
        Pipes.pop(0)

pygame.init()

Font = pygame.font.SysFont("Calibri", 26)

Bird_Width = 34
Bird_Height = 24

FPS = 60
WIDTH = 350
HEIGHT = 600
GroundY = HEIGHT * 0.8
PLAYER = "bird.png"
BACKGROUND = "background.png"
PIPE = "pipe.png"
BASE = "ground.png"

PIPE_X = WIDTH
PIPE_Y = 0
PIPE_WIDTH = 30
PIPE_HEIGHT = 300
Velocity_Pipe = -2
Velocity_Bird = 0
Gravity = 0.35

Score = 0
Game_over = False

Delay = 20
Time = 1500

Bird_X = WIDTH / 8
Bird_Y = HEIGHT / 2

pipes_time = pygame.USEREVENT + 0
pygame.time.set_timer(pipes_time, Time)

Pipes = []

Player_working = fit(PLAYER, 60, 60, False)

bird_mask = pygame.mask.from_surface(Player_working)
pipe_mask = pygame.mask.from_surface(fit(PIPE, PIPE_WIDTH, PIPE_HEIGHT))

Bird_Center = Bird_X + Player_working.get_width() // 2

# main

win = setWindow(WIDTH, HEIGHT)

FPSCLOCK = pygame.time.Clock()
setTitle("Flappy Bird")

exit_ = False

while not exit_:
    for event in getEvent():
        if is_close(event.type):
            exit_ = True

        elif event.type == pipes_time and not Game_over:
            create_pipe()

        if event.type == pygame.KEYDOWN:
            if check(event, SPACE, UP):
                Velocity_Bird = -5

    if not Game_over:
        move()
        draw()
        update()
        FPSCLOCK.tick(FPS)

pygame.quit()
quit()