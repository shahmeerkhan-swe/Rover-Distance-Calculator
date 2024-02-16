#Khan_Shahmeer 201662879 October2022 CA-02
#Calculating the distance travelled by a rover horizontally and vertically
import math
speed = 1.5
destination_reached = 0

#Input Section:
angle = int(input("Please enter the angle of travel for the robot in degrees: "))
time = int(input("Please enter the time taken for the robot to travel to the destination: "))

angleR = math.radians(angle)

#Process Section:
distance_travelled = speed * time
distance_horizontal = distance_travelled * math.sin(angleR)
distance_vertical = distance_travelled * math.cos(angleR)
battery_used = time * 2.7
battery_remaining = 100 - battery_used


#Output Section:
print("The angle you entered is: ",angle,"degrees")
print("The travel time entered is: ",time,"s")
print("The distance travelled is: ",distance_travelled,"m")
print("The horizontal distance travelled is: ", distance_horizontal,"m")
print("The vertical distance travelled is: ", distance_vertical,"m")
print("The battery used in the journey is: ", battery_used,"%")
print("The battery remaining is: ", battery_remaining,"%")

if (battery_used < 100):
    destination_reached = 1
    print("\nThe robot has reached its destination")
else:
    print("The robot has run out of battery!, the destination could not be reached")

if (destination_reached == 1):
    if(battery_remaining > battery_used):
        print("The robot has enough battery to make the return trip")
        print("\nPress return to exit the program")
    else:
        print("The robot cannot make the return trip")
