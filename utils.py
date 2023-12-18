import pygame
import os
import random
import time
from pygame import mixer

# Buttons zeichnen, deren Koordinaten im main.py definiert sind
def draw_buttons(buttons, window, color):
    for button in buttons:
        pygame.draw.rect(window, color, button)

# Lade alle Pianosounds in den Ordner
def pick_sound():
    # leere Liste erstellen um die Piano Sounds aufzubewahren
    piano_sounds = []

    # Weg zum Ordner "Piano sounds"
    folder_path = "piano_sounds"

    # Schleife durch alle Dateien im Ordner
    for file_name in os.listdir(folder_path):
        # checken, ob die Datei ein Piano Sound als .mid Datei ist
        if file_name.endswith(".mid"):
            # Datei zur Liste hinzufügen
            sound_path = os.path.join(folder_path, file_name)
            # Piano sound zur Liste von Piano Sounds hinzufügen
            piano_sounds.append(sound_path)

    # sicherstellen, dass die Reihenfolge der Liste stimmt
    piano_sounds = sorted(piano_sounds)

    return piano_sounds

# Eine Liste mit 12 Buttons kreieren, zu Beginn sind alle Buttons falsch (nur einer darf ja richtig sein)
# Wenn ein Sound gespielt wird, wird der entsprechende Button als "True" abgespeichert
def correct_values():
    # leere Liste erstellen um die Buttons aufzubewahren
    correct_values = []

    for value in range(0, 12):
        #Alle Buttons werden als "False" gesetzt
        correct_values.append(False)
    
    return correct_values


# Play the piano sound
def play_sounds(piano_sounds, correct_button):
    # Zufällige Basisnote wird gesetzt (aber nur von 0-25!sonst geht Intervall über die Liste hinaus)
    first_note_number = random.randint(0, 25)

    # erste Note (= Basisnote) aus der Liste der Piano Sounds holen
    first_note = piano_sounds[first_note_number]

    # die erste Note spielen
    mixer.music.load(first_note)
    mixer.music.set_volume(1)
    mixer.music.play()

    # 2 Sekunden warten
    time.sleep(2)

    # zufällig eine zweite Note auswählen, diese wird durch Intervall definiert
    interval = random.randint(1, 12)
    print (interval) #so kann man die Lösung sehen

    # den richtigen Button als "True" abspeichern
    correct_button[interval -1] = True 

    second_note_number = first_note_number + interval # das Interval zur ersten Note hinzufügen

    second_note = piano_sounds[second_note_number] # die zweite Note von der Liste der Piano Sounds holen


    # die zweite Note abspielen
    mixer.music.load(second_note)
    mixer.music.set_volume(1)
    mixer.music.play()

    # den korrekten Button dem Spiel bekanntgeben
    return correct_button

# den Hintergrund (je nach gedrücktem Button) wechseln
def draw_result(window, background_win_lose, background_sound, text_surface, text_rect):
    # wenn der richtige Button gedrückt wird -> main.py wechselt Hintergrund zu "thumbs up"
    # sonst: "thumbsdown"
    
    window.blit(background_win_lose, (0,0))
    window.blit(text_surface, text_rect)
    pygame.display.flip()
    
    # 1 Sekunde warten, bevor der Spieler das Resultat weiss
    time.sleep(1)

    # Hintergrund ändern 
    
    window.blit(background_sound, (0,0))
    # window.blit(text_surface, text_rect)
    pygame.display.flip()

    time.sleep(1)

