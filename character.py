import pygame
from ability import *
from typing import Tuple

class Character:
    """
    Player character class.
    Manages player position, movement, health, score, and shooting abilities.
    """
    
    def __init__(self, x: int, y: int, image: pygame.Surface) -> None:
        """
        Initialize the character.
        
        Args:
            x: Initial X coordinate
            y: Initial Y coordinate
            image: Pygame surface for character sprite
        """
        self.rect = pygame.Rect(x, y, 50, 50)  
        self.speed = 5

        self.health = 10  # Initial health
        self.score = 0  # Initial score
        self.isAlive = True
        self.survival_time = 0
  
        self.ability = Ability1()
        self.image = image  

    def move(self, dx: int, dy: int) -> None:
        """
        Move the character by the given delta values.
        
        Args:
            dx: Change in X coordinate (-1, 0, or 1)
            dy: Change in Y coordinate (-1, 0, or 1)
        """
        # ERROR 4: Check variable name - is 'self.speeed' correct?
        self.rect.x += dx * self.speeed
        self.rect.y += dy * self.speed

    def shoot(self) -> None:
        """Shoot bullets using the character's ability."""
        # ERROR 5: Check arguments - are we passing the right number of parameters?
        color: Tuple[int, int, int] = (0, 255, 0)   
        size: int = 10             
        self.ability.shoot(self.rect.centerx - size // 2,
                           self.rect.top,
                           color)   

    def update_bullets(self) -> None:
        """Update all active bullets."""
        self.ability.update_bullets()   

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the character and its bullets on the surface.
        
        Args:
            surface: Pygame surface to draw on
        """
        if self.health > 0:
            surface.blit(self.image, self.rect)
            self.ability.draw(surface)
        else:
            self.isAlive = False   
