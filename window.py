import pygame

pygame.init()
window, surface, color, ant, ant0, direction, running = pygame.display.set_mode((
    2160, 1350), pygame.HWSURFACE | pygame.DOUBLEBUF), pygame.Surface((2160, 1350)), [(17, 17, 17, 255), (
    200, 200, 200, 255)], (1080, 675), [1080, 675], 1, True
window.fill(color[0])
while running:
    pygame.display.flip()
    window.blit(surface, (0, 0))
    n = 1 if surface.get_at(ant) == color[0] else 0
    surface.set_at(ant, color[n])
    direction = int((direction + (n - 0.5) * 2) % 4)
    ant0[direction % 2] += 1 if direction >= 2 else -1
    ant0[0],ant0[1] = ant0[0] % 2160,ant0[1] % 1350
    ant = (ant0[0], ant0[1])
    for event in pygame.event.get():running = False if event.type == pygame.QUIT else True
pygame.quit()
