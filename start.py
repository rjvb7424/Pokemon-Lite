import pygame

FONT = pygame.font.Font(None, 36)

def start_screen(screen):
    # Draw the background of the start screen.
    wallpaper = pygame.transform.scale(
        pygame.image.load("battle sprites/wallpaper/grassland_day.png"),
        (screen.get_width(), screen.get_height())
    )
    # Add a start battle button
    button_color = (0, 255, 0)
    button_rect = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() - 100, 100, 50)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = FONT.render('Start Battle', True, (0, 0, 0))
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
    input_box1 = pygame.Rect(100, 100, 140, 32)
    input_box2 = pygame.Rect(100, 150, 140, 32)

    player_id = ''
    opponent_id = ''

    info_text = FONT.render('All 151 original Pokemons are in this application. Input two Pokemon IDs to simulate a fight.', True, (255, 255, 255))
    screen.blit(info_text, (50, 50))

    pygame.draw.rect(screen, (255, 255, 255), input_box1, 2)
    pygame.draw.rect(screen, (255, 255, 255), input_box2, 2)
    txt_surface1 = FONT.render(player_id, True, (255, 255, 255))
    txt_surface2 = FONT.render(opponent_id, True, (255, 255, 255))

    screen.blit(txt_surface1, (input_box1.x+5, input_box1.y+5))
    screen.blit(txt_surface2, (input_box2.x+5, input_box2.y+5))

    input_box1.w = max(200, txt_surface1.get_width()+10)
    input_box2.w = max(200, txt_surface2.get_width()+10)
    screen.blit(wallpaper, (0, 0))

    return player_id, opponent_id