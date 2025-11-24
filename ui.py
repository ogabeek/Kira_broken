import pygame
from settings import*
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character

def draw_health_and_score(display_surface: pygame.Surface, player: 'Character') -> None:
    """
    Draw player's health, score, and survival time on screen.
    
    Args:
        display_surface: Pygame surface to draw on
        player: Character object with health, score, and survival_time attributes
    """
    font = pygame.font.Font(None, 36)  # Font
    health_text = font.render(f'Health: {player.health}', True, (0, 0, 0))
    score_text = font.render(f'Score: {player.score}', True, (0, 0, 0))
    timer_text = font.render(f'Timer: {player.survival_time}', True, (0, 0, 0))
    display_surface.blit(health_text, (10, 10))  # Display health
    display_surface.blit(score_text, (10, 50))  # Display score
    display_surface.blit(timer_text, (10, 100))  # Display time

def draw_game_over(display_surface: pygame.Surface) -> None:
    """
    Draw game over screen with message.
    
    Args:
        display_surface: Pygame surface to draw on
    """
    display_surface.fill(WHITE)
    font = pygame.font.Font(None, 74)  # Font for message
    game_over_text = font.render('Dead =))', True, (255, 0, 0))  # Red color
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Center the text
    display_surface.blit(game_over_text, text_rect)  # Render the text
