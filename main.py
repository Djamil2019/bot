import time
import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

pygame.init()


screen = pygame.display.set_mode((850, 150))
pygame.display.set_caption("ВАЖНОЕ СООБЩЕНИЕ")
font = pygame.font.SysFont("Lucida Console", 20)
Label = font.render("ПОЗДРАВЛЯЮ С ЗАГРУЗКОЙ ВИРУСА!", 1, (12, 140, 0, 1))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			time.sleep(0.10)
			screen = pygame.display.set_mode((850, 150))
			pygame.display.set_caption("ВАЖНОЕ СООБЩЕНИЕ")
			messagebox.showerror("Хахахахахаха!", "Бесполезно, я уже очищаю данные! :)")

	screen.fill((0, 0, 0))
	screen.blit(Label, (50, 50))

	pygame.display.update()
