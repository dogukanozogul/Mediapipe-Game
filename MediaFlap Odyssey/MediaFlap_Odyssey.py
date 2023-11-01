import cv2
import mediapipe as mp
import autopy
import math
import time
import sys
import pygame
from pygame.locals import *
import tkinter as tk
from button import Button
from random import randint

root = tk.Tk()
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.destroy()

screen = pygame.display.set_mode((screen_width, screen_height))

general_font_size = 75
title_font_size = 100
score_font_size = 50

menu_text_pos_x, menu_text_pos_y = (screen_width/2), (4*title_font_size/3)
menu_buttons_pos_x, play_button_pos_y, options_button_pos_y, quit_button_pos_y = (screen_width/2), ((4*title_font_size/3) + (4*general_font_size/3) + 50), ((4*title_font_size/3) + 2*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 3*((4*general_font_size/3) + 50))

options_text_pos_x, options_text_pos_y = (screen_width/2), (4*title_font_size/3)
option_back_button_pos_x, minus_buttons_pos_x, plus_buttons_pos_x, music_text_pos_y, music_buttons_pos_y, sfx_text_pos_y, sfx_buttons_pos_y, option_back_button_pos_y = (screen_width/2), (screen_width/2)-150, (screen_width/2)+150, ((4*title_font_size/3) + (4*general_font_size/3) + 50), ((4*title_font_size/3) + 2*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 3*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 4*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 5*((4*general_font_size/3) + 50))
option_rects_pos_x, music_rect_pos_y, sfx_rect_pos_y = ((screen_width/2) - 180), ((4*title_font_size/3) + 115), ((4*title_font_size/3) + 415)
sound_rect_width, sound_rect_height = 24, 24

play_menu_text_pos_x, play_menu_text_pos_y = (screen_width/2), (4*title_font_size/3)
play_menu_buttons_pos_x, player_pos_y, recreate_button_pos_y, start_button_pos_y, play_back_button_pos_y = (screen_width/2), ((4*title_font_size/3) + (4*general_font_size/3) + 50), ((4*title_font_size/3) + 2*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 3*((4*general_font_size/3) + 50)), ((4*title_font_size/3) + 4*((4*general_font_size/3) + 50))

quit_menu_rect_width, quit_menu_rect_height = 700, 220
quit_menu_rect_pos_x, quit_menu_rect_pos_y = (screen_width/2)-(quit_menu_rect_width/2) , (screen_height/2)-(quit_menu_rect_height/2)
quit_text_pos_x, quit_text_pos_y = (screen_width/2), (screen_height/2)-(quit_menu_rect_height/2)+((4*general_font_size/3)/2)
quit_yes_pos_x, quit_no_pos_x, quit_buttons_pos_y = (screen_width/2)-(quit_menu_rect_width/4), (screen_width/2)+(quit_menu_rect_width/4), (screen_height/2)+(quit_menu_rect_height/2)-((4*general_font_size/3)/2)

quitm_menu_rect_width, quitm_menu_rect_height = 800, 220
quitm_menu_rect_pos_x, quitm_menu_rect_pos_y = (screen_width/2)-(quitm_menu_rect_width/2) , (screen_height/2)-(quitm_menu_rect_height/2)
quitm_text_pos_x, quitm_text_pos_y = (screen_width/2), (screen_height/2)-(quitm_menu_rect_height/2)+((4*general_font_size/3)/2)
quitm_yes_pos_x, quitm_no_pos_x, quitm_buttons_pos_y = (screen_width/2)-(quitm_menu_rect_width/4), (screen_width/2)+(quitm_menu_rect_width/4), (screen_height/2)+(quitm_menu_rect_height/2)-((4*general_font_size/3)/2)

play_again_rect_width, play_again_rect_height = 500, 220
play_again_rect_pos_x, play_again_rect_pos_y = (screen_width/2)-(play_again_rect_width/2) , (screen_height/2)-(play_again_rect_height/2)
play_again_pos_x, play_again_pos_y = (screen_width/2), (screen_height/2)-(play_again_rect_height/2)+((4*general_font_size/3)/2)
play_again_yes_pos_x, play_again_no_pos_x, play_again_buttons_pos_y = (screen_width/2)-(play_again_rect_width/4), (screen_width/2)+(play_again_rect_width/4), (screen_height/2)+(play_again_rect_height/2)-((4*general_font_size/3)/2)

score_text_pos_x, score_text_pos_y = screen_width - 100 , (4*score_font_size/3)

player_width, player_height = 96, 54
obstacle_width = 100
base_top_height = 100

game_images = {}
game_sounds = {}

player = 'assets/imgs/player.png'
background = 'assets/imgs/background.jpg'
game_background = 'assets/imgs/game_bg.jpg'
menu_rect = 'assets/imgs/menu_rect.png'
base_top = 'assets/imgs/black.png'
obstacle = 'assets/imgs/black.png'
sound_rect = 'assets/imgs/white2.png'

pygame.init()
pygame.display.set_caption('MediaFlap Odyssey')

game_images['base_top'] = pygame.transform.scale(pygame.image.load(base_top).convert_alpha(), (screen_width, base_top_height))
game_images['background'] = pygame.transform.scale(pygame.image.load(background).convert_alpha(), (screen_width, screen_height))
game_images['game_background'] = pygame.transform.scale(pygame.image.load(game_background).convert_alpha(), (screen_width, screen_height))
game_images['player'] = pygame.transform.scale(pygame.image.load(player).convert_alpha(), (player_width , player_height))
game_images['obstacle'] = pygame.transform.scale(pygame.image.load(obstacle), (obstacle_width, 400))
game_images['menu_rect'] = pygame.image.load(menu_rect).convert_alpha()
game_images['big_menu_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (500, 110))
game_images['option_menu_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (360, 220))
game_images['big_option_menu_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (500, 220))
game_images['quit_menu_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (quit_menu_rect_width, quit_menu_rect_height))
game_images['quitm_menu_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (quitm_menu_rect_width, quitm_menu_rect_height))
game_images['play_again_rect'] = pygame.transform.scale(pygame.image.load(menu_rect).convert_alpha(), (play_again_rect_width, play_again_rect_height))

for i in range(10):
    game_images['sound_rect' + str(i)] = pygame.transform.scale(pygame.image.load(sound_rect).convert_alpha(), (sound_rect_width, sound_rect_height))
    sound_rect_height += 9


game_sounds['click'] = pygame.mixer.Sound('assets/mscs/click.mp3')
game_sounds['hit'] = pygame.mixer.Sound('assets/mscs/hit.mp3')
game_sounds['select'] = pygame.mixer.Sound('assets/mscs/select.mp3')
main_menu_soundtrack = 'assets/mscs/main_menu_soundtrack.mp3'
game_soundtrack = 'assets/mscs/game_soundtrack.mp3'

pygame.mouse.set_visible(False)

hands = mp.solutions.hands
hands_mesh = hands.Hands(static_image_mode=False, min_detection_confidence=0.8,min_tracking_confidence=0.8)

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

draw = mp.solutions.drawing_utils

finger_status = [False, False, False]
old_finger_status = [False, False, False]

cap = cv2.VideoCapture(0)

def get_font(size):
    return pygame.font.Font("assets/font.TTF", size)

def get_obstacles_heights(obstacle_count):

    player_gap_size_min = (5 * player_height) - (5 * obstacle_count)
    player_gap_size_max = (6 * player_height) - (5 * obstacle_count)

    if player_gap_size_min < 100:
        player_gap_size_min = 100
    if player_gap_size_max < 150:
        player_gap_size_max = 150

    player_gap_size = randint(player_gap_size_min, player_gap_size_max)

    remained_screen_height = screen_height - player_gap_size - (2 * base_top_height)

    upper_obstacle_height = randint(50, remained_screen_height - 50)

    lower_obstacle_height = remained_screen_height - upper_obstacle_height

    obstacle_count += 1

    return upper_obstacle_height, lower_obstacle_height, obstacle_count

def obstacle_collision_check(player_x, player_y, upper_obstacle_height, lower_obstacle_pos_y, obstacle_x_pos):
    player_bottom = player_y + (player_height / 2)
    player_top = player_y - (player_height / 2)

    player_right = player_x + (player_width / 2)
    player_left = player_x - (player_width / 2)

    obstacle_left = obstacle_x_pos
    obstacle_right = obstacle_x_pos + obstacle_width

    gap_bottom = lower_obstacle_pos_y
    gap_top = base_top_height + upper_obstacle_height

    if ((player_right >= obstacle_left) and (player_left <= obstacle_right)) and ((player_bottom >= gap_bottom) or (player_top <= gap_top)):
        return True
    return False

def play_again():
    click_time = time.time()

    while True:
        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results2 = hands_mesh.process(rgb)

        if results2.multi_hand_landmarks:
            for i in results2.multi_hand_landmarks:
                wrist = i.landmark[0]
                thumb = i.landmark[4]
                finger_result = []
                for j in range(5, 14, 4):
                    result = math.sqrt(((int(abs(i.landmark[j + 3].x * 640 - i.landmark[j].x * 640))) ** 2) + (
                                (int(abs(i.landmark[j + 3].y * 480 - i.landmark[j].y * 480))) ** 2))
                    finger_result.append(result)
                break_point = 0.80 * math.sqrt(((int(abs(i.landmark[17].x * 640 - i.landmark[5].x * 640))) ** 2) + (
                            (int(abs(i.landmark[17].y * 480 - i.landmark[5].y * 480))) ** 2))
                click_result = math.sqrt(((int(abs(thumb.x * 640 - wrist.x * 640))) ** 2) + ((int(abs(thumb.y * 480 - wrist.y * 480))) ** 2))
                draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)  ##

                for k in range(len(finger_result)):
                    if (finger_result[k] >= break_point) and finger_status[k] == False:
                        finger_status[k] = True
                    elif (finger_result[k] < break_point) and finger_status[k] == True:
                        finger_status[k] = False

                if finger_status == [True, False, False]:
                    autopy.mouse.move(play_again_yes_pos_x, play_again_buttons_pos_y)
                elif finger_status == [True, True, False]:
                    autopy.mouse.move(play_again_no_pos_x, play_again_buttons_pos_y)

                if (click_result >= (2.3 * break_point)) and ((time.time() - click_time) >= 0.3):
                    autopy.mouse.click()

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(game_images['play_again_rect'], (play_again_rect_pos_x, play_again_rect_pos_y))

        play_again_text = get_font(general_font_size).render("PLAY AGAIN?", True, "#ff0000")
        play_again_rect = play_again_text.get_rect(center=(play_again_pos_x, play_again_pos_y))
        screen.blit(play_again_text, play_again_rect)

        play_again_yes = Button(image=None, pos=(play_again_yes_pos_x, play_again_buttons_pos_y), text_input="YES",
                          font=get_font(general_font_size), base_color="White", hovering_color="Red",
                          interaction_image=None)
        play_again_no = Button(image=None, pos=(play_again_no_pos_x, play_again_buttons_pos_y), text_input="NO",
                         font=get_font(general_font_size), base_color="White", hovering_color="Red",
                         interaction_image=None)

        for button in [play_again_yes, play_again_no]:
            button.buttonInteraction(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_yes.checkForInput(mouse_pos):
                    game_sounds['click'].play()
                    play_game()

                elif play_again_no.checkForInput(mouse_pos):
                    game_sounds['click'].play()
                    Main_Menu(True)

        pygame.display.update()

def quit_to_main_menu():
    stop = False

    click_time = time.time()

    while True:
        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results2 = hands_mesh.process(rgb)

        if results2.multi_hand_landmarks:
            for i in results2.multi_hand_landmarks:
                wrist = i.landmark[0]
                thumb = i.landmark[4]
                finger_result = []
                for j in range(5, 14, 4):
                    result = math.sqrt(((int(abs(i.landmark[j + 3].x * 640 - i.landmark[j].x * 640))) ** 2) + (
                                (int(abs(i.landmark[j + 3].y * 480 - i.landmark[j].y * 480))) ** 2))
                    finger_result.append(result)
                break_point = 0.80 * math.sqrt(((int(abs(i.landmark[17].x * 640 - i.landmark[5].x * 640))) ** 2) + (
                            (int(abs(i.landmark[17].y * 480 - i.landmark[5].y * 480))) ** 2))
                click_result = math.sqrt(
                    ((int(abs(thumb.x * 640 - wrist.x * 640))) ** 2) + ((int(abs(thumb.y * 480 - wrist.y * 480))) ** 2))
                draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)  ##

                for k in range(len(finger_result)):
                    if (finger_result[k] >= break_point) and finger_status[k] == False:
                        finger_status[k] = True
                    elif (finger_result[k] < break_point) and finger_status[k] == True:
                        finger_status[k] = False

                if finger_status == [True, False, False]:
                    autopy.mouse.move(quitm_yes_pos_x, quitm_buttons_pos_y)
                elif finger_status == [True, True, False]:
                    autopy.mouse.move(quitm_no_pos_x, quitm_buttons_pos_y)

                if (click_result >= (2.3 * break_point)) and ((time.time() - click_time) >= 0.3):
                    autopy.mouse.click()

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(game_images['quitm_menu_rect'], (quitm_menu_rect_pos_x, quitm_menu_rect_pos_y))

        quitm_text = get_font(general_font_size).render("QUIT to MAIN MENU?", True, "#ff0000")
        quitm_rect = quitm_text.get_rect(center=(quitm_text_pos_x, quitm_text_pos_y))
        screen.blit(quitm_text, quitm_rect)

        quitm_yes = Button(image=None, pos=(quitm_yes_pos_x, quitm_buttons_pos_y), text_input="YES",
                          font=get_font(general_font_size), base_color="White", hovering_color="Red",
                          interaction_image=None)
        quitm_no = Button(image=None, pos=(quitm_no_pos_x, quitm_buttons_pos_y), text_input="NO",
                         font=get_font(general_font_size), base_color="White", hovering_color="Red",
                         interaction_image=None)

        for button in [quitm_yes, quitm_no]:
            button.buttonInteraction(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitm_yes.checkForInput(mouse_pos):
                    game_sounds['click'].play()
                    Main_Menu(True)
                elif quitm_no.checkForInput(mouse_pos):
                    game_sounds['click'].play()
                    stop = True
        if stop:
            break

        pygame.display.update()

def play_game():
    pygame.mixer.music.load(game_soundtrack)
    pygame.mixer.music.play(-1)

    score = 0

    start_time = time.time()

    player_x = (screen_width / 8) - (player_width / 2)
    player_y = (screen_height / 2) - (player_height / 2)

    upper_obstacles_heights = []
    lower_obstacles_pos_y = []
    obstacles_pos_x = []

    obstacle_count = 0

    for i in range(100):
        if i > 0:
            x_gap_min = (5 * player_width) - (5 * obstacle_count)
            x_gap_max = (6 * player_width) - (5 * obstacle_count)

            if x_gap_min < 250:
                x_gap_min = 250
            if x_gap_max < 400:
                x_gap_max = 400

            x_gap = randint(x_gap_min, x_gap_max)

            obstacle_pos_x = randint((obstacles_pos_x[i - 1] + x_gap), (obstacles_pos_x[i - 1] + (2 * x_gap)))
        else:
            obstacle_pos_x = randint((screen_width / 4), (screen_width / 2))


        upper_obstacle_height, lower_obstacle_height, obstacle_count = get_obstacles_heights(obstacle_count)

        game_images['upper_obstacle' + str(i)] = pygame.transform.scale(pygame.image.load(obstacle), (obstacle_width, upper_obstacle_height))
        game_images['lower_obstacle' + str(i)] = pygame.transform.scale(pygame.image.load(obstacle), (obstacle_width, lower_obstacle_height))

        upper_obstacles_heights.append(upper_obstacle_height)
        lower_obstacles_pos_y.append(screen_height - lower_obstacle_height - base_top_height)
        obstacles_pos_x.append(obstacle_pos_x)

    obstacles_vel_x = -1
    player_vel_x = 0.1

    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(game_images['game_background'], (0, 0))

        screen.blit(game_images['base_top'], (0, 0))
        screen.blit(game_images['base_top'], (0, screen_height - base_top_height))


        for i in range(4):
            score_text = get_font(score_font_size).render(str(score), True, "#ff0000")
            score_rect = score_text.get_rect(center=(score_text_pos_x, score_text_pos_y))
            screen.blit(score_text, score_rect)
            score = int(time.time() - start_time)

            obstacles_vel_x = ((-0.02) * score) - 1
            if obstacles_vel_x < -10:
                obstacles_vel_x = -10

            for i in range(len(obstacles_pos_x)):
                if (obstacles_pos_x[i] + obstacle_width) >= (player_x) and (obstacles_pos_x[i]) - (
                        player_x + (player_width)) <= 1:
                    if obstacle_collision_check(player_x + (player_width / 2), player_y + (player_height / 2),
                                                upper_obstacles_heights[i], lower_obstacles_pos_y[i],
                                                obstacles_pos_x[i]):
                        obstacles_vel_x = 0
                        player_vel_x = 0
                        game_sounds['hit'].play()
                        play_again()

            player_y = mouse_pos[1] - (player_height / 2)

            if (((player_y + player_height) >= (screen_height - base_top_height)) or (player_y <= base_top_height)):
                obstacles_vel_x = 0
                player_vel_x = 0
                pa_text = get_font(score_font_size).render("Play again!", True, "#ff0000")
                pa_rect = pa_text.get_rect(center=(screen_width / 2, screen_height / 2))
                screen.blit(pa_text, pa_rect)

            for i in range(len(obstacles_pos_x)):
                obstacles_pos_x[i] += obstacles_vel_x

            if (player_x + (player_width / 2)) <= (screen_width / 2):
                player_x += player_vel_x

            for i in range(len(obstacles_pos_x)):
                screen.blit(game_images['upper_obstacle' + str(i)], (obstacles_pos_x[i], base_top_height))
                screen.blit(game_images['lower_obstacle' + str(i)], (obstacles_pos_x[i], lower_obstacles_pos_y[i]))

            screen.blit(game_images['player'], (player_x, player_y))
            ##score, player_x, player_y, obstacles_pos_x, obstacles_vel_x, player_vel_x = test(score, start_time, player_x, player_y, obstacles_pos_x, lower_obstacles_pos_y, upper_obstacles_heights, obstacles_vel_x, player_vel_x, mouse_pos)

        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results1 = face_detection.process(rgb)

        if results1.detections:
            for detection in results1.detections:
                bounding_box = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bounding_box.xmin * iw), int(bounding_box.ymin * ih), int(
                    bounding_box.width * iw), int(bounding_box.height * ih)

                center_x = (x + (w // 2))
                center_y = (y + (h // 2) - 25)
                radius = ((max(w, h) // 2) + 25)

                pos_y = (1080 * (y + (h // 2))) / 640
                autopy.mouse.move(1920 / 2, pos_y)

        for i in range(4):
            score_text = get_font(score_font_size).render(str(score), True, "#ff0000")
            score_rect = score_text.get_rect(center=(score_text_pos_x, score_text_pos_y))
            screen.blit(score_text, score_rect)
            score = int(time.time() - start_time)

            obstacles_vel_x = ((-0.02) * score) - 1
            if obstacles_vel_x < -10:
                obstacles_vel_x = -10

            for i in range(len(obstacles_pos_x)):
                if (obstacles_pos_x[i] + obstacle_width) >= (player_x) and (obstacles_pos_x[i]) - (
                        player_x + (player_width)) <= 1:
                    if obstacle_collision_check(player_x + (player_width / 2), player_y + (player_height / 2),
                                                upper_obstacles_heights[i], lower_obstacles_pos_y[i],
                                                obstacles_pos_x[i]):
                        obstacles_vel_x = 0
                        player_vel_x = 0
                        game_sounds['hit'].play()
                        play_again()

            player_y = mouse_pos[1] - (player_height / 2)

            if (((player_y + player_height) >= (screen_height - base_top_height)) or (player_y <= base_top_height)):
                obstacles_vel_x = 0
                player_vel_x = 0
                pa_text = get_font(score_font_size).render("Play again!", True, "#ff0000")
                pa_rect = pa_text.get_rect(center=(screen_width / 2, screen_height / 2))
                screen.blit(pa_text, pa_rect)

            for i in range(len(obstacles_pos_x)):
                obstacles_pos_x[i] += obstacles_vel_x

            if (player_x + (player_width / 2)) <= (screen_width / 2):
                player_x += player_vel_x

            for i in range(len(obstacles_pos_x)):
                screen.blit(game_images['upper_obstacle' + str(i)], (obstacles_pos_x[i], base_top_height))
                screen.blit(game_images['lower_obstacle' + str(i)], (obstacles_pos_x[i], lower_obstacles_pos_y[i]))

            screen.blit(game_images['player'], (player_x, player_y))
            ##score, player_x, player_y, obstacles_pos_x, obstacles_vel_x, player_vel_x = test(score, start_time, player_x, player_y, obstacles_pos_x, lower_obstacles_pos_y, upper_obstacles_heights, obstacles_vel_x, player_vel_x, mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                quit_to_main_menu()

        pygame.display.update()

def options_menu():
    click_time = time.time()
    option_control = True
    music_control = False
    sfx_control = False

    music_rect_number = int(10 * pygame.mixer.music.get_volume())
    sfx_rect_number = int(10 * game_sounds['hit'].get_volume())

    while True:
        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results2 = hands_mesh.process(rgb)

        if results2.multi_hand_landmarks:
            for i in results2.multi_hand_landmarks:
                wrist = i.landmark[0]
                thumb = i.landmark[4]
                finger_result = []
                for j in range(5, 14, 4):
                    result = math.sqrt(((int(abs(i.landmark[j + 3].x * 640 - i.landmark[j].x * 640))) ** 2) + (
                                (int(abs(i.landmark[j + 3].y * 480 - i.landmark[j].y * 480))) ** 2))
                    finger_result.append(result)
                break_point = 0.80 * math.sqrt(((int(abs(i.landmark[17].x * 640 - i.landmark[5].x * 640))) ** 2) + (
                            (int(abs(i.landmark[17].y * 480 - i.landmark[5].y * 480))) ** 2))
                click_result = math.sqrt(
                    ((int(abs(thumb.x * 640 - wrist.x * 640))) ** 2) + ((int(abs(thumb.y * 480 - wrist.y * 480))) ** 2))
                draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)  ##

                for k in range(len(finger_result)):
                    if (finger_result[k] >= break_point) and finger_status[k] == False:
                        finger_status[k] = True
                    elif (finger_result[k] < break_point) and finger_status[k] == True:
                        finger_status[k] = False

                if option_control == True:
                    if finger_status == [True, False, False]:
                        autopy.mouse.move(option_back_button_pos_x, music_rect_pos_y)
                    elif finger_status == [True, True, False]:
                        autopy.mouse.move(option_back_button_pos_x, sfx_rect_pos_y)
                    elif finger_status == [True, True, True]:
                        autopy.mouse.move(option_back_button_pos_x, option_back_button_pos_y)
                elif music_control == True:
                    if finger_status == [True, False, False]:
                        autopy.mouse.move(minus_buttons_pos_x, music_buttons_pos_y)
                    elif finger_status == [True, True, False]:
                        autopy.mouse.move(plus_buttons_pos_x, music_buttons_pos_y)
                    elif finger_status == [True, True, True]:
                        autopy.mouse.move(option_back_button_pos_x, option_back_button_pos_y)
                elif sfx_control == True:
                    if finger_status == [True, False, False]:
                        autopy.mouse.move(minus_buttons_pos_x, sfx_buttons_pos_y)
                    elif finger_status == [True, True, False]:
                        autopy.mouse.move(plus_buttons_pos_x, sfx_buttons_pos_y)
                    elif finger_status == [True, True, True]:
                        autopy.mouse.move(option_back_button_pos_x, option_back_button_pos_y)

                if (click_result >= (2.3 * break_point)) and ((time.time() - click_time) >= 0.3):
                    if finger_status == [True, False, False] and option_control == True:
                        option_control = False
                        music_control = True
                    elif finger_status == [True, True, False] and option_control == True:
                        option_control = False
                        sfx_control = True
                    else:
                        autopy.mouse.click()
                        click_time = time.time()

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(game_images['background'], (0, 0))
        screen.blit(game_images['option_menu_rect'], (option_rects_pos_x, music_rect_pos_y))
        screen.blit(game_images['option_menu_rect'], (option_rects_pos_x, sfx_rect_pos_y))

        options_text = get_font(title_font_size).render("OPTIONS", True, "#ff0000")
        options_rect = options_text.get_rect(center=(options_text_pos_x, options_text_pos_y))
        screen.blit(options_text, options_rect)

        for i in range(music_rect_number):
            screen.blit(game_images['sound_rect' + str(i)], (((screen_width/2)- 126 + (i*24)), (music_buttons_pos_y - (i*9))))
        for i in range(sfx_rect_number):
            screen.blit(game_images['sound_rect' + str(i)], (((screen_width/2)- 126 + (i*24)), (sfx_buttons_pos_y - (i*9))))

        music_text = get_font(general_font_size).render("MUSIC", True, "#ff0000")
        music_rect = music_text.get_rect(center=(option_back_button_pos_x, music_text_pos_y))
        screen.blit(music_text, music_rect)

        sfx_text = get_font(general_font_size).render("SFX", True, "#ff0000")
        sfx_rect = sfx_text.get_rect(center=(option_back_button_pos_x, sfx_text_pos_y))
        screen.blit(sfx_text, sfx_rect)

        music_plus_button = Button(image=None, pos=(plus_buttons_pos_x, music_buttons_pos_y),
                              text_input="+", font=get_font(general_font_size), base_color="#ff8276",
                              hovering_color="White", interaction_image=None)

        music_minus_button = Button(image=None, pos=(minus_buttons_pos_x, music_buttons_pos_y),
                                   text_input="-", font=get_font(general_font_size), base_color="#ff8276",
                                   hovering_color="White", interaction_image=None)
        sfx_plus_button = Button(image=None, pos=(plus_buttons_pos_x, sfx_buttons_pos_y),
                            text_input="+", font=get_font(general_font_size), base_color="#ff8276",
                            hovering_color="White", interaction_image=None)
        sfx_minus_button = Button(image=None, pos=(minus_buttons_pos_x, sfx_buttons_pos_y),
                                 text_input="-", font=get_font(general_font_size), base_color="#ff8276",
                                 hovering_color="White", interaction_image=None)
        back_button = Button(image=game_images['menu_rect'], pos=(option_back_button_pos_x, option_back_button_pos_y),
                             text_input="BACK", font=get_font(general_font_size), base_color="#ff8276",
                             hovering_color="White", interaction_image=game_images['big_menu_rect'])

        for button in [music_plus_button, music_minus_button, sfx_plus_button, sfx_minus_button, back_button]:
            button.buttonInteraction(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_plus_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    if music_rect_number != 10:
                        music_rect_number +=1
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.11)
                elif music_minus_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    if music_rect_number != 0:
                        music_rect_number -=1
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.11)
                elif sfx_plus_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    if sfx_rect_number != 10:
                        sfx_rect_number +=1
                        sounds = ('hit', 'click', 'select')
                        for s in sounds:
                            game_sounds[s].set_volume(game_sounds[s].get_volume() + 0.11)
                elif sfx_minus_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    if sfx_rect_number != 0:
                        sfx_rect_number -=1
                        sounds = ('hit', 'click', 'select')
                        for s in sounds:
                            game_sounds[s].set_volume(game_sounds[s].get_volume() - 0.11)
                elif back_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    if option_control == True:
                        Main_Menu(False)
                    else:
                        option_control = True

        pygame.display.update()

def quit_menu():
    click_time = time.time()

    while True:
        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results2 = hands_mesh.process(rgb)

        if results2.multi_hand_landmarks:
            for i in results2.multi_hand_landmarks:
                wrist = i.landmark[0]
                thumb = i.landmark[4]
                finger_result = []
                for j in range(5, 14, 4):
                    result = math.sqrt(((int(abs(i.landmark[j + 3].x * 640 - i.landmark[j].x * 640))) ** 2) + (
                                (int(abs(i.landmark[j + 3].y * 480 - i.landmark[j].y * 480))) ** 2))
                    finger_result.append(result)
                break_point = 0.80 * math.sqrt(((int(abs(i.landmark[17].x * 640 - i.landmark[5].x * 640))) ** 2) + (
                            (int(abs(i.landmark[17].y * 480 - i.landmark[5].y * 480))) ** 2))
                click_result = math.sqrt(
                    ((int(abs(thumb.x * 640 - wrist.x * 640))) ** 2) + ((int(abs(thumb.y * 480 - wrist.y * 480))) ** 2))
                draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)  ##

                for k in range(len(finger_result)):
                    if (finger_result[k] >= break_point) and finger_status[k] == False:
                        finger_status[k] = True
                    elif (finger_result[k] < break_point) and finger_status[k] == True:
                        finger_status[k] = False

                if finger_status == [True, False, False]:
                    autopy.mouse.move(quit_yes_pos_x, quit_buttons_pos_y)
                elif finger_status == [True, True, False]:
                    autopy.mouse.move(quit_no_pos_x, quit_buttons_pos_y)

                if (click_result >= (2.3 * break_point)) and ((time.time() - click_time) >= 0.3):
                    autopy.mouse.click()

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(game_images['background'], (0, 0))
        screen.blit(game_images['quit_menu_rect'], (quit_menu_rect_pos_x, quit_menu_rect_pos_y))

        quit_text = get_font(general_font_size).render("QUIT to DESKTOP?", True, "#ff0000")
        quit_rect = quit_text.get_rect(center=(quit_text_pos_x, quit_text_pos_y))
        screen.blit(quit_text, quit_rect)

        quit_yes = Button(image=None, pos=(quit_yes_pos_x, quit_buttons_pos_y), text_input="YES", font=get_font(general_font_size), base_color="White", hovering_color="Red", interaction_image=None)
        quit_no = Button(image=None, pos=(quit_no_pos_x, quit_buttons_pos_y), text_input="NO", font=get_font(general_font_size), base_color="White", hovering_color="Red", interaction_image=None)

        for button in [quit_yes, quit_no]:
            button.buttonInteraction(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_yes.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    time.sleep(0.6)
                    pygame.quit()
                    sys.exit()
                elif quit_no.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    Main_Menu(False)

        pygame.display.update()

def Main_Menu(initial_music):
    if initial_music:
        pygame.mixer.music.load(main_menu_soundtrack)
        pygame.mixer.music.play(-1)
        initial_music = False

    pygame.mouse.set_pos(menu_buttons_pos_x, play_button_pos_y)
    older_mouse_pos_y = play_button_pos_y

    click_time = time.time()

    old_finger_status = [False, False, False]

    while True:
        _, frame = cap.read()

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results2 = hands_mesh.process(rgb)

        if results2.multi_hand_landmarks:
            for i in results2.multi_hand_landmarks:
                wrist = i.landmark[0]
                thumb = i.landmark[4]
                finger_result = []
                for j in range(5, 14, 4):
                    result = math.sqrt(((int(abs(i.landmark[j + 3].x * 640 - i.landmark[j].x * 640))) ** 2) + ((int(abs(i.landmark[j + 3].y * 480 - i.landmark[j].y * 480))) ** 2))
                    finger_result.append(result)
                break_point = 0.80 * math.sqrt(((int(abs(i.landmark[17].x * 640 - i.landmark[5].x * 640))) ** 2) + ((int(abs(i.landmark[17].y * 480 - i.landmark[5].y * 480))) ** 2))
                click_result = math.sqrt(((int(abs(thumb.x * 640 - wrist.x * 640))) ** 2) + ((int(abs(thumb.y * 480 - wrist.y * 480))) ** 2))
                draw.draw_landmarks(frame, i, hands.HAND_CONNECTIONS)  ##

                for k in range(len(finger_result)):
                    if (finger_result[k] >= break_point) and finger_status[k] == False:
                        finger_status[k] = True
                    elif (finger_result[k] < break_point) and finger_status[k] == True:
                        finger_status[k] = False

                if finger_status == [True, False, False]:
                    autopy.mouse.move(menu_buttons_pos_x, play_button_pos_y)
                elif finger_status == [True, True, False]:
                    autopy.mouse.move(menu_buttons_pos_x, options_button_pos_y)
                elif finger_status == [True, True, True]:
                    autopy.mouse.move(menu_buttons_pos_x, quit_button_pos_y)

                if (click_result >= (2.3*break_point)) and ((time.time() - click_time) >= 0.7):
                    autopy.mouse.click()

        screen.blit(game_images['background'], (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(title_font_size).render("MEDIAFLAP ODYSSEY", True, "#ff0000")
        menu_rect = menu_text.get_rect(center=(menu_text_pos_x, menu_text_pos_y))

        play_button = Button(image=game_images['menu_rect'], pos=(menu_buttons_pos_x, play_button_pos_y),text_input="PLAY", font=get_font(general_font_size), base_color="#ff8276", hovering_color="White", interaction_image=game_images['big_menu_rect'])
        options_button = Button(image=game_images['menu_rect'], pos=(menu_buttons_pos_x, options_button_pos_y), text_input="OPTIONS", font=get_font(general_font_size), base_color="#ff8276", hovering_color="White", interaction_image=game_images['big_menu_rect'])
        quit_button = Button(image=game_images['menu_rect'], pos=(menu_buttons_pos_x, quit_button_pos_y), text_input="QUIT", font=get_font(general_font_size), base_color="#ff8276", hovering_color="White", interaction_image=game_images['big_menu_rect'])

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            change = button.buttonInteraction(mouse_pos)
            if change and (mouse_pos[1] > older_mouse_pos_y + 55 or mouse_pos[1] < older_mouse_pos_y - 55):
                older_mouse_pos_y = mouse_pos[1]
                game_sounds['click'].play()
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                quit_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play_game()
                    game_sounds['select'].play()
                if options_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    options_menu()
                if quit_button.checkForInput(mouse_pos):
                    game_sounds['select'].play()
                    quit_menu()

        pygame.display.update()

if __name__ == "__main__":
    Main_Menu(True)