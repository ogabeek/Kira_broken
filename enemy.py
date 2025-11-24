import pygame
import random
from settings import*
from ability import*
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character

class Mob:
    """
    Enemy mob class (vampire).
    Handles enemy spawning, movement, collision, and AI behavior.
    """
    
    def __init__(self, x: int, y: int, image: pygame.Surface) -> None:
        """
        Initialize the mob.
        
        Args:
            x: Initial X coordinate (unused, mob spawns off-screen)
            y: Initial Y coordinate (unused, mob spawns randomly)
            image: Pygame surface for mob sprite
        """
        self.rect = pygame.Rect(
            random.choice([-50, SCREEN_WIDTH + 50]),  # Spawn off-screen
            random.randint(0, SCREEN_HEIGHT),  # Spawn vertically within the screen
            50, 50  # Vampire size
        )
        self.speed = 2  # Vampire speed
        self.alive = True  # Vampire state (alive/dead)
        # ERROR 6: Check type - should this be a class or an instance?
        self.ability = Ability2

        self.image = image

    def move(self, target: 'Character') -> None:
        """
        Move towards the target character.
        
        Args:
            target: Character object to chase
        """
        # ERROR 7: Check variable name - is 'self.allive' correct?
        if self.allive:
            if target.rect.centerx < self.rect.centerx:
                self.rect.x -= self.speed
            elif target.rect.centerx > self.rect.centerx:
                self.rect.x += self.speed

            if target.rect.centery < self.rect.centery:
                self.rect.y -= self.speed
            elif target.rect.centery > self.rect.centery:
                self.rect.y += self.speed

    def shoot(self) -> None:
        """Shoot bullets using the mob's ability."""
        color: Tuple[int, int, int] = (0, 255, 0)   
        size: int = 2             
        self.ability.shoot(self.rect.centerx - size // 2,
                           self.rect.top,
                           color,
                           size)   

    #def update_bullets(self):
    #    """Update vampire bullets."""
    #    self.ability.update_bullets()   

#---------------------
    def update(self, character: 'Character') -> None:
        """
        Update vampire state and check collisions.
        
        Args:
            character: Player character to check collisions with
        """
        if not self.alive:
            return
        if self.rect.colliderect(character.rect):  # Collision with character
            character.health -= 1  # Decrease health
            # ERROR 8: Check attribute name - does Character have 'alive' attribute?
            if character.health <= 0:
                character.alive = False  # Character dies
            self.alive = False  # Vampire also dies     
        for bullet in character.ability.bullets:  # Iterate over character ability bullets
            if self.rect.colliderect(bullet.rect):  # Check collision with a bullet
                self.alive = False  # Vampire dies from bullet

                character.score += 1  # Increase score
                break

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the mob on the surface if alive.
        
        Args:
            surface: Pygame surface to draw on
        """
        if self.alive:
            surface.blit(self.image, self.rect) 

    @classmethod
    def spawn(cls, image: pygame.Surface) -> 'Mob':
        """
        Factory method to spawn a new mob.
        
        Args:
            image: Pygame surface for mob sprite
            
        Returns:
            New Mob instance spawned at random off-screen position
        """
        return cls(random.choice([-50, SCREEN_WIDTH + 50]), random.randint(0, SCREEN_HEIGHT), image)