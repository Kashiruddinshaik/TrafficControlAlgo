import json
from getApiData import jamFactorRoads
import time
import datetime

def algorithm():
    print(datetime.datetime.now().strftime('%H:%M:%S'), ": [BEGIN] Algorithm")

    with open('jamFactors.json', 'r') as f:
        roads = json.loads(f.read())

    # 4 Roads -> 1, 2, 3, 4
    # Set roadPenalty values initially for each Road
    roadPenalty = [1, 1, 1, 1]

    # jamFactor is obtained from HERE Api and lies between [0,10]
    jamFactors = []

    #for road in roads:
    #    jamFactors.append(roads[road])
    # print(jamFactors)

    # total loss value
    lossValues = [0, 0, 0, 0]
    
    # adding constants to include non internet-connected vehicles in jam factor
    alphas = [1,1,1,1]
    baseTime = 100

    while True:

        print(datetime.datetime.now().strftime('%H:%M:%S'), ': [BEGIN] Fetching jam factors of roads')
        jamFactorRoads()
        print(datetime.datetime.now().strftime('%H:%M:%S'), ": [BEGIN] Fetched jam factors of roads")
        
        # if baseTime <= 5 :
        #     baseTime = 120
        for i in range(0,4):
            alphas[i] = jamFactors[i] * 0.1
            jamFactors[i] = alphas[i] + jamFactors[i]
            jamFactors[i] = round(jamFactors[i],2)

        #calculate tot value for each lane
        #Reward value of each road
        reward1 = round(roadPenalty[0]*jamFactors[0],2) #4  #8  #24
        reward2 = round(roadPenalty[1]*jamFactors[1],2) #3  #6  #18
        reward3 = round(roadPenalty[2]*jamFactors[2],2) #5  #10 #5
        reward4 = round(roadPenalty[3]*jamFactors[3],2) #7  #7  #14
        reward = [reward1,reward2,reward3,reward4]
            
        for road in range(0,4):
            cost = reward[0]+reward[1]+reward[2]+reward[3]
            #lossValue[i] = (summation of cost of all roads excluding road i) - reward[i]
            # or
            #lossValue[i] = (summation of cost of all roads) - 2 * reward[i]
            lossValues[road] = cost - 2*reward[road]

        #get the road with minimum loss value
        minLoss = min(lossValues)
        for y in range(len(lossValues)):
            if minLoss == lossValues[y]:
                minLossRoad = y
                break

        #timer algo
        totalReward = round(sum(reward),2)
        print(reward[minLossRoad], totalReward, baseTime)
        Timer = int((reward[minLossRoad]/totalReward) * baseTime)
        baseTime = baseTime - Timer

        #change penalty value for selected road to default value 1 and rest based on the penalty formula
        for z in range(len(roadPenalty)):
            if z == minLossRoad:
                roadPenalty[z] = 1
            else:
                roadPenalty[z] = (roadPenalty[z]+1)*(roadPenalty[z])

        ct = datetime.datetime.now().strftime('%H:%M:%S')
        print()
        print(f'{ct} : [INFO] Recalculating')
        print(f'{ct} : [ALGO] Jam Factors -', jamFactors)
        print(f'{ct} : [ALGO] Penalty -', roadPenalty)
        print(f'{ct} : [ALGO] Road -', minLossRoad+1)
        print(f'{ct} : [ALGO] Time -', Timer)
        print()
        time.sleep(Timer)

algorithm()