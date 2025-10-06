import math
# Base values are assigned as default
default_unit = "metric"
default_mode = "free fall"
acceleration = -9.8
velocity = 0
distance = 0

# Program welcomes the user
print("Welcome To The Motion Simulation!")

# Program then asks for unit system
print("Please Type Your Unit System(Empirical/Metric): ")
user_unit = str(input())
user_unit = user_unit.lower()
user_unit_velocity = ""
user_unit_position = ""

# Units are assigned for velocity and position depending on selected unit system
# Object values are adjusted by corresponding units
if user_unit == "empirical":
    user_unit_velocity = "feet/second"
    user_unit_position = "feet"
    acceleration = acceleration * 3.281
    velocity = velocity * 3.281
elif user_unit == "metric":
    user_unit = default_unit
    user_unit_velocity = "meters/second"
    user_unit_position = "meters"
else:
    user_unit = default_unit
    user_unit_velocity = "meters/second"
    user_unit_position = "meters"
    print("Units Are Set To Default Due to Invalid Entry: \"Metric\"")

# User is asked to select the mode
print("Please Choose Your Simulation Mode: Free Fall; Launch Upward; Custom")
mode = str(input())
mode = mode.lower()

# Program checks if the selected mode has a match.
# Then, the program reacts back with corresponding output.
if mode == "free fall" :
    print("Please Enter the Vertical Distance of the Object: ",user_unit_position)
    distance = float(input())

if mode == "launch upward":
    print("Please Enter the Initial Velocity of the Object: ",user_unit_velocity)
    velocity = float(input())

if mode == "custom":
    print("Please Enter the Vertical Distance of the Object: ",user_unit_position)
    distance = float(input())
    print("Please Enter the Initial Velocity of the Object: ",user_unit_velocity)
    velocity = float(input())

# Program sets the mode to its default metric system
# If no match found for the mode which entered by the user
if mode!= "free fall":
    if mode != "launch upward":
        if mode != "custom":
            mode = default_mode
            print("Simulation Mode Set to Default Due to Invalid Entry: \"Free Fall\"")
            print("Please Enter the Vertical Distance of the Object: ",user_unit_position)
            distance = float(input())

# The user enters three time intervals in seconds
# Then program assigns calculated positions and velocities to variables based on the given times
print("Type Three Time Intervals To Simulate: seconds")
time = [input("Time @ "),input("Time @ "),input("Time @ ")]
time_1 = float(time[0])
time_2 = float(time[1])
time_3 = float(time[2])

velocity_1 = velocity + acceleration * time_1
distance_1 = distance + (velocity * time_1) + (acceleration * (time_1**2) / 2)

velocity_2 = velocity + acceleration * time_2
distance_2 = distance + (velocity * time_2) + (acceleration * (time_2**2) / 2)

velocity_3 = velocity + acceleration * time_3
distance_3 = distance + (velocity * time_3) + (acceleration * (time_3**2) / 2)
"""
Equation is 0.5 x acceleration x time.square + velocity x time + height = 0
Find discriminant (∆) and figure the time from roots of the quadratic equation.
(∆>0 and a maximum of two roots) or (∆=0 and a root) or (∆<0 and no roots no collision)
Now, user can be warned for what the time and what the velocity are at the collision.
"""
a = acceleration * 0.5
b = velocity
c = distance
discriminant = pow(b,2) - (4 * a * c)

if discriminant > 0:
    root1 = (-math.sqrt(discriminant)-b)/2/a
    root2 = (math.sqrt(discriminant)-b)/2/a
    collision_time = max(root1, root2)
    collision_velocity = velocity + acceleration * collision_time
elif discriminant == 0:
    collision_time = (-math.sqrt(discriminant)-b)/2/a
    collision_velocity = velocity + acceleration * collision_time
else:
    collision_time = None
    collision_velocity = None

"""Lastly the program outputs as comparing the distance"""
if distance_1 >= 0:
    print(f"At {time_1} seconds, the velocity is {velocity_1:.2f} {user_unit_velocity}, the position is {distance_1:.2f} {user_unit_position}.")
elif distance_1 < 0:
    print(f"Warning! Object has hit the ground. @,{collision_time:.2f} seconds with velocity of {collision_velocity:.2f} {user_unit_velocity}.")
if distance_2 >= 0:
    print(f"At {time_2} seconds, the velocity is {velocity_2:.2f} {user_unit_velocity}, the position is {distance_2:.2f} {user_unit_position}.")
elif distance_2 < 0:
    print(f"Warning! Object has hit the ground. @,{collision_time:.2f} seconds with velocity of {collision_velocity:.2f} {user_unit_velocity}.")
if distance_3 >= 0:
    print(f"At {time_3} seconds, the velocity is {velocity_3:.2f} {user_unit_velocity}, the position is {distance_3:.2f} {user_unit_position}.")
elif distance_3 < 0:
    print(f"Warning! Object has hit the ground. @,{collision_time:.2f} seconds with velocity of {collision_velocity:.2f} {user_unit_velocity}.")



