# =====
# MIDI Out Port Name (e.g. SC-8820:SC-8820 Part A 20:0)
out_port = ''
# Send GS Reset before playing the MIDI file?
# ※ Roland Sound Canvas needs this to play MIDI file properly.
# default = True
use_gs_reset = True
# =====

import mido
import time

# ignore this >:]
port = mido.open_output(out_port)

def play(file):
    # Actually plays MIDI file to implemented port.
    # code will be halted temporary while the file is playing.
    if use_gs_reset:
        # Execute GS Reset
        for msg in mido.MidiFile('midi/system/gsreset.mid').play():
            port.send(msg)
        # give a half second to ready
        time.sleep(.5)
    # GO!
    for msg in mido.MidiFile(file).play():
        port.send(msg)

