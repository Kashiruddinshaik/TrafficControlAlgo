import os
import sys
import optparse

# we need to import some python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


from sumolib import checkBinary  # Checks for the binary in environ vars
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true", default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

laneid = ""

# contains TraCI control loop
def run():
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(step)

        # Get number of vehicles in lane
        num_vehicles = traci.lane.getLastStepVehicleNumber(lane_id)

        # Print number of vehicles in lane
        print("Number of vehicles in lane {}: {}".format(lane_id, num_vehicles))

        det_vehs = traci.inductionloop.getLastStepVehicleIDs("det_0")
        for veh in det_vehs:
            print(veh)
            traci.vehicle.changeLane(veh, 2, 25)
        step += 1

    traci.close()
    sys.stdout.flush()


# main entry point
if name == "main":
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "demo.sumocfg", "--tripinfo-output", "tripinfo.xml"])
    run()