from tqdm import tqdm
#open file and red line
landing_area = open("files\day17.txt", 'r').read().split('\n')[0].split(", ")
x_min, x_max = [int(i) for i in landing_area[0].split("=")[1].split("..")]
y_min, y_max = [int(i) for i in landing_area[1].split("=")[1].split("..")]

#Part 1 parabolic formula (try and hit lowest y point of the landing area)
lowestY = y_min
max_height = y_min*(y_min+1) / 2
print("Part 1: ", max_height)

#Part 2
x_range = [0, x_max]
y_range = [y_min, 1000]
bounds=[[x_min, x_max], [y_min, y_max]]

def does_it_hit(launch_velocity, bounds):
    v_x, v_y = launch_velocity
    x, y = 0, 0
    while True:
        x, y, v_x, v_y = x + v_x, y + v_y, max(0, v_x-1), v_y-1
        if x > bounds[0][1] or y < bounds[1][0]: return False
        if x >= bounds[0][0] and x <= bounds[0][1] and y >= bounds[1][0] and y <= bounds[1][1]: return True

hits = []
for x in tqdm(range(x_range[0], x_range[1]+1)):
    for y in range(y_range[0], y_range[1]+1):
        if does_it_hit([x, y], bounds):
            hits.append([x,y])

print("Part 2: ", len(hits))