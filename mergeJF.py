import json

with open('15mins_jamFactors.json', 'r') as f:
    original = json.loads(f.read())

with open('remaining_vehicles.json', 'r') as f:
    remaining = json.loads(f.read())

a = b = 0

final = []
for i in range(45):
    final.append(original[a])
    final.append(remaining[b])
    a += 1
    b += 1

with open('new_JF_list.json', 'w') as f:
    f.write(json.dumps(final))