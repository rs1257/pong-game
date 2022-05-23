import pygame

class Paddle:
  direction = -3

  def __init__(self, position, player):
    self.position = position
    self.player= player

  def draw(self, window):
    rect = pygame.Rect(self.position[0], self.position[1], 20, 60)
    pygame.draw.rect(window, (255, 255, 255), rect)

  def move(self):
    self.position[1] += self.direction
    if self.position[1] < 70:
      self.position[1] = 70
    elif self.position[1] > 470:
      self.position[1] = 470

  def change_direction(self, key):
    if self.player == "p1":
      if key == pygame.K_UP:
        self.direction = -3
      elif key == pygame.K_DOWN:
        self.direction = 3
    elif self.player == "p2":
      if key == pygame.K_w:
        self.direction = -3
      elif key == pygame.K_s:
        self.direction = 3
