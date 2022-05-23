import pygame

class Ball:
  position = [400, 300]
  direction = [-3, -3]
  radius = 10

  def draw(self, window):
    x_pos = self.position[0] - self.radius
    y_pos = self.position[1] - self.radius
    pygame.draw.circle(window, (255, 255, 255), [x_pos, y_pos], 10)
  
  def move(self, p1, p2):
    score = [0, 0]
    x = self.position[0] + self.direction[0]
    y = self.position[1] + self.direction[1]

    if (x > p1[0] and x < p1[0] + 20):
      if (y > p1[1] and y < p1[1] + 40):
        self.direction = [3, -3]
      elif (y > p1[1] + 40 and y < p1[1] + 80):
        self.direction = [3, 3]
    
    if (x > p2[0] and x < p2[0] + 20):
      if (y > p2[1] and y < p2[1] + 40):
        self.direction = [-3, -3]
      elif (y > p2[1] + 40 and y < p2[1] + 80):
        self.direction = [-3, 3]

    if x > 730:
      x = 730
      self.direction[0] = -3
      score = [1, 0]
    elif x < 90:
      x = 90
      self.direction[0] = 3
      score = [0, 1]
    if y > 530:
      y = 530
      self.direction[1] = -3
    elif y < 90:
      y = 90
      self.direction[1] = 3
    
    self.position = [x, y]
    return score
