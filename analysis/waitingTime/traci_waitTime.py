import traci
import json

print('1')
# Connect to SUMO and get lane ID
traci.start(["sumo-gui", "-c",
            r"C:\Users\manav\Desktop\TrafficControlAlgo\Sumo_Simulations\withAlgorithm\sample.sumocfg"])
print('2')
lane0_0 = "E0_0"
lane0_1 = "E0_1"
lane1_0 = "E1_0"
lane1_1 = "E1_1"
lane2_0 = "E2_0"
lane2_1 = "E2_1"
lane3_0 = "E3_0"
lane3_1 = "E3_1"

lanes = [lane0_0, lane0_1, lane1_0, lane1_1, lane2_0, lane2_1, lane3_0, lane3_1]

waitTimes = []
step = 0
#simulation loop
while traci.simulation.getMinExpectedNumber() > 0:

    if step % 30 == 0:
        # Get the waiting time of each vehicle in each lane
        waiting_times_by_lane = {}
        for lane_id in lanes:
            waiting_times_by_lane[lane_id] = []
            for vehicle_id in traci.lane.getLastStepVehicleIDs(lane_id):
                waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
                waiting_times_by_lane[lane_id].append(waiting_time)
        
        # Calculate the average waiting time per lane
        average_waiting_time_by_lane = {}
        for lane_id, waiting_times in waiting_times_by_lane.items():
            if len(waiting_times) > 0:
                average_waiting_time_by_lane[lane_id] = sum(waiting_times) / len(waiting_times)
            else:
                average_waiting_time_by_lane[lane_id] = 0

        waitTimes.append({
            'A': average_waiting_time_by_lane['E0_0'] + average_waiting_time_by_lane['E0_1'],
            'B': average_waiting_time_by_lane['E1_0'] + average_waiting_time_by_lane['E1_1'],
            'C': average_waiting_time_by_lane['E2_0'] + average_waiting_time_by_lane['E2_1'],
            'D': average_waiting_time_by_lane['E3_0'] + average_waiting_time_by_lane['E3_1'],
        })    
    
    traci.simulationStep()
    step += 1

    if step == 5000:
        traci.close()
        break

with open('withAlgoWaiting.json', 'w') as f:
   f.write(json.dumps(waitTimes))

# Close SUMO connection
# traci.close()
