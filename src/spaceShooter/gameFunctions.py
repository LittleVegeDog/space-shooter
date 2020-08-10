## @file gameFunctions.py
#  @brief General functions that are needed for the basic functionaities of the system
#  @author tasdik, Hongzhao Tan, Nishanth Raveendran, Dananjay Prabaharan

import pygame
from InGameAssets import *
from constant import *
from os import path
import gameObjects
from __init__ import screen

## @brief The method that displays the main menu of the game and keep the main menu displayed until certian activities of the user
def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0, 0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
            elif ev.key == pygame.K_i:
                instruction_page()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            draw_text(screen, "Press [I] For Instructions", 20, WIDTH/2, (HEIGHT/2)+250)
            pygame.display.update()

    # pygame.mixer.music.stop()
    ready = pygame.mixer.Sound(path.join(sound_folder, 'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
    pygame.display.update()

## @brief The method that displays the pause menu of the game and keep the pause menu displayed until certian activities of the user
def pause_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit() 
        else:
            draw_text(screen, "Press [ENTER] To Continue", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()

    #pygame.mixer.music.stop()
    ready = pygame.mixer.Sound(path.join(sound_folder,'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
    pygame.display.update()

## @brief The method that displays the instruction page of the game and keep the instruction page displayed until certian activities of the user
def instruction_page():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    instr_pict = pygame.image.load(path.join(img_dir, "instructionPage.png")).convert()
    instr_pict = pygame.transform.scale(instr_pict, (WIDTH, HEIGHT), screen)

    screen.blit(instr_pict, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                break
    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

## @brief The method that draws all of the texts that need to be displayed on the general GUI
#  @param surf The surface where the text needs to be drawn on
#  @param text The content of the text that needs to be drawn
#  @param size The size of the characters of the text that needs to be drawn with
#  @param x The x value of the point where the middile point of the drawn text needs to be placed on
#  @param y The y value of the point where the middile point of the drawn text needs to be placed on
def draw_text(surf, text, size, x, y):
    # selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    # True denotes the font to be anti-aliased
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

## @brief The method that draws the shield bar of the space shooter on the general GUI
#  @param surf The surface where the shield bar needs to be drawn on
#  @param x The x value of the point where the top left corner of the drawn shield bar needs to be placed on
#  @param x The y value of the point where the top left corner of the drawn shield bar needs to be placed on
#  @param pct The percentage value of the shield left
def draw_shield_bar(surf, x, y, pct):
    # if pct < 0:
    #     pct = 0
    pct = max(pct, 0)
    # moving them to top
    # BAR_LENGTH = 100
    # BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

## @brief The method that draws the GUI which indicates the number of the space shooter's lives left on the general GUI
#  @param x The x value of the point where the top right corner of the drawn GUI needs to be placed on
#  @param y The y value of the point where the top right corner of the drawn GUI needs to be placed on
#  @param img The image that is used for the appearance that represents a single life of the space shooter
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

## @brief The method that generates a new meteor into current state of the game
def newmob():
    mob_element = gameObjects.Mob()
    all_sprites.add(mob_element)
    mobs.add(mob_element)

## @brief The method that generates a new alien into current state of the game
def newalien():
    alien_element = gameObjects.Alien()
    all_sprites.add(alien_element)
    aliens.add(alien_element)
