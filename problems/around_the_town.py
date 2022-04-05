import math

class Stop:
    def __init__(self, current_loc) -> None:
        self.current_loc = current_loc
        self.landmarks = []
        pass
    
    def add_new_landmark(self, landmark):
        self.landmarks.append(landmark)
    
    def clear_landmarks(self):
        self.landmarks = []
    
    def get_current_loc(self):
        return self.current_loc
    
    def set_current_loc(self, new_loc):
        self.current_loc = new_loc
    
    def get_distance_from_loc(self, loc):
        x, y = tuple([float(num) for num in self.current_loc.split(' ')])
        loc_x, loc_y = tuple([float(num) for num in loc.split(' ')])
        distance = math.sqrt(((x - loc_x) ** 2) + ((y - loc_y) ** 2))
        return distance
    
    def get_new_loc(self):
        new_x = 0
        new_y = 0
        for landmark in self.landmarks:
            x, y = tuple([float(num) for num in landmark.split(' ')])
            new_x += x
            new_y += y
        
        num_landmarks = len(self.landmarks)
        return f'{(new_x / num_landmarks)} {(new_y / num_landmarks)}'

def get_closest_stop(landmark, stops):
    closest = stops[0]
    for i in range(1, len(stops)):
        if stops[i].get_distance_from_loc(landmark) < closest.get_distance_from_loc(landmark):
            closest = stops[i]
    return closest

n_input = int(input())

inputs = []
for i in range(n_input):
    f_in = [int(num) for num in input().split(' ')]
    inp = { 'fLine': f_in, 'L': [input() for j in range(f_in[0])], 'S': [input() for j in range(f_in[1])]}
    inputs.append(inp)

for case in inputs:
    l = case['L']
    s = case['S']
    
    stops = [Stop(stop) for stop in s]
    
    last_stops_loc = [stop.get_current_loc() for stop in stops]
    final = []
    optimal_found = False
    while not optimal_found:
        for loc in l:
            get_closest_stop(loc, stops).add_new_landmark(loc)
        
        for stop in stops:
            stop.set_current_loc(stop.get_new_loc())
            stop.clear_landmarks()
        
        optimal_found = True
        for i, last_stop in enumerate(last_stops_loc):
            x, y = tuple([round(float(num), 2) for num in stops[i].get_current_loc().split(' ')])
            las_x, las_y = tuple([round(float(num), 2) for num in last_stop.split(' ')])
            r_ls = f'{las_x} {las_y}'
            r_s = f'{x} {y}'
            if r_s != r_ls:
                optimal_found = False
        
        last_stops_loc = [stop.get_current_loc() for stop in stops]
    
    for stop in stops:
        x, y = tuple([round(float(num), 1) for num in stop.get_current_loc().split(' ')])
        print(f'{x} {y}')