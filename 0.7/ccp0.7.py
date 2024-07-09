from scamp import *
from music21 import *
import os
from chord_positioning import AABA


s = Session(tempo=120)
s.fast_forward_to_beat(4000)
piano = s.new_part("piano")

s.start_transcribing()

chord_seq = AABA()
def chords():
    for notes in chord_seq:
        piano.play_chord(notes, 1, 4)
        
print(chord_seq)
chords()
        
performance = s.stop_transcribing()

output_dir = r'FILEPATH'
os.makedirs(output_dir, exist_ok=True)

performance.to_score().export_music_xml(os.path.join(output_dir, 'Generated Tune.xml'))

score = converter.parse(r'FILEPATH')

for measure in score.parts[0].getElementsByClass('Measure'):
    for element in measure:
        if isinstance(element, chord.Chord):
            element.simplifyEnharmonics(inPlace = True)
            symbol = harmony.chordSymbolFigureFromChord(element)
            chord_symbol = harmony.ChordSymbol(symbol)
            measure.insert(element.offset, chord_symbol)
            measure.remove(element)

    for element in measure.getElementsByClass('Clef'):
        measure.remove(element)
        
score.metadata.composer = 'Generated with Chord Progression Program 0.7 written by Gabriel Sagan'

score.show()



        
    
    


