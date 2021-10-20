# Author:
#              Mathew Tucker
# Date:
#              16OCT21
# Description:
#              The following code allows
#              the user to trigger musical
#              notes via signals captured
#              Adafruit's Touch Capacitive
#              Hat.


def scale():

	# Notes of intstrument
	C = 62
	D = 76
	E = 78
	F = 79
	G = 81
	A = 83
	B = 85
	# Scales
	MajorPenatonic_1 = [C,D,E,G,A]
	MajorPenatonic_2 = [F,G,A,C,D]
	MajorPenatonic_3 = [G,A,B,D,E]
	EgyptianSuspen_1 = [D,E,G,A,C]
	EgyptianSuspen_2 = [G,A,C,D,F]
	EgyptianSuspen_3 = [A,B,D,E,G]
	
    val = 4#int(input("Please enter a value 1-6 to select a scale: "))
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
        
# Each the leads each shoot of the bamboo plant
# is conntected to
shoots = [1, 4, 7, 9, 11]

def play(midi_out, inst):
    
    import board
    import busio
    import adafruit_mpr121
    import pygame
    import pygame.midi
    import sys
    import time
    
    # Create I2C bus.
    i2c = busio.I2C(board.SCL, board.SDA)
    # Create MPR121 object.
    mpr121 = adafruit_mpr121.MPR121(i2c)
    
   
    
    note=scale()
    midi_out.set_instrument(inst)
    
    # Volume
    MAX = 127
    # Touch Threshhold
    touch = [0,1,2,3,4]
    j=0
    for i in shoots:
        touch[j]= 90#0.75*mpr121[i].raw_value
        j=j+1
    
    # The Try-Except block allows the user to break the while-loop with CTRL+C and
    # change the instrument from the default- Grand Piano(0)
    try:
        # Loop until CTRL+C is pressed
        while True:
            # Loop through each lead (1,4,7,9,11).
            for i in shoots:
                if mpr121[i].raw_value:
                    print('pin ' + str(i) + ': ' + str(mpr121[i].raw_value))
            if mpr121[1].raw_value<touch[0]:
                #Play note
                midi_out.note_on(note[4],MAX)
                print("playing note 4")
            else:
                #Stop note
                midi_out.note_off(note[4],MAX)
            if mpr121[4].raw_value<touch[1]:
                #Play note
                midi_out.note_on(note[2],MAX)
                print("playing note 2")
            else:
                #Stop note
                midi_out.note_off(note[2],MAX)
            if mpr121[7].raw_value<touch[2]:
                #Play note
                midi_out.note_on(note[1],MAX)
                print("playing note 1")
            else:
                #Stop note
                midi_out.note_off(note[1],MAX)
            if mpr121[9].raw_value<touch[3]:
                #Play note
                midi_out.note_on(note[3],MAX)
                print("playing note 3")
            else:
                #Stop note
                midi_out.note_off(note[3],MAX)
            if mpr121[11].raw_value<touch[4]:
                #Play note
                midi_out.note_on(note[0],MAX)
                print("playing note 0")
            else:
                #Stop note
                midi_out.note_off(note[0],MAX)
            time.sleep(1)
    except KeyboardInterrupt:
        inst = int(input("Please enter a value from 0-127: "))
        play(midi_out, inst)


import pygame
import pygame.midi
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
#print(port)
midi_out = pygame.midi.Output(3, 0)
#print(pygame.midi.get_device_info(port))

inst = 1

play(midi_out, inst)