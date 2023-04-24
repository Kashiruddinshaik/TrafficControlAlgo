import flexpolyline as fp
import json

bharathiyar_road = [
    (11.016149, 76.970931),
    (11.016254, 76.972316),
    (11.016359, 76.973368),
    (11.016507, 76.974634),
    (11.016591, 76.975665),
    (11.016754, 76.976996)
]

balasundaram_road = [
    (11.006645, 76.974948),
    (11.008693, 76.975494),
    (11.009926, 76.975722),
    (11.012636, 76.976222),
    (11.014158, 76.976586),
    (11.016498, 76.977200)
]

kattoor_road = [
    (11.013764, 76.979832),
    (11.013808, 76.978996),
    (11.014775, 76.978816),
    (11.015551, 76.978723),
    (11.016167, 76.978395),
    (11.016596, 76.977591)
]

sarojini_naidu_road = [
    (11.020724, 76.978622),
    (11.020192, 76.978622),
    (11.019561, 76.978579),
    (11.019187, 76.978436),
    (11.018731, 76.978114),
    (11.018112, 76.977734),
    (11.016975, 76.977418)
]

encodings = {
    'bharathiyar_road': fp.encode(bharathiyar_road),
    'balasundaram_road': fp.encode(balasundaram_road),
    'kattoor_road': fp.encode(kattoor_road),
    'sarojini_naidu_road': fp.encode(sarojini_naidu_road),
}

obj = json.dumps(encodings)

with open("corridor_encodings.json", 'w') as f:
    f.write(obj)
