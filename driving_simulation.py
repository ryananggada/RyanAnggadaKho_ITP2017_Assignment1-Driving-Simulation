ini_vel = 0
time_on_road = int(input("Time spent on the road = "))
acc = int(input("Acceleration = "))
distance = int(input("Distance = "))
speed_limit = 60

for i in range(int(time_on_road+1)):
    star_rep = ""
    current_time = i
    final_vel = ini_vel + (acc * current_time)
    distance_travelled = 0.5 * acc * current_time**2
    distance_star = int(distance_travelled / 10)
    for j in range(int(distance_star)):
        star_rep += "*"
    print("Duration: {} Distance: {}".format(current_time, star_rep))

max_speed = ini_vel + (acc * time_on_road)
if max_speed > speed_limit:
    print("The person went over the speed limit. (Max speed was {} m/s)".format(max_speed))
else:
    print("The person did not go over the speed limit. (Max speed was {} m/s)".format(max_speed))

distance_reached = int(0.5 * acc * time_on_road**2)
if distance_reached >= distance:
    print("The person reached the destination. (Reached {} m)".format(distance_reached))
else:
    print("The person did not reach the destination. (Reached {} m)".format(distance_reached))
