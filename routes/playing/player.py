# =====
# MIDI Out Port Name (e.g. SC-8820:SC-8820 Part A 20:0)
out_port = ''
# Send GS Reset before playing the MIDI file?
# ※ Roland Sound Canvas needs this to play MIDI file properly.
# default = True
use_gs_reset = True
# =====

import mido

# ignore this >:]
port = mido.open_output(out_port)

def gsreset():
    msg = mido.Message('sysex', data=[65, 16, 66, 18, 0, 0, 127, 0, 1])
    port.send(msg)

def load(file):
    return mido.MidiFile(file)

def play(midi_obj):
    # Actually plays MIDI file to implemented port.
    # code will be halted temporary while the file is playing.
    for msg in mido.MidiFile(midi_obj).play():
        port.send(msg)
