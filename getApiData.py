import requests, json
from env import HERE_API_KEY, TOKEN

HEADERS={'Content-Type': 'text/html', 'Authorization':'Bearer {TOKEN}'}

# Returns jamFactor of a road
def roadJamFactor(road, name):
    HERE_URL = f'https://data.traffic.hereapi.com/v7/flow?in=corridor:{road};r=1&locationReferencing=none&apiKey={HERE_API_KEY}'
    r = requests.get(HERE_URL)
    result = json.loads(r.text)
    return result['results'][0]['currentFlow']['jamFactor']
    
    # json_result = json.dumps(result, indent=2)
    # with open(f'{name}.json', 'w') as outfile:
    #     outfile.write(json_result)
    # print(f"Jam Factor updated successfully at: ./{name}.json")


def jamFactorRoads():
    roads = {}
    with open("corridor_encodings.json", 'r') as f:
        obj = f.read()
        roads = json.loads(obj)
    
    jamFactors = {}
    for key in roads:
        jamFactors[key] = roadJamFactor(roads[key], key)
        # print(f'Getting jam factor of road: {key}')
    
    with open('jamFactors.json', 'w') as outfile:
        outfile.write(json.dumps(jamFactors))

# jamFactorRoads()