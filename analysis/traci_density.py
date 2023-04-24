import traci
import json

print('1')
# Connect to SUMO and get lane ID
traci.start(["sumo-gui", "-c",
            r"C:\Users\manav\Desktop\TrafficControlAlgo\Sumo_Simulations\withoutAlgorithm\sample.sumocfg"])
print('2')
lane0_0 = "E0_0"
lane0_1 = "E0_1"
lane1_0 = "E1_0"
lane1_1 = "E1_1"
lane2_0 = "E2_0"
lane2_1 = "E2_1"
lane3_0 = "E3_0"
lane3_1 = "E3_1"

density = []

step = 0
while traci.simulation.getMinExpectedNumber() > 0:
    # Get number of vehicles in lane
    if step % 30 == 0:
        n0_0 = traci.lane.getLastStepOccupancy(lane0_0)
        n0_1 = traci.lane.getLastStepOccupancy(lane0_1)
        n1_0 = traci.lane.getLastStepOccupancy(lane1_0)
        n1_1 = traci.lane.getLastStepOccupancy(lane1_1)
        n2_0 = traci.lane.getLastStepOccupancy(lane2_0)
        n2_1 = traci.lane.getLastStepOccupancy(lane2_1)
        n3_0 = traci.lane.getLastStepOccupancy(lane3_0)
        n3_1 = traci.lane.getLastStepOccupancy(lane3_1)

        # Print number of vehicles in lane
        print("{} - Density of vehicles in lane {}: {}".format(step, 0, n0_0 + n0_1))
        print("{} - Density of vehicles in lane {}: {}".format(step, 1, n1_0 + n1_1))
        print("{} - Density of vehicles in lane {}: {}".format(step, 2, n2_0 + n2_1))
        print("{} - Density of vehicles in lane {}: {}".format(step, 3, n3_0 + n3_1))

        density.append({"A": (n0_0 + n0_1),
                                  "B": (n1_0 + n1_1), 
                                  "C": (n2_0 + n2_1), 
                                  "D": (n3_0 + n3_1)})
    
    traci.simulationStep()
    step += 1

    if step == 5000:
        traci.close()
        break

with open('withoutAlgoDensity.json', 'w') as f:
    f.write(json.dumps(density))

# Close SUMO connection
# traci.close()
