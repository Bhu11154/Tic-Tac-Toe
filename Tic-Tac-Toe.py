import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
RED = (75,0,130)
BGCOLOR = (148,0,211)
LINECOLOR = (23, 145, 135)
LINEWIDTH = 15
BOARD_ROWS = 3
BOARD_COL = 3
RADIUS = 60
CWIDTH = 15
CCOLOR = (255,0,255)
SPACE = 55

board = np.zeros((BOARD_ROWS, BOARD_COL))
print(board)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(BGCOLOR)

pygame.draw.line(screen, LINECOLOR, (0, 200), (600, 200), LINEWIDTH)
pygame.draw.line(screen, LINECOLOR, (0, 400), (600, 400), LINEWIDTH)
pygame.draw.line(screen, LINECOLOR, (200, 0), (200, 600), LINEWIDTH)
pygame.draw.line(screen, LINECOLOR, (400, 0), (400, 600), LINEWIDTH)

player = 1
gameover = False


def mark_square(row, col, play):

    board[row][col] = play


def available(row, col):

    if board[row][col] == 0:
        return True
    else:
        return False


def draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CCOLOR, (int(row * 200 + 100), int(col * 200 + 100)), RADIUS, CWIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, RED, (row * 200 + SPACE, col * 200 + 200 - SPACE), (row * 200 + 200 - SPACE, col * 200 + SPACE), 20)
                pygame.draw.line( screen, RED, (row * 200 + SPACE , col * 200 + SPACE), (row * 200 + 200 - SPACE , col * 200 + 200 -SPACE) , 20 )

def win(play):
    for col in range(BOARD_COL):
        if board[0][col] == play and board[1][col] == play and board[2][col] == play:
            draw_horizontal_winning_line(col, play)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == play and board[row][1] == play and board[row][2] == play:
            draw_vertical_winning_line(row, play)
            return True

    if board[2][0] == play and board[1][1] == play and board[0][2] == play:
        draw_asc_diagonal(play)
        return True

    if board[0][0] == play and board[1][1] == play and board[2][2] == play:
        draw_desc_diagonal(play)
        return True

    return False


def draw_vertical_winning_line(col, play):
    posx = col * 200 + 100

    if play == 1:
       COLOU = CCOLOR
    elif play == 2:
        COLOU = RED
    pygame.draw.line( screen, COLOU, (posx, 15), (posx, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, play):
    posY = row * 200 + 100

    if play == 1:
        colo = CCOLOR
    elif play == 2:
        colo = RED

    pygame.draw.line(screen, colo, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(play):
    if play == 1:
        colo = CCOLOR
    elif play == 2:
        colo = RED

    pygame.draw.line(screen, colo, (15, HEIGHT), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(play):
    if play == 1:
        colo = CCOLOR
    elif play == 2:
        colo = RED

    pygame.draw.line(screen, colo, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(BGCOLOR)
    pygame.draw.line(screen, LINECOLOR, (0, 200), (600, 200), LINEWIDTH)
    pygame.draw.line(screen, LINECOLOR, (0, 400), (600, 400), LINEWIDTH)
    pygame.draw.line(screen, LINECOLOR, (200, 0), (200, 600), LINEWIDTH)
    pygame.draw.line(screen, LINECOLOR, (400, 0), (400, 600), LINEWIDTH)
    player = 1
    for row  in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            board[row][col] = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseX // 200)
            clicked_col = int(mouseY // 200)

            if available(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if win(player) :
                        gameover = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if win(player):
                        gameover = True
                    player = 1

                draw()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()


    pygame.display.update()