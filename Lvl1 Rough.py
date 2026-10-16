"""Move the mouse over the canvas to paint animated rainbow pixels.

Install pygame with: python -m pip install pygame
"""

import colorsys
import math
import sys

try:
	import pygame
except ImportError:
	print("This animation requires pygame. Install it with: python -m pip install pygame")
	raise SystemExit(1)


pygame.init()
WIDTH, HEIGHT = 800, 600
PIXEL_SIZE = 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainbow Pixel Art — move your cursor")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

# Grid cells contain a base hue that shifts over time.
painted = {}
elapsed = 0.0


def paint(position):
	column, row = position[0] // PIXEL_SIZE, position[1] // PIXEL_SIZE
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			x, y = column + dx, row + dy
			if 0 <= x < WIDTH // PIXEL_SIZE and 0 <= y < HEIGHT // PIXEL_SIZE:
				painted[(x, y)] = (elapsed * 0.12 + math.hypot(dx, dy) * 0.08) % 1.0


running = True
while running:
	elapsed += clock.get_time() / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False
		elif event.type == pygame.MOUSEMOTION:
			paint(event.pos)
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			paint(event.pos)

	screen.fill((17, 18, 30))
	for (x, y), base_hue in painted.items():
		hue = (base_hue + elapsed * 0.16) % 1.0
		color = tuple(round(channel * 255) for channel in colorsys.hsv_to_rgb(hue, 0.9, 1.0))
		pygame.draw.rect(
			screen,
			color,
			(x * PIXEL_SIZE + 1, y * PIXEL_SIZE + 1, PIXEL_SIZE - 2, PIXEL_SIZE - 2),
		)

	hint = font.render("Move cursor to paint  |  Esc to quit", True, (220, 220, 235))
	screen.blit(hint, (14, 12))
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
