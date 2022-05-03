import mido

def negotiate(midi_obj):
    # Messages truck
    trk_portA = mido.MidiFile() # Port 01
    trk_portB = mido.MidiFile() # Port 02
    # Port negotiation
    try:
        for m1 in midi_obj.tracks:
            trk_tmp = []
            port = 0
            for m2 in m1:
                try:
                    port = m2.port
                except:
                    pass
            if port == 0:
                # It's Port A Track
                trk_portA.tracks.append(m1)
            elif port == 1:
                # It's Port B Track
                trk_portB.tracks.append(m1)
            else:
                pass
    except AttributeError:
        # this MIDI object has no port prefix
        # storing all tracks to port A
        for m1 in midi_obj.tracks:
            trk_portA.tracks.append(m1)
        trk_portB = None
    # set ticks per beat
    trk_portA.ticks_per_beat = midi_obj.ticks_per_beat
    try:
        trk_portB.ticks_per_beat = midi_obj.ticks_per_beat
        # set tempo value to port B (temporary)
        trk_portB.tracks.append(trk_portA.tracks[0])
    except AttributeError:
        # Single Port MIDI file, skipping
        pass
    # hey, get this
    return trk_portA, trk_portB
