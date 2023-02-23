import pygame, sys
from pygame_functions import *
from sitckfight import *

def move_backward(screen):
    stance = 0
    frame += 1
    frame2 += 1
    pos_enx -= 50
    pos_road -= 50
    changeSpriteImage(stickman, frame)
    changeSpriteImage(enemy_stick, frame2)
    if frame == 2:
        frame = 0
        frame2 = 0
    moveSprite(road, pos_road, 980, True)
    moveSprite(stickman, x, 800, True)
    moveSprite(enemy_stick, pos_enx, 800, True)
    scrollBackground(-5, 0)

def move_forward(screen):
    stance = 0
    frame += 1
    frame2 += 1
    pos_enx += 50
    pos_road += 50
    changeSpriteImage(stickman, frame)
    changeSpriteImage(enemy_stick, frame2)
    if frame == 2:
        frame = 0
        frame2 = 0
    moveSprite(road, pos_road, 980, True)
    moveSprite(stickman, x, 800, True)
    moveSprite(enemy_stick, pos_enx, 800, True)
    scrollBackground(5, 0)

def move_on_map(screen, txt, stance):
    if keyPressed("d") and txt == 0 and stance == 0:
            move_backward(screen)
    if keyPressed("q") and txt == 0 and stance == 0:
        move_forward(screen)
    elif txt == 0 and stance == 0:
        stance = 1
    if x <= 0:
        x += 30
        moveSprite(stickman, x, 800, True)
        scrollBackground(-10, 0)
    if x >= 1920:
        x -= 30
        moveSprite(stickman, x, 800, True)
        scrollBackground(10, 0)
    return stance