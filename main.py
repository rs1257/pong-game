import os
import sys
import pygame

from paddle import Paddle
from ball import Ball

X_SIZE = 800
Y_SIZE = 600

def main():
  pygame.init()

  # center the window created  
  os.environ['SDL_VIDEO_CENTERED'] = '1'
  
  game_display = pygame.display.set_mode((X_SIZE, Y_SIZE))

  clock = pygame.time.Clock()

  score_p1, score_p2 = 0, 0
  p1 = Paddle([100, 260], "p1")
  p2 = Paddle([680, 260], "p2")
  ball = Ball()
  
  while True:
    pygame.display.set_caption('Pong Game - %s : %s' % (score_p1, score_p2))
    game_display.fill((0,0,0))
  
    draw_border(game_display)
    p1.draw(game_display)
    p2.draw(game_display)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYUP:
          p1.change_direction(event.key)
          p2.change_direction(event.key)

    p1.move()
    p2.move()
    score_update = ball.move(p1.position, p2.position)
    score_p1 += score_update[0]
    score_p2 += score_update[1]
    ball.draw(game_display)

    pygame.display.update()
    clock.tick(60)


def draw_border(game_display):
  rect = pygame.Rect(50, 50, 20, 500)
  pygame.draw.rect(game_display, (255, 255, 255), rect)
  rect = pygame.Rect(730, 50, 20, 500)
  pygame.draw.rect(game_display, (255, 255, 255), rect)
  rect = pygame.Rect(50, 530, 700, 20)
  pygame.draw.rect(game_display, (255, 255, 255), rect)
  rect = pygame.Rect(50, 50, 700, 20)
  pygame.draw.rect(game_display, (255, 255, 255), rect)

if __name__ == '__main__':
  main()