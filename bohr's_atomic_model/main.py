import math
import threading as tr
import time

import pygame

import state
from cam import main

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 14)
pygame.display.set_caption("so tuff")


def update_rings():
    while state.running:
        rings = 0
        for n in range(1, 100):
            if state.ELECTRONS <= 2 * n**2:
                rings = n
                break

        state.RINGS = max(0, rings)
        time.sleep(1)


ring_thread = tr.Thread(target=update_rings, daemon=True)
ring_thread.start()

cam_thread = tr.Thread(target=main, daemon=True)
cam_thread.start()

while state.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, [152, 186, 213], (400, 300), 48, width=1)

    to_fill = state.ELECTRONS

    for i in range(1, state.RINGS + 1):
        pygame.draw.circle(screen, [255, 255, 255], (400, 300), 48 + i * 48, width=1)
        if to_fill > 0:
            for j in range(1, (2 * (i**2) + 1)):
                x = 400 + (48 + i * 48) * math.cos(math.radians(360 / j))
                y = 300 + (48 + i * 48) * math.sin(math.radians(360 / j))

                to_fill -= 1

                if (to_fill) >= 0:
                    pygame.draw.circle(screen, [255, 197, 211], (x, y), radius=7)
                else:
                    break

    p_text = font.render(f"p = {state.PROTONS}", True, (255, 255, 255))
    n_text = font.render(f"n = {state.NEUTRONS}", True, (255, 255, 255))
    screen.blit(p_text, p_text.get_rect(center=(400, 290)))
    screen.blit(n_text, n_text.get_rect(center=(400, 310)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
