#import pgzrun
from time import sleep

TITLE = "Pong 2023"
WIDTH = 700
HEIGHT = 500

player1 = Actor('player', (10, HEIGHT / 2))
player2 = Actor('player', (WIDTH - 10, HEIGHT / 2))
ball = Actor('ball', (WIDTH / 2, HEIGHT / 2))

ball_speed_x = 2
ball_speed_y = 2

player1_score = 0
player2_score = 0

def draw_text():
    screen.draw.text(str(player1_score), center=(WIDTH / 4, 30), fontsize=60)
    screen.draw.text(str(player2_score), center=(WIDTH / 4 * 3, 30), fontsize=60)

def draw():
    screen.clear()
    player1.draw()
    player2.draw()
    screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), (255, 255, 255))
    ball.draw()
    draw_text()

def update():
    global ball_speed_x
    global ball_speed_y
    global player1_score
    global player2_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.y > HEIGHT or ball.y < 0:
        ball_speed_y *= -1
    if ball.x >= WIDTH or ball.x <= 0:
        ball_speed_x *= -1
        if ball.x <= 0:
            player2_score += 1
        else:
            player1_score += 1
        ball.x = WIDTH / 2
        ball.y = HEIGHT / 2
        sleep(1)
    
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
    
    #player1 move - w,s
    if keyboard.w and player1.top > 0:
        player1.y -= 5
    if keyboard.s and player1.bottom < HEIGHT:
        player1.y += 5
        
    #player2 move - up,down
    if keyboard.up and player2.top > 0:
        player2.y -= 5
    if keyboard.down and player2.bottom < HEIGHT:
        player2.y += 5

#pgzrun.go()