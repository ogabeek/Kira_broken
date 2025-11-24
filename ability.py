import pygame
import sys
import time
from typing import Tuple, List

# Bullet class
class Bullet:
    """
    Bullet projectile class.
    Handles bullet movement, rendering, and lifetime.
    """
    
    def __init__(self, x: int, y: int, color: Tuple[int, int, int], 
                 size: int, direction: Tuple[int, int]) -> None:
        """
        Initialize a bullet.
        
        Args:
            x: Initial X coordinate
            y: Initial Y coordinate
            color: RGB color tuple (R, G, B)
            size: Size of the bullet in pixels
            direction: Movement direction as tuple (dx, dy)
        """
        self.rect = pygame.Rect(x, y, size, size)  # Rectangle for the bullet
        self.color = color  # Bullet color
        self.speed = 5  # Bullet speed
        self.direction = direction  # Movement direction (vector)
        self.creation_time = time.time()  # Bullet creation time

    def update(self) -> None:
        """Update bullet position based on direction and speed."""
        # ERROR 1: Check the operator - should bullets move or stay still?
        self.rect.x -= self.direction[0] * self.speed  # Move bullet along X axis
        self.rect.y -= self.direction[1] * self.speed  # Move bullet along Y axis

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the bullet on the surface.
        
        Args:
            surface: Pygame surface to draw on
        """
        pygame.draw.rect(surface, self.color, self.rect)  # Draw the bullet

    def is_alive(self) -> bool:
        """
        Check if bullet is still alive (within lifetime limit).
        
        Returns:
            True if bullet is alive, False otherwise
        """
        # ERROR 2: Check the comparison operator - when should bullets expire?
        return (time.time() - self.creation_time) > 3  # Check bullet lifetime
    
# Класс способности
class Ability:
    """
    Base ability class.
    Manages bullet creation, updates, and rendering.
    """
    
    def __init__(self) -> None:
        """Initialize ability with empty bullet list."""
        self.bullets: List[Bullet] = []  # List to store bullets

    def shoot(self, x: int, y: int) -> None:
        """
        Abstract shoot method to be implemented by subclasses.
        
        Args:
            x: X coordinate to shoot from
            y: Y coordinate to shoot from
            
        Raises:
            NotImplementedError: Must be implemented in subclass
        """
        raise NotImplementedError("method 'shot' must be inside oof the class as a method")

    def update_bullets(self) -> None:
        """Update all bullets and remove expired ones."""
        # ERROR 3: Check the logic - should we keep alive or dead bullets?
        for bullet in list(self.bullets):  # Use list() to safely remove items during iteration
            bullet.update()  # Update each bullet
            if bullet.is_alive():  # Remove bullet if it exceeded its lifetime
                self.bullets.remove(bullet)

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw all active bullets on the surface.
        
        Args:
            surface: Pygame surface to draw on
        """
        for bullet in self.bullets:
            bullet.draw(surface)  # Draw each bullet

class Ability1(Ability):
    """
    Multi-directional shooting ability.
    Shoots bullets in 4 directions (up, down, left, right).
    """
    
    def shoot(self, x: int, y: int, color: Tuple[int, int, int] = (0, 255, 0), 
              size: int = 5) -> None:
        """
        Shoot bullets in 4 directions.
        
        Args:
            x: X coordinate to shoot from
            y: Y coordinate to shoot from
            color: RGB color tuple for bullets (default green)
            size: Size of bullets in pixels (default 5)
        """
        directions: List[Tuple[int, int]] = [
            (0, -1),   # Up
            (0, 1),    # Down
            (-1, 0),   # Left
            (1, 0)     # Right
        ]
        
        for direction in directions:
            bullet = Bullet(x, y, color, size, direction)  # Create bullet with given parameters
            self.bullets.append(bullet)  # Add bullet to the list

class Ability2(Ability):
    """
    Single-direction shooting ability.
    Shoots one bullet upward.
    """
    
    def shoot(self, x: int, y: int, color: Tuple[int, int, int] = (255, 0, 0), 
              size: int = 10) -> None:
        """
        Shoot a single bullet upward.
        
        Args:
            x: X coordinate to shoot from
            y: Y coordinate to shoot from
            color: RGB color tuple for bullet (default red)
            size: Size of bullet in pixels (default 10)
        """
        direction: Tuple[int, int] = (0, -1)  # Direction up
        bullet = Bullet(x, y, color, size, direction)  # Create bullet with given parameters
        self.bullets.append(bullet)  # Add bullet to the list