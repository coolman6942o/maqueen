from microbit import *

#Subroutine 1
def startUltrasonic():
    # Description: This subroutine triggers the ultrasonic sensor on the Maqueen robot to 
    # measure the distance of any obstacles in front. The measured distance is returned in centimeters.
    # Data Requirement: Utilizes the Maqueen ultrasonic sensor to output a distance value.
    
    distance = maqueen.ultrasonic(PingUnit.CENTIMETERS)  # Measures the distance to the nearest obstacle
    return distance  # Returns the measured distance for further processing

#Subroutine 2
def obstacleAvoidance():
    # Description: This subroutine handles obstacle detection and avoidance for the Maqueen robot.
    # It retrieves distance data using the ultrasonic sensor and decides whether to move forward,
    # stop, reverse, or turn based on the proximity of obstacles.
    # Data Requirement: Calls startUltrasonic() to get obstacle distance data to make decisions. 
    
    distance = startUltrasonic()  # Get distance from the ultrasonic sensor
    
    if distance > 10 or distance == 0:  # If the path is clear enough or distance not detected
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)  # Move forward
        basic.show_string("F")  # Display 'F' for forward direction
        bluetooth.uart_write_number(distance)  # Send the distance data over Bluetooth
    else:
        maqueen.motor_stop(maqueen.Motors.ALL)  # Stop motors if an obstacle is close
        basic.show_string("S")  # Display 'S' for stop
        basic.pause(250)  # Brief pause before reversing
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)  # Reverse
        basic.show_string("B")  # Display 'B' for backward direction
        basic.pause(1000)  # Reverse time
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)  # Turn left
        basic.show_string("L")  # Display 'L' for left direction
        basic.pause(250)  # Time to execute turn
        bluetooth.uart_write_number(distance)  # Send the updated distance
    
while True:
    obstacleAvoidance()  # Continuously call to maintain obstacle avoidance behavior

