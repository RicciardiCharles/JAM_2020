import pygame, sys
from pygame_functions import *
from sitckfight import *

def settings_menu(screen, mm): 
    
    color = (231, 223, 198)    
    color_light = (222, 60, 75)
    color_dark = (98, 60, 234) 

    width = screen.get_width() 
    height = screen.get_height() 

    smallfont = pygame.font.SysFont('Corbel',55) 
    exit_but = smallfont.render('Remove Music' , True , color) 
    play_but = smallfont.render('Resume', True, color)
    sett_but = smallfont.render('Stop sounds', True, color)
    menu = 1
    while menu == 1:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 + 120 <= mouse[1] <= height / 2 + 200: 
                    mm.stop()
                if width / 2 - 120 <= mouse[0] <= width / 2 + 120 and height / 2 - 200 <= mouse[1] <= height / 2 - 120:
                    return 0
                if width / 2 - 120  <= mouse[0] <= width / 2 + 120 and height / 2 - 40 <= mouse[1] <= height / 2 + 40:
                    print ('lol')
                    no_sound = 1
        screen.fill((84, 66, 107)) 
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

        screen.blit(play_but, (width / 2 - 60, height / 2 - 175))
        screen.blit(sett_but, (width / 2 - 90, height / 2 - 15))
        screen.blit(exit_but , (width / 2 - 100, height / 2 + 145))
        pygame.display.update()

def dialogue1(screen):
    label = makeLabel("phrase pas sympa", 40, 800, 400, "blue", "Agency FB", "yellow")
    showLabel(label)
    return (label)
