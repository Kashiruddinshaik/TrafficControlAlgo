import json
from xml.dom import minidom

G1 = 'rrrrrrrrrrrrrrrrrrGGGGgg'
G2 = 'GGGGggrrrrrrrrrrrrrrrrrr'
G3 = 'rrrrrrGGGGggrrrrrrrrrrrr'
G4 = 'rrrrrrrrrrrrGGGGggrrrrrr'

Y1 = 'rrrrrrrrrrrrrrrrrryyyyyy'
Y2 = 'yyyyyyrrrrrrrrrrrrrrrrrr'
Y3 = 'rrrrrryyyyyyrrrrrrrrrrrr'
Y4 = 'rrrrrrrrrrrryyyyyyrrrrrr'

G_Light = {1: G1, 2: G2, 3: G3, 4: G4}
Y_Light = {1: Y1, 2: Y2, 3: Y3, 4: Y4}

doc = minidom.parse('TLSGenerated.xml')

with open('road_times_backup.json') as f:
    lightSequence = json.loads(f.read())

tl = doc.getElementsByTagName('tlLogic')[0]
print(tl.tagName)

for light in lightSequence:
    phase = doc.createElement('phase')
    phase.setAttribute('duration', str(light['time']))
    phase.setAttribute('state', str(G_Light[light['road']]))
    tl.appendChild(phase)

    phase = doc.createElement('phase')
    phase.setAttribute('duration', '3')
    phase.setAttribute('state', str(Y_Light[light['road']]))
    tl.appendChild(phase)

doc.writexml(open('TLSGenerated.xml', 'w'))