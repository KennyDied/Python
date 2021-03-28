import pygame
from random import randint
from math import floor
from io import BytesIO

with open("red_btn.png", "rb") as image:
    f = image.read()
    red_button_png = bytearray(f)

with open("blue_btn.png", "rb") as image:
    f = image.read()
    blue_button_png = bytearray(f)

png_size = (10, 10)
png_width, png_height = png_size
grid_size = (3, 3)
grid_width, grid_height = grid_size
screen_scale = 20
screen_size = (grid_width * screen_scale * png_width, grid_height * screen_scale * png_width)
screen_width, screen_height = screen_size


def random_grid():
    grid = []
    for i in range(grid_height):
        temp = []
        for j in range(grid_width):
            temp += [randint(0, 1)]
        grid += [temp]
    return grid


def toggle_pos(grid, mouse):
    x, y = mouse
    x = int(x)
    y = int(y)
    if 0 <= x < grid_width and 0 <= y < grid_height:
        if grid[y][x] == 1:
            grid[y][x] = 0
        else:
            grid[y][x] = 1
    return grid


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    buffer = pygame.Surface((png_width * grid_width, png_height * grid_height))
    ret = False  # если true - игра заканчивается
    grid = random_grid()
    pygame.display.set_caption("Пробел - рандомизировать, Е - редактировать")
    edit = False  # режим редактирования
    f = BytesIO(bytes(red_button_png))
    red_button_surface = pygame.image.load(f, "png")
    f = BytesIO(bytes(blue_button_png))
    blue_button_surface = pygame.image.load(f, "png")

    while not ret:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ret = True
            if event.type == pygame.MOUSEBUTTONDOWN: click = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: grid = random_grid()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e: edit = not edit

        # проверяем ввод
        if pygame.mouse.get_pressed()[0] and click:
            x, y = pygame.mouse.get_pos()
            x = floor(x / (screen_width / grid_width))
            y = floor(y / (screen_height / grid_height))
            toggle_pos(grid, (x, y))
            if not edit:
                toggle_pos(grid, (x + 1, y))
                toggle_pos(grid, (x, y + 1))
                toggle_pos(grid, (x, y - 1))
                toggle_pos(grid, (x - 1, y))
        win = 0
        for i in grid:
            if not 1 in i:
                win += 1
        if win == len(grid) and not edit:
            pygame.display.set_caption("Вы победили!")
        elif edit:
            pygame.display.set_caption("Режим редактирования")
        else:
            pygame.display.set_caption("Выключить свет")

        # заполнить текстурой
        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j] == 0:
                    buffer.blit(red_button_surface, (j * png_width, i * png_height))
                else:
                    buffer.blit(blue_button_surface, (j * png_width, i * png_height))

        scaled_screen = pygame.transform.scale(buffer, screen_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
