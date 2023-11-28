import pygame
import random
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("QuickSort Visualization")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 20)  # Giảm kích thước font để vừa với số

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

def draw_array(arr, colors):
    bar_width = width // len(arr)
    for i, value in enumerate(arr):
        pygame.draw.rect(screen, colors[i], (i * bar_width, height - value, bar_width, value))
        text = font.render(str(value), True, white)
        screen.blit(text, (i * bar_width + bar_width // 2 - 8, height - value - 25))

def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def reset(num_columns):
    global array, colors, sorting, current_step, time_elapsed
    array = [random.randint(50, height - 20) for _ in range(num_columns)]
    colors = [white] * len(array)
    sorting = False
    current_step = 0
    time_elapsed = 0

reset_button = pygame.Rect(20, 20, 100, 40)
num_columns = 25  # Số cột mặc định

array = [random.randint(50, height - 20) for _ in range(num_columns)]
colors = [white] * len(array)
sorting = False
current_step = 0
time_elapsed = 0
delay_time = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorting = not sorting  # Chuyển đổi trạng thái sắp xếp khi nhấn Space
            elif event.key == pygame.K_r:
                reset(num_columns)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if reset_button.collidepoint(event.pos):
                reset(num_columns)

    screen.fill(black)

    if sorting and current_step < len(array) and time_elapsed >= delay_time:
        quicksort(array, 0, current_step)
        colors = [green if i == current_step else red for i in range(len(array))]
        current_step += 1
        time_elapsed = 0

    draw_array(array, colors)

    pygame.draw.rect(screen, white, reset_button)
    text = font.render("Reset (R)", True, black)
    screen.blit(text, (30, 30))

    pygame.display.flip()
    clock.tick(144)
    time_elapsed += clock.get_rawtime()

# Đóng cửa sổ khi kết thúc
pygame.quit()
sys.exit()
