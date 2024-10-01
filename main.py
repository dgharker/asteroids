import pygame
from constants import *
import player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Player.containers = (updateable, drawable)

    p = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)




    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updateable:
            u.update(dt)

        screen.fill((0,0,0))
        for d in drawable:   
            d.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()