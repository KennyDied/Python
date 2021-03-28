import pygame
from random import randint
from math import floor
from io import BytesIO
from Grid import Grid
from TextInputBox import TextInputBox


with open("pics/red_btn.png", "rb") as image:
    f = image.read()
    red_button_png = bytearray(f)

with open("pics/blue_btn.png", "rb") as image:
    f = image.read()
    blue_button_png = bytearray(f)


png_size = (5, 5)
png_width, png_height = png_size


def start_window():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([600, 600])
    bg = [0, 0, 0]
    small_font = pygame.font.SysFont('Corbel', 35)
    smaller_font = pygame.font.SysFont('Corbel', 25)

    width = screen.get_width()
    height = screen.get_height()

    button = pygame.Rect(width / 2 - 85,  4 * height / 5, 170, 40)
    white_color = [255, 255, 255]

    text_description = small_font.render('Описание игры:', True, white_color)
    text_description1 = smaller_font.render('На старте игры несколько огни включены в случайном ', True, white_color)
    text_description2 = smaller_font.render('порядке.', True, white_color)
    text_description3 = smaller_font.render('Лентой на одном свете будет переключать его', True, white_color)
    text_description4 = smaller_font.render('вместе с соседними огнями.', True, white_color)
    text_description5 = smaller_font.render('Цель игры состоит в том, чтобы выключить все огни', True, white_color)
    text_description6 = smaller_font.render('на борту, но вы найдете некоторые трудности, когда', True, white_color)
    text_description7 = smaller_font.render('увидите, что окружающие огни хотят поучаствовать.', True, white_color)

    text1 = small_font.render('Размер сетки: ', True, white_color)
    text2 = small_font.render('Х', True, white_color)

    text_input_box1 = TextInputBox(230, 4 * height / 5 - 70, 30, small_font)
    text_input_box2 = TextInputBox(300, 4 * height / 5 - 70, 30, small_font)

    group = pygame.sprite.Group(text_input_box1, text_input_box2)

    while True:
        clock.tick(60)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button.collidepoint(mouse_pos):
                    new_grid = Grid(text_input_box1.text, text_input_box2.text)
                    return new_grid

        group.update(event_list)
        screen.fill(bg)
        group.draw(screen)

        text = small_font.render('Играть!', True, white_color)
        pygame.draw.rect(screen, [255, 0, 0], button)
        screen.blit(text, (width / 2 - 80, 4 * height / 5 + 3))
        screen.blit(text1, (5, 4 * height / 5 - 70))
        screen.blit(text2, (270, 4 * height / 5 - 60))
        screen.blit(text_description, (10, 30))
        screen.blit(text_description1, (10, 70))
        screen.blit(text_description2, (10, 95))
        screen.blit(text_description3, (10, 120))
        screen.blit(text_description4, (10, 145))
        screen.blit(text_description5, (10, 170))
        screen.blit(text_description6, (10, 195))
        screen.blit(text_description7, (10, 220))

        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    sys.exit


def random_grid(grid):
    grid1 = []
    for i in range(int(grid.height)):
        temp = []
        for j in range(int(grid.width)):
            temp += [randint(0, 1)]
        grid1 += [temp]
    return grid1


def toggle_pos(grid, new_grid, mouse):
    x, y = mouse
    x = int(x)
    y = int(y)
    if 0 <= x < int(new_grid.width) and 0 <= y < int(new_grid.height):
        if grid[y][x] == 1:
            grid[y][x] = 0
        else:
            grid[y][x] = 1
    return grid


def game(new_grid):
    screen_scale = 20
    grid_w = int(new_grid.width)
    grid_h = int(new_grid.height)
    screen_size = (grid_w * screen_scale * png_width, grid_h * screen_scale * png_width)
    screen_width, screen_height = screen_size
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    buffer = pygame.Surface((png_width * grid_w, png_height * grid_h))
    ret = False  # если true - игра заканчивается
    grid = random_grid(new_grid)
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: grid = random_grid(new_grid)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e: edit = not edit

        # проверяем ввод
        if pygame.mouse.get_pressed()[0] and click:
            x, y = pygame.mouse.get_pos()
            x = floor(x / (screen_width / grid_w))
            y = floor(y / (screen_height / grid_h))
            toggle_pos(grid, new_grid, (x, y))
            if not edit:
                toggle_pos(grid, new_grid, (x + 1, y))
                toggle_pos(grid, new_grid, (x, y + 1))
                toggle_pos(grid, new_grid, (x, y - 1))
                toggle_pos(grid, new_grid, (x - 1, y))
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
        for i in range(grid_h):
            for j in range(grid_w):
                if grid[i][j] == 0:
                    buffer.blit(red_button_surface, (j * png_width, i * png_height))
                else:
                    buffer.blit(blue_button_surface, (j * png_width, i * png_height))

        scaled_screen = pygame.transform.scale(buffer, screen_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()


def main():
    new_grid = start_window()
    game(new_grid)


if __name__ == "__main__":
    main()
