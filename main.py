from models.scene_manager import SceneManager
import pygame

pygame.init()
canvas = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(pygame.image.load("assets/favicon.ico").convert())
clock = pygame.time.Clock()

scene_manager = SceneManager(pygame)

# GAME LOOP
exit = False
while not exit:
    scene_manager.show(canvas)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            exit = True

    scene_manager.update(pygame, event_list)
    pygame.display.update()
    clock.tick(60)
