--- Primary code files

1. algorithm.py -> Take jamFactors as inputs and output a road and time to give green signal for
2. main.py -> Runner file for the algorithm.


--- Retrieve JamFactors

3. corridor.py -> Script that encodes coordinates of roads into HERE_API understandable IDs
4. corridor_encodings.json -> Stores the encoded junctions
5. jamFactors.json -> A single instance of jamFactor for the junction
6. env.py -> File that stores environment variables API keys etc.


--- Fetch periodic JamFactors

7. getApiData.py -> Retrieves jamFactors on that timestamps and stores in jamFactors.json
8. 15mins_jamFactors.json -> File that stores jamFactors of the junction recorded over 15 minutes at 10 second intervals


--- Get remaining vehicles from SUMO and merge

9. traci_count.py -> Get number of vehicles remaining in every lane at every 50s interval from SUMO
10. remaining_vehicles.json -> List of remaining jamFactors objects at the junction
11. mergeJF.py -> Script that merges 15mins_jamFactors.json and remaining_vehicles.json
12. new_JF_List.json -> Final JamFactors


--- Generate SUMO traffic 

13. generateRoutes.py -> Converts jamFactors into vehicles and generates traffic, output -> generatedRoutes.rou.xml
14. generatedRoutes.rou.xml -> Generated traffic from all directions as xml

--- Generate traffic light sequence

15. generateRoadTimes.py -> Script to run the algorithm and get the traffic light sequence as JSON
16. road_times.json -> Stores a list of roads and times for each of the roads
17. generateLightAlgo.py -> Script that converts the JSON road times into SUMO XML traffic light sequence
18. TLSGenerated.xml -> Generated traffic light sequence in XML

