import mido

def negotiate(midi_obj):
    # Messages truck
    trk_portA = mido.MidiFile() # Port 01
    trk_portB = mido.MidiFile() # Port 02
    # Port negotiation
    try:
        trb_count = 0
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
                try:
                    # Fix port prefix
                    m1.port = 1
                except:
                    pass
                trk_portB.tracks.append(m1)
                trb_count += 1
            else:
                pass
        if trb_count == 0:
            # It's Single Port SMF
            trk_portB = None
    except AttributeError:
        # this MIDI object has no port prefix (Single port SMF)
        # storing all tracks to port A
        for m1 in midi_obj.tracks:
            trk_portA.tracks.append(m1)
        trk_portB = None
    # set ticks per beat
    trk_portA.ticks_per_beat = midi_obj.ticks_per_beat
    try:
        trk_portB.ticks_per_beat = midi_obj.ticks_per_beat
        # set tempo value to port B (temporary)
        trb1 = trk_portA.tracks[0]
        trb2 = mido.MidiTrack()
        for i in trb1:
            try:
                # fix Port Prefix to prevent loss of instrument setup of Port B
                # TODO : calculate timing after SysEx Message to prevent loss of sync
                i.port = 1
            except:
                trb2.append(i)
        trk_portB.tracks.append(trb2)
    except AttributeError:
        # Single Port SMF
        trk_portB = None
    # hey, get this
    return trk_portA, trk_portB
