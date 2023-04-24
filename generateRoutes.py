from xml.dom import minidom
import math, random
import json

EAST = 'east'
WEST = 'west'
SOUTH = 'south'
NORTH = 'north'
edges={'east': '0', 'north': '1', 'south': '2', 'west': '3'}
DIRECTIONS = [WEST, NORTH, EAST, SOUTH]

doc = minidom.parse('generatedRoutes.rou.xml')


def getMaxVehicles(jf):
    if 1 <= jf <= 3:
        return 5
    elif 4 <= jf <= 6:
        return 10
    elif 7 <= jf <= 9:
        return 16
    else:
        return 25


def getVehicleNumbers(vehicles):
    vehicle_numbers = []
    for _ in range(3):
        if vehicles == 0:
            vehicle_numbers.append(0)
        else:
            n = random.randint(1, int(vehicles))
            vehicle_numbers.append(n)
            vehicles -= n
    return vehicle_numbers


routes = doc.getElementsByTagName('routes')[0]

with open('new_JF_list.json', 'r') as f:
    JF_RECORDING = json.loads(f.read())

flowid = 1
begin = 0
end = 100

for i in range(len(JF_RECORDING)):
    for src_dir, jf in zip(DIRECTIONS, JF_RECORDING[i].values()):
        
        vehicles = min(math.floor(2*jf), getMaxVehicles(jf))
        vehicle_numbers = getVehicleNumbers(vehicles)
        
        i = 0
        for dest_dir in DIRECTIONS:
            if src_dir == dest_dir:
                continue
            
            route_dir = src_dir+'_'+dest_dir+str(flowid)
            edge = 'E'+edges[src_dir]+' -E'+edges[dest_dir]
            
            route = doc.createElement('route')
            route.setAttribute('id', route_dir)
            route.setAttribute('edges', edge)
            routes.appendChild(route)

            flow = doc.createElement('flow')
            flow.setAttribute('id', 'cf'+str(flowid))
            flow.setAttribute('color', '1,1,0')
            flow.setAttribute('route', route_dir)
            flow.setAttribute('number', str(vehicle_numbers[i]))
            flow.setAttribute('begin', str(begin))
            flow.setAttribute('end', str(end))
            routes.appendChild(flow)

            i += 1
            flowid += 1
    begin += 50
    end += 50

        

doc.writexml(open('generatedRoutes.rou.xml', 'w'))
