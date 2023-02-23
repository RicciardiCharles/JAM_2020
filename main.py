import pygame, sys
from pygame_functions import *
from sitckfight import *
from settings import *

pygame.init()

res = (1920, 1080)

screen = pygame.display.set_mode(res)

color = (231, 223, 198)
color_light = (222, 60, 75)
color_dark = (98, 60, 234)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel',55)
exit_but = smallfont.render('Quit :(' , True , color)
play_but = smallfont.render('Play :)', True, color)
sett_but = smallfont.render('Settings', True, color)

def main_menu():
    pygame.mixer.init()
    mm = pygame.mixer.Sound("ressources/main_menu.ogg")
    mm.play()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 + 120 <= mouse[1] <= height / 2 + 200: 
                    pygame.quit()
                if width / 2 - 120 <= mouse[0] <= width / 2 + 120 and height / 2 - 200 <= mouse[1] <= height / 2 - 120:
                    mm.stop()
                    in_game()
                if width / 2 - 120  <= mouse[0] <= width / 2 + 120 and height / 2 - 40 <= mouse[1] <= height / 2 + 40:
                    settings_menu(screen, mm)
        screen.fill((242, 132, 130))
        mouse = pygame.mouse.get_pos()
        if width / 2 - 120 <= mouse[0] <= width / 2 + 120 and height / 2 - 200 <= mouse[1] <= height / 2 - 120:
            pygame.draw.rect(screen,color_light,[width / 2 - 120,height / 2 - 200, 300, 80])
        else:
            pygame.draw.rect(screen,color_dark,[width / 2 - 120,height / 2 - 200, 300, 80])

        if width / 2 - 120  <= mouse[0] <= width / 2 + 120 and height / 2 - 40 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen,color_light,[width / 2 - 120,height / 2 - 40, 300, 80])
        else:
            pygame.draw.rect(screen,color_dark,[width / 2 - 120,height / 2 - 40, 300, 80])

        if width / 2 - 120 <= mouse[0] <= width / 2 + 120 and height / 2 + 120 <= mouse[1] <= height / 2 + 200:
            pygame.draw.rect(screen,color_light,[width / 2 - 120,height / 2 + 120, 300, 80])
        else:
            pygame.draw.rect(screen,color_dark,[width / 2 - 120,height / 2 + 120, 300, 80])

        screen.blit(play_but, (width / 2 - 30, height / 2 - 175))
        screen.blit(sett_but, (width / 2 - 30, height / 2 - 15))
        screen.blit(exit_but , (width / 2 - 30, height / 2 + 145))
        pygame.display.update()

main_menu()