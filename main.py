import pygame
from constants import *
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable,drawable,shots)

    p = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()




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
        
        for a in asteroids:
            if a.collision(p):
                print("Game Over!")
                return
            for s in shots:
                if a.collision(s):
                    a.split()
                    s.kill()



        screen.fill((0,0,0))
        for d in drawable:   
            d.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()