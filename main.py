# librairies importieren
import pygame
import time
import utils
from pygame import mixer
from pygame.font import Font
 
# Hintergrundbilder laden
background_start = pygame.image.load("background/start.jpg")
background_sound = pygame.image.load("background/sound.jpg")
background_thumbsup = pygame.image.load("background/thumbsup.jpg")
background_thumbsdown = pygame.image.load("background/thumbsdown.jpg")
 
# Sounds laden (mid files)
piano_sounds = utils.pick_sound()
 
# Buttons erstellen (k2, ..., oktave) -> Buttons = Flächen, wo man draufklicken kann
correct_button = utils.correct_values()
 
# Game Screen erstellen
window_surf  = pygame.display.set_mode((800, 550)) # Breite, Höhe (px)
pygame.display.set_caption("Klicke auf das richtige Intervall.") 
 
# Buttons erstellen
# x, y, Breite, Höhe(px)
button_start = pygame.Rect(305, 232, 190, 190)
button_k2 = pygame.Rect(453, 127, 70, 70)
button_g2 = pygame.Rect(516, 194, 70, 70)
button_k3 = pygame.Rect(544, 277, 70, 70)
button_g3 = pygame.Rect(512, 366, 70, 70)
button_r4 = pygame.Rect(448, 428, 70, 70)
button_tr4 = pygame.Rect(360, 458, 70, 70)
button_r5 = pygame.Rect(271, 434, 70, 70)
button_k6 = pygame.Rect(210, 372, 70, 70)
button_g6 = pygame.Rect(195, 285, 70, 70)
button_k7 = pygame.Rect(213, 198, 70, 70)
button_g7 = pygame.Rect(269, 127, 70, 70)
button_o8 = pygame.Rect(361, 101, 70, 70)
 
# Liste mit Buttons erstellen (in der richtigen Reihenfolge der Intervalle)
buttons = [button_start, button_k2, button_g2, button_k3, button_g3, button_r4, button_tr4, button_r5, button_k6, button_g6, button_k7, button_g7, button_o8]
 
# Farbe der Buttons bestimmen (transparent, weiss war hilfreich beim Prozess)
button_color = pygame.Color(255, 255, 255, 0) # last value is the alpha value (0-128) -> 0 = transparent, 128 = opaque
 
# Initialize Pygame
pygame.init()
mixer.init()
 
# Buttons im Screen zeichnen
utils.draw_buttons(buttons, window_surf, button_color)
 
window_surf.blit(background_start, (0,0))
 
points = 0
games_played = 0
 
# Erfolgsquote
font = Font(None, 28)

 
# Main-Schleife
running = True
while running:
    quote = round((points / games_played if games_played > 0 else 1) * 100, 1)
    text = str(quote)
    text_surface = font.render(text[:-2], True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (130, 535)
    window_surf.blit(text_surface, text_rect)
    pygame.display.flip()
    #print(f"points{points} / games_played {games_played}")
 
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # schauen, ob der Start Button geklickt ist -> Sound spielen
            if buttons[0].collidepoint(event.pos):
                # wenn der Start Button gedrückt ist
                window_surf.blit(background_sound, (0,0))
                window_surf.blit(text_surface, text_rect)
                pygame.display.flip()
 
                time.sleep(1)
 
                correct_button = utils.play_sounds(piano_sounds, correct_button)
 
            # Schauen, ob der gepresste Button k2 ist -> dann schauen, ob k2 auch der korrekte Button ist
            # wenn es der korrekte Button war --> thumbsup (sonst thumbsdown)
            # Sound abspielen
            elif (buttons[1].collidepoint(event.pos)):
                if correct_button[0]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[0] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[0] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[2].collidepoint(event.pos)):
                if correct_button[1]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[1] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[1] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
           
            elif (buttons[3].collidepoint(event.pos)):
                if correct_button[2]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[2] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[2] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[4].collidepoint(event.pos)):
                if correct_button[3]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[3] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[3] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[5].collidepoint(event.pos)):
                if correct_button[4]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[4] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[4] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[6].collidepoint(event.pos)):
                if correct_button[5]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[5] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[5] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[7].collidepoint(event.pos)):
                if correct_button[6]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[6] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[6] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
 
            elif (buttons[8].collidepoint(event.pos)):
                if correct_button[7]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[7] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[7] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[9].collidepoint(event.pos)):
                if correct_button[8]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[8] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[8] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[10].collidepoint(event.pos)):
                if correct_button[9]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[9] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[9] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[11].collidepoint(event.pos)):
                if correct_button[10]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[10] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[10] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
            elif (buttons[12].collidepoint(event.pos)):
                if correct_button[11]:
                    utils.draw_result(window_surf, background_thumbsup, background_sound, text_surface, text_rect)
                    correct_button[11] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    points += 1
                    games_played += 1
                else:
                    utils.draw_result(window_surf, background_thumbsdown, background_sound, text_surface, text_rect)
                    correct_button[11] = False
                    correct_button = utils.play_sounds(piano_sounds, correct_button)
                    games_played += 1
           
 
    # Update the display
    pygame.display.flip()
 
# Quit Pygame
pygame.quit()