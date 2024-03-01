import pygame
from sys import exit

def play_sound_effect():
    pygame.mixer.music.load('music/effect-xaropinho-rapaz.mp3')
    pygame.mixer.music.play()

pygame.init()

screen_size = (400, 400)
background_color = (255, 0, 0)
half_width = screen_size[0] // 2
half_heigth = screen_size[1] // 2

screen = pygame.display.set_mode(screen_size)
screen.fill(background_color)
pygame.display.set_caption('dont press the button')
clock = pygame.time.Clock()

button_normal = pygame.image.load('imgs/transparent_button_normal.png').convert_alpha()
button_pressed = pygame.image.load('imgs/transparent_button_pressed.png').convert_alpha()
button_shadow = pygame.image.load('imgs/transparent_button_shadow.png').convert_alpha()

is_button_pressed = False
button_normal_rect = button_normal.get_rect(center = (half_width, half_heigth))
button_pressed_rect = button_pressed.get_rect(center = (half_width, half_heigth))
button_shadow_rect = button_shadow.get_rect(center = (half_width, half_heigth))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_normal_rect.collidepoint(event.pos):
                is_button_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if button_normal_rect.collidepoint(event.pos):
                is_button_pressed = False

    screen.blit(button_shadow, button_shadow_rect)

    pygame.draw.rect(screen, background_color, button_normal_rect)

    if is_button_pressed:
        screen.blit(button_pressed, button_pressed_rect)
        play_sound_effect()
    else:
        screen.blit(button_normal, button_normal_rect)

    pygame.display.update()

    clock.tick(30)