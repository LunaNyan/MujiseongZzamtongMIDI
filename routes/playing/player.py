import mido
import threading
import routes.playing.common as common

# Ignore that "Cannot fine reference" Warning.
# It works properly if you installed both mido and python-rtmidi.
porta = mido.open_output('SC-8820:SC-8820 Part A 20:0')
portb = mido.open_output('SC-8820:SC-8820 Part B 20:1')

def play_porta(mobj):
    for msg in mobj.play():
        porta.send(msg)

def play(file):
    # TODO : This code is temporary, and has risk of sync loss
    # to fix this, make a new player architecture that not using module function (mido.MidiFile.play)
    trks = common.negotiate(mido.MidiFile(file))
    if trks[1] != None:
        print("file is Dual-Port SMF File")
        th1 = threading.Thread(target=play_porta, args=([trks[0]]))
        th1.start()
        for msg in trks[1].play():
            portb.send(msg)
    else:
        for msg in trks[0].play():
            porta.send(msg)
