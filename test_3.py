# raw_value test code
import time
import pygame
import pygame.midi
import sys


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(0)

# Volume
MAX = 127

# Touch Threshhold
touch = 90

# Notes of intstrument
C = 62
D = 76
E = 78
F = 79
G = 81
A = 83
B = 85
# Scales
MajorPenatonic_1 = [C, D, E, G, A]
MajorPenatonic_2 = [F, G, A, C, D]
MajorPenatonic_3 = [G, A, B, D, E]
EgyptianSuspen_1 = [D, E, G, A, C]
EgyptianSuspen_2 = [G, A, C, D, F]
EgyptianSuspen_3 = [A, B, D, E, G]


def scale():
    val = int(input("Please enter a value 1-6 to select a scale: "))
    if val == 1:
        return MajorPenatonic_1
    if val == 2:
        return MajorPenatonic_2
    if val == 3:
        return MajorPenatonic_3
    if val == 4:
        return EgyptianSuspen_1
    if val == 5:
        return EgyptianSuspen_2
    if val == 6:
        return EgyptianSuspen_3
    else:
        print("Please try again")
        scale()


def main():
    note = scale()
    # Loop until key is pressed
    while True:
        midi_out.note_on(note[2], MAX)
        time.sleep(1)
        midi_out.note_off(note[2], MAX)
        time.sleep(1)


main()