## @file gameState.py
#  @brief The module for initializing, updating, and displaying the overall state of the game
#  @author tasdik, Hongzhao Tan, Nishanth Raveendran, Dananjay Prabaharan

from __future__ import division
import pygame
import random
from os import path

# assets folder

###############################
# to be placed in "constant.py" later
from __init__ import *
###############################

###############################
# to placed in "__init__.py" later
# initialize pygame and create window
from constant import *
###############################

from InGameAssets import *
# Define all game functions
from gameFunctions import *
# Define all in-game objects
import gameObjects

## @brief The method that initializes, updates, and displays the overall state of the game
def display_update_gamestate():
    ###################################################
    # Load all game images
    # ^^ draw this rect first
    player_mini_img.set_colorkey(BLACK)
###################################################


###################################################
# main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.2)  # simmered the sound down a little

###################################################

# TODO: make the game music loop over again and again. play(loops=-1) is not working
# Error :
# TypeError: play() takes no keyword arguments
# pygame.mixer.music.play()

#############################
# Game loop
    running = True
    menu_display = True
    pause_display = False
    while running:
        if menu_display:
            main_menu()
            pygame.time.wait(3000)

        # Stop menu music
            pygame.mixer.music.stop()
        # Play the gameplay music
            pygame.mixer.music.load(
                path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
            # makes the gameplay sound in an endless loop
            pygame.mixer.music.play(-1)

            menu_display = False

        # group all the sprites together for ease of update
        # all_sprite was here
            player = gameObjects.Player()
            all_sprites.add(player)

        # spawn a group of mob
            for i in range(8):  # 8 mobs
                # mob_element = Mob()
                # all_sprites.add(mob_element)
                # mobs.add(mob_element)
                newmob()

            for i in range(2):
                newalien()
        # Score board variable
            score = 0

        # For pause menu
        if pause_display:
            pause_menu()
            pygame.time.wait(3000)

        # Stop menu music
            pygame.mixer.music.stop()
        # Play the gameplay music
            pygame.mixer.music.load(
                path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
            # makes the gameplay sound in an endless loop
            pygame.mixer.music.play(-1)

            pause_display = False

    # 1 Process input/events
        # will make the loop run at the same speed all the time
        clock.tick(FPS)
        # gets all the events which have occured till now and keeps tab of them.
        for event in pygame.event.get():
            # listening for the the X button at the top
            if event.type == pygame.QUIT:
                running = False

        # Press ESC to exit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_p:
                    pause_display = True
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    # 2 Update
        all_sprites.update()
    # check if a bullet hit a mob
    # now we have a group of bullets and a group of mob
        hits1 = pygame.sprite.groupcollide(mobs, bullets, True, True)
        hits2 = pygame.sprite.groupcollide(mobs, missles, True, False)
        hits = {**hits1, **hits2}
    # now as we delete the mob element when we hit one with a bullet, we need to respawn them again
    # as there will be no mob_elements left out
        for hit in hits:
            score += 300 - hit.radius  # give different scores for hitting big and small metoers
            expl_sounds[1].play()
            expl = gameObjects.Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            #if random.random() > 0.9:
             #   pow = gameObjects.Pow(hit.rect.center)
             #   all_sprites.add(pow)
             #   powerups.add(pow)
            newmob()  # spawn a new mob

        hits1 = pygame.sprite.groupcollide(aliens, bullets, True, True)
        hits2 = pygame.sprite.groupcollide(aliens, missles, True, False)
        hits = {**hits1, **hits2}
        for hit in hits:
            score += 50 - hit.radius  # give different scores for hitting big and small metoers
            expl_sounds[0].play()
            expl = gameObjects.Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.44:
                pow = gameObjects.Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            newalien()  # spawn a new mob

    # ^^ the above loop will create the amount of mob objects which were killed spawn again
    #########################

    # check if the player collides with the mob
        # gives back a list, True makes the mob element disappear
        hits1 = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits1:
            player_die_sound.play()
            player.shield -= hit.radius
            expl = gameObjects.Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = gameObjects.Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
                player.hide()
                player.lives -= 1
                player.shield = 100


        hits2 = pygame.sprite.spritecollide(player, aliens, True, pygame.sprite.collide_circle)
        for hit in hits2:
            player_die_sound.play()
            player.shield -= hit.radius
            expl = gameObjects.Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newalien()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = gameObjects.Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
                player.hide()
                player.lives -= 1
                player.shield = 100

    # if the player hit a power up
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup(2)
            if hit.type == 'missl':
                player.powerup(3)
            if hit.type == 'rapid':
                player.powerup(4)

    # if player died and the explosion has finished, end game
        if player.lives == 0 and not death_explosion.alive():
            #running = False
            menu_display = True
            all_sprites.remove(player)
        # pygame.display.update()

    # 3 Draw/render
        screen.fill(BLACK)
    # draw the stargaze.png image
        screen.blit(background, background_rect)

        all_sprites.draw(screen)
        # 10px down from the screen
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)

    # Draw lives
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)

    # Done after drawing everything to the screen
        pygame.display.flip()

    pygame.quit()


display_update_gamestate()
