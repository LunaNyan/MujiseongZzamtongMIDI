import mido

class metadata:
    def __init__(self, name, path, charset, length, events_count, smf_type, ticks_per_beat):
        self.name = name
        self.path = path
        self.charset = charset
        self.length = length
        self.events_count = events_count
        self.smf_type = smf_type
        self.ticks_per_beat = ticks_per_beat

def get_meta(file):
    f = mido.MidiFile(file)
    name = f.tracks[0][0].name
    path = f.filename
    charset = f.charset
    length = f.length
    events_count = len(f.tracks[0])
    smf_type = f.type
    ticks_per_beat = f.ticks_per_beat
    return metadata(name, path, charset, length, events_count, smf_type, ticks_per_beat)
