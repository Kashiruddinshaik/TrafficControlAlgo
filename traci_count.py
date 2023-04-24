import traci
import json

# Connect to SUMO and get lane ID
traci.start(["sumo-gui", "-c",
            r"C:\Users\manav\Desktop\AdaptiveTrafficLightSumo\withAlgorithm\sample.sumocfg"])
lane0_0 = "E0_0"
lane0_1 = "E0_1"
lane1_0 = "E1_0"
lane1_1 = "E1_1"
lane2_0 = "E2_0"
lane2_1 = "E2_1"
lane3_0 = "E3_0"
lane3_1 = "E3_1"

remaining_vehicles = []

step = 0
while traci.simulation.getMinExpectedNumber() > 0:
    # Get number of vehicles in lane
    if step % 50 == 0:
        n0_0 = traci.lane.getLastStepVehicleNumber(lane0_0)
        n0_1 = traci.lane.getLastStepVehicleNumber(lane0_1)
        n1_0 = traci.lane.getLastStepVehicleNumber(lane1_0)
        n1_1 = traci.lane.getLastStepVehicleNumber(lane1_1)
        n2_0 = traci.lane.getLastStepVehicleNumber(lane2_0)
        n2_1 = traci.lane.getLastStepVehicleNumber(lane2_1)
        n3_0 = traci.lane.getLastStepVehicleNumber(lane3_0)
        n3_1 = traci.lane.getLastStepVehicleNumber(lane3_1)

        # Print number of vehicles in lane
        print("{} - Number of vehicles in lane {}: {}".format(step, 0, n0_0 + n0_1))
        print("{} - Number of vehicles in lane {}: {}".format(step, 1, n1_0 + n1_1))
        print("{} - Number of vehicles in lane {}: {}".format(step, 2, n2_0 + n2_1))
        print("{} - Number of vehicles in lane {}: {}".format(step, 3, n3_0 + n3_1))

        remaining_vehicles.append({"bharathiyar_road": (n0_0 + n0_1)//2,
                                  "balasundaram_road": (n1_0 + n1_1)//2, 
                                  "kattoor_road": (n2_0 + n2_1)//2, 
                                  "sarojini_naidu_road": (n3_0 + n3_1)//2})
    traci.simulationStep()
    step += 1

with open('remaining_vehicles.json', 'w') as f:
    f.write(json.dumps(remaining_vehicles))

# Close SUMO connection
# traci.close()
