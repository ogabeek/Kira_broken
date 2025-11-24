import pygame
import random
import sys
import os
from pygame.locals import QUIT
from settings import*
from character import Character
from enemy import Mob
from ui import*


def main() -> None:
    """
    Main game loop function.
    Initializes pygame, loads assets, and runs the game loop.
    """
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Twillight')
    clock = pygame.time.Clock()
    
    # Load files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(script_dir, 'asset', 'bg.png')
    v_path = os.path.join(script_dir, 'asset', 'v.png')
    p_path = os.path.join(script_dir, 'asset', 'm.png')
    background_image = pygame.image.load(bg_path).convert()
    enemy_image = pygame.image.load(v_path).convert_alpha()
    player_image = pygame.image.load(p_path).convert_alpha()

    player = Character(175, 250,player_image)  
    vampires = []

    # ERROR 9: Check variable initialization - where should start_ticks be set?
    # Main game loop
    while True:
        start_ticks = 0
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Keyboard input handling
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        # ERROR 10: Check function call - are we passing the correct arguments?
        player.move(dx)
        player.survival_time = (pygame.time.get_ticks() - start_ticks) / 1000  # Time in seconds

        # Vampire spawn logic
        if random.random() < 0.02:
            vampires.append(Mob.spawn(enemy_image))
        for vampire in vampires[:]:
            vampire.move(player)
            vampire.update(player)
            # vampire.update_bullets()   # Update vampire bullets (if any)

            if not vampire.alive:
                vampires.remove(vampire)

        # Insert code here if we want to draw an object before updating the screen
        DISPLAYSURF.blit(background_image, (0, 0))
        player.update_bullets()   # Update bullets
        player.draw(DISPLAYSURF)   # Draw player and bullets
        for vampire in vampires:
            vampire.draw(DISPLAYSURF)

        # Display health and score
        draw_health_and_score(DISPLAYSURF, player)
        if not player.isAlive:
            draw_game_over(DISPLAYSURF)

        # Update the screen with the currently drawn objects
        pygame.display.update()
        clock.tick(FPS)
        # Insert code here if we want to draw an object after updating the screen

if __name__ == "__main__":
    main()
    