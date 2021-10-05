"""
This is the main moduel of the game. Running this file
runs the game.

Attributes:
    highest_score (int): the highest score achieved since
        the game started
"""
import pygame
import sys
import random
import new_player
import dug
import time
import projectile
import enemies
import spritesheet_functions as spsh
from pygame.locals import *
from constants import *
from levels import *

highest_score = 0


def level(screen, level_num, design, monster_add):
    """level is used to load level layouts and monsters

    Args:
        screen (pygame.Surface): The surface that the all
            levels and monsters will be drawn on
        level_num (int): the current level that the player
            is on
        design (dug): The group that holds the white path
            for the game
        monster_add (boolean): used to decide if monsters
            need to be added to the map
    """
    monsters = pygame.sprite.LayeredDirty()
    if level_num == 1:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(100, 300, 'bombguy'))
            monsters.add(enemies.Enemies(300, 300, 'bombguy'))
    elif level_num == 2:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        design.add_level_dirt(screen, 180, 400, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 300, 'bombguy'))
            monsters.add(enemies.Enemies(300, 300, 'bombguy'))
            monsters.add(enemies.Enemies(180, 400, 'dragon'))
    elif level_num == 3:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'bombguy'))
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'bombguy'))
    elif level_num == 4:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 180, 400, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(100, 300, 'bombguy'))
            monsters.add(enemies.Enemies(300, 300, 'bombguy'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
            monsters.add(enemies.Enemies(180, 400, 'bombguy'))
    elif level_num == 5:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'dragon'))
            monsters.add(enemies.Enemies(100, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'dragon'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
    elif level_num == 6:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 65, 300, 88, 27)
        design.add_level_dirt(screen, 300, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        design.add_level_dirt(screen, 180, 400, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'dragon'))
            monsters.add(enemies.Enemies(100, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'dragon'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
            monsters.add(enemies.Enemies(180, 400, 'bombguy'))
    elif level_num == 7:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 80, 300, 88, 27)
        design.add_level_dirt(screen, 275, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        design.add_level_dirt(screen, 120, 350, 88, 27)
        design.add_level_dirt(screen, 250, 350, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'dragon'))
            monsters.add(enemies.Enemies(100, 300, 'bombguy'))
            monsters.add(enemies.Enemies(300, 300, 'bombguy'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
            monsters.add(enemies.Enemies(120, 350, 'dragon'))
            monsters.add(enemies.Enemies(250, 350, 'dragon'))
    elif level_num == 8:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 80, 300, 88, 27)
        design.add_level_dirt(screen, 275, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        design.add_level_dirt(screen, 120, 350, 88, 27)
        design.add_level_dirt(screen, 250, 350, 88, 27)
        design.add_level_dirt(screen, 120, 250, 88, 27)
        design.add_level_dirt(screen, 250, 250, 88, 27)
        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'bombguy'))
            monsters.add(enemies.Enemies(300, 400, 'bombguy'))
            monsters.add(enemies.Enemies(100, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'dragon'))
            monsters.add(enemies.Enemies(65, 200, 'bombguy'))
            monsters.add(enemies.Enemies(300, 200, 'bombguy'))
            monsters.add(enemies.Enemies(120, 350, 'dragon'))
            monsters.add(enemies.Enemies(250, 350, 'dragon'))
            monsters.add(enemies.Enemies(120, 250, 'dragon'))
            monsters.add(enemies.Enemies(250, 250, 'bombguy'))
    elif level_num == 9:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 80, 300, 88, 27)
        design.add_level_dirt(screen, 275, 300, 88, 27)
        design.add_level_dirt(screen, 65, 200, 88, 27)
        design.add_level_dirt(screen, 300, 200, 88, 27)
        design.add_level_dirt(screen, 65, 400, 88, 27)
        design.add_level_dirt(screen, 300, 400, 88, 27)
        design.add_level_dirt(screen, 120, 350, 88, 27)
        design.add_level_dirt(screen, 250, 350, 88, 27)
        design.add_level_dirt(screen, 120, 250, 88, 27)
        design.add_level_dirt(screen, 250, 250, 88, 27)
        design.add_level_dirt(screen, 50, 450, 350, 27)
        design.add_level_dirt(screen, 13, 122, 27, 355)
        design.add_level_dirt(screen, 407, 122, 27, 355)
        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'dragon'))
            monsters.add(enemies.Enemies(100, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'dragon'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
            monsters.add(enemies.Enemies(120, 350, 'dragon'))
            monsters.add(enemies.Enemies(250, 350, 'dragon'))
            monsters.add(enemies.Enemies(120, 250, 'dragon'))
            monsters.add(enemies.Enemies(250, 250, 'dragon'))
            monsters.add(enemies.Enemies(250, 450, 'dragon'))
    elif level_num == 10:
        design.add_level_dirt(screen, 0, 0, SCREEN_WIDTH, 115)
        design.add_level_dirt(screen, 60, 300, 108, 27)
        design.add_level_dirt(screen, 275, 300, 108, 27)
        design.add_level_dirt(screen, 45, 200, 108, 27)
        design.add_level_dirt(screen, 300, 200, 108, 27)
        design.add_level_dirt(screen, 45, 400, 108, 27)
        design.add_level_dirt(screen, 300, 400, 108, 27)
        design.add_level_dirt(screen, 100, 350, 108, 27)
        design.add_level_dirt(screen, 250, 350, 108, 27)
        design.add_level_dirt(screen, 100, 250, 108, 27)
        design.add_level_dirt(screen, 250, 250, 108, 27)
        design.add_level_dirt(screen, 50, 450, 350, 27)

        if monster_add:
            monsters.add(enemies.Enemies(65, 400, 'dragon'))
            monsters.add(enemies.Enemies(300, 400, 'dragon'))
            monsters.add(enemies.Enemies(100, 300, 'dragon'))
            monsters.add(enemies.Enemies(300, 300, 'dragon'))
            monsters.add(enemies.Enemies(65, 200, 'dragon'))
            monsters.add(enemies.Enemies(300, 200, 'dragon'))
            monsters.add(enemies.Enemies(120, 350, 'bombguy'))
            monsters.add(enemies.Enemies(250, 350, 'dragon'))
            monsters.add(enemies.Enemies(120, 250, 'dragon'))
            monsters.add(enemies.Enemies(250, 250, 'dragon'))
            monsters.add(enemies.Enemies(200, 450, 'dragon'))
            monsters.add(enemies.Enemies(100, 400, 'bombguy'))
            monsters.add(enemies.Enemies(360, 400, 'dragon'))
            monsters.add(enemies.Enemies(150, 300, 'dragon'))
            monsters.add(enemies.Enemies(350, 300, 'dragon'))
            monsters.add(enemies.Enemies(100, 200, 'bombguy'))
            monsters.add(enemies.Enemies(350, 200, 'dragon'))
            monsters.add(enemies.Enemies(160, 350, 'dragon'))
            monsters.add(enemies.Enemies(300, 350, 'bombguy'))
            monsters.add(enemies.Enemies(160, 250, 'dragon'))
            monsters.add(enemies.Enemies(300, 250, 'dragon'))
            monsters.add(enemies.Enemies(350, 450, 'bombguy'))
            monsters.add(enemies.Enemies(300, 450, 'bombguy'))
            monsters.add(enemies.Enemies(200, 450, 'bombguy'))
    return monsters


def start_game(start_time, player, dirt_dug):
    """Used to move the automaticall move the player

    The purpose of this is to move the player into place
        at the beginning of the game

    Args:
        start_time (float): the time that the game started
        player (NewPlayer): the main player of the game
        dirt_dug (Dug): the group holding all of the dug
            up pixels

    """
    dirt = 0
    if time.time() - start_time < 3.5:
        if player.x > 220:
            dirt = player_move(player, 'l', dirt_dug, 4)
        if player.x <= 220 and player.y < 296:
            dirt = player_move(player, 'd', dirt_dug, 4)
    return dirt


def player_move(digger, direct, dirt, digger_speed):
    """Used to move the player and create the dug path

    Args:
        digger (NewPlayer): the main player of the game
        direct (char): direction that the player is moving
        dirt (Dug): group holding the dug up pixels
        digger_speed(int): amount of pixels to move

    """
    new_dirt = 0
    if direct == 'u':
        dig_dirt = digger.move(direct, digger_speed)
        # enemy.move('u', digger_speed)
        new_dirt = dirt.add_dirt(
            SURFACE, digger.x, digger.y, digger.rect.width,
            digger.rect.height, direct, dig_dirt)
    elif direct == 'd':
        dig_dirt = digger.move(direct, digger_speed)
        # enemy.move('d', digger_speed)
        new_dirt = dirt.add_dirt(
            SURFACE, digger.x, digger.y, digger.rect.width,
            digger.rect.height, direct, dig_dirt)
    elif direct == 'l':
        dig_dirt = digger.move(direct, digger_speed)
        # enemy.move('l', digger_speed)
        new_dirt = dirt.add_dirt(
            SURFACE, digger.x, digger.y, digger.rect.width,
            digger.rect.height, direct, dig_dirt)
    elif direct == 'r':
        dig_dirt = digger.move(direct, digger_speed)
        # enemy.move('r', digger_speed)
        new_dirt = dirt.add_dirt(
            SURFACE, digger.x, digger.y, digger.rect.width,
            digger.rect.height, direct, dig_dirt)
    return new_dirt


def main():
    """The function to run the entire game

    This function create the character and call all
    necessary function to keep the game running
    """
    pygame.init()
    fps_clock = pygame.time.Clock()
    digger_speed = 5
    start = time.time()
    won = True
    # Background
    sheet = spsh.SpriteSheet('LevelBackgrounds.png')
    cur_level = 1
    bg_images = [LEVEL_ONE_BG, LEVEL_TWO_BG, LEVEL_THREE_BG, LEVEL_FOUR_BG,
                 LEVEL_FIVE_BG, LEVEL_SIX_BG, LEVEL_SEVEN_BG, LEVEL_EIGHT_BG,
                 LEVEL_NINE_BG, LEVEL_TEN_BG]
    bgimage = bg_images[cur_level - 1]
    SURFACE.blit(bgimage, (0, 0))
    pygame.display.update()

    # Creating player and dug up list
    all_sprites = pygame.sprite.LayeredDirty()
    digger = new_player.NewPlayer(400, 84)
    all_sprites.add(digger)
    player_group = pygame.sprite.LayeredDirty()
    player_group.add(digger)
    dugup = dug.Dug(SURFACE)
    dugup.draw(SURFACE)


    # Missile variables
    missile_group = pygame.sprite.LayeredDirty()
    missile_timeout = 0

    # Enemies
    monster_list = level(SURFACE, cur_level, dugup, True)
    all_sprites.add(dugup)
    all_sprites.add(monster_list)

    lives = 3
    score = 0
    total_score = 0
    monsters = len(monster_list)
    monster_hits = 0
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Conditions for movement (deleting pixels right now)
    move_left = False
    move_right = False
    move_down = False
    move_up = False
    shoot = False
    main_loop = True
    while main_loop:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            # Dectects key presses
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    move_up = True
                elif event.key == K_DOWN:
                    move_down = True
                elif event.key == K_LEFT:
                    move_left = True
                elif event.key == K_RIGHT:
                    move_right = True
                if event.key == K_SPACE:
                    if shoot:
                        active = True
                    else:
                        active = False
                    shoot = True
                    missile_timeout = time.time()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    move_up = False
                elif event.key == K_DOWN:
                    move_down = False
                elif event.key == K_LEFT:
                    move_left = False
                elif event.key == K_RIGHT:
                    move_right = False
        # Moves Objects
        new_dirt = start_game(start, digger, dugup)
        if move_up:
            new_dirt = player_move(digger, 'u', dugup, digger_speed)
        elif move_down:
            new_dirt = player_move(digger, 'd', dugup, digger_speed)
        elif move_left:
            new_dirt = player_move(digger, 'l', dugup, digger_speed)
        elif move_right:
            new_dirt = player_move(digger, 'r', dugup, digger_speed)
        # Adding dirt to all sprites
        if new_dirt != 0:
            all_sprites.add(new_dirt)
        if shoot:
            if digger.direction == 'l':
                project = projectile.Projectile(
                    digger.x - MISSILE_WIDTH,
                    digger.y + int(digger.rect.height / 2),
                    digger.direction, digger_speed, SURFACE)
            elif digger.direction == 'r':
                project = projectile.Projectile(
                    digger.x + digger.rect.width + 1,
                    digger.y + int(digger.rect.height / 2),
                    digger.direction, digger_speed, SURFACE)
            elif digger.direction == 'u':
                project = projectile.Projectile(
                    digger.x + int(digger.rect.width / 3),
                    digger.y - MISSILE_WIDTH,
                    digger.direction, digger_speed, SURFACE)
            else:  # digger.direction = 'd':
                project = projectile.Projectile(
                    digger.x + int(digger.rect.width / 3),
                    digger.y + digger.rect.height + 1,
                    digger.direction, digger_speed, SURFACE)
            missile_group.add(project)
            shoot = False
        for missile in missile_group:
            hit_bool = missile.move(SURFACE, digger_speed, monster_list)
            if time.time() - missile_timeout > 1 or hit_bool:
                missile.kill()
                missile.visible = 0
                if hit_bool:
                    monster_hits += 1
        all_sprites.add(missile_group)
        player_hit = pygame.sprite.spritecollide(
            digger, monster_list, False, pygame.sprite.collide_mask)
        monster_miss = True
        for monster in monster_list:
            all_sprites.move_to_front(monster)
            monster_miss = monster.move(SURFACE, digger_speed, digger)
            if monster.reached_end:
                lives -= 1
                if lives <= 0:
                    main_loop = False
                    won = False

        # Moving digger to the front to be seen
        if len(player_hit) > 0 or not monster_miss:
            digger.visible = 0
            digger.kill()
            main_loop = False
            won = False
        elif digger.visible == 1:
            all_sprites.move_to_front(digger)
        if len(monster_list) <= 0:
            if lives <= 0:
                main_loop = False
                won = False
            else:
                total_score += score
                cur_level += 1
                if cur_level < 10:
                    bgimage = bg_images[cur_level - 1]
                    SURFACE.blit(bgimage, (0, 0))
                    pygame.display.update()
                    main_loop = True
                    all_sprites = pygame.sprite.LayeredDirty()
                    digger = new_player.NewPlayer(400, 84)
                    all_sprites.add(digger)
                    player_group.add(digger)
                    dugup = dug.Dug(SURFACE)
                    dugup.draw(SURFACE)
                    monster_list = level(SURFACE, cur_level, dugup, True)
                    all_sprites.add(dugup)
                    all_sprites.add(monster_list)
                    monsters = len(monster_list)
                    monster_hits = 0
                    start = time.time()
                else:
                    main_loop = False
                    menu('WIN', total_score)

        # Updating sprites to be drawn
        all_sprites.clear(SURFACE, bgimage)
        all_sprites.update()
        redraw = all_sprites.draw(SURFACE)
        # SCORING
        top_bar = pygame.Surface((SCREEN_WIDTH, 70))
        top_bar.fill(WHITE)
        SURFACE.blit(top_bar, [0, 0])
        score = (len(dugup))
        score += monster_hits * (20 * cur_level)
        score_text = font.render('Score: ' + str(score), True, BLACK)
        lives_text = font.render('Chances: ' + str(lives), True, BLACK)
        total_score_text = font.render('Total Score: ' + str(total_score),
                                       True, BLACK)
        level_text = font.render('Level: ' + str(cur_level), True, BLACK)
        SURFACE.blit(score_text, [10, 10])
        SURFACE.blit(lives_text, [250, 10])
        SURFACE.blit(total_score_text, [10, 40])
        SURFACE.blit(level_text, [250, 40])
        # BACK TO UPDATES
        pygame.display.update()
        pygame.display.update(redraw)
        fps_clock.tick(FPS)
        if not main_loop:
            total_score += score
            if won:
                menu('WIN', total_score)
            else:
                menu('LOSE', total_score)


def menu(text, score):
    """The starting menu of the game.

    This menu is loaded
    when the program is initially run, when the player
    wins, and when the player looses.
    """
    pygame.init()
    fps_clock = pygame.time.Clock()
    menu_background = pygame.image.load('main_menu.png')
    global highest_score
    if score > highest_score:
        highest_score = score
    SURFACE.blit(menu_background, (0, 0))
    pygame.display.update()
    font = pygame.font.SysFont('Calibri', 25, True, False)
    score_text = font.render('Highest Score: ' + str(highest_score),
                             True, WHITE)
    if text != 'start':
        display_text = font.render('You ' + str(text) + '!', True, WHITE)
        SURFACE.blit(display_text, [150, 300])
    SURFACE.blit(score_text, [100, 420])
    menu_loop = True
    while menu_loop:
        pygame.display.update()
        fps_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
            # Dectects key presses
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    menu_loop = False
                    main()
        pygame.display.update()
        pygame.display.flip()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    menu('start', highest_score)
