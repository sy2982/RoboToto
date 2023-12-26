from math import sin, cos
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

def initialize_servos():
    try:
        # Initialize servo motors for each leg
        servo = []
        for i in range(1, 9):
            servos = LX16A(i)
            if i % 2 != 0:  # For odd-numbered servos
                servos.set_angle_limits(30, 210)
            else:
                servos.set_angle_limits(0, 210)
            servo.append(servos)
        return servo
    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

def home(servo):
    try:
        for i, servos in enumerate(servo, start=1):
            print(f"Servo {i}: {servos.get_physical_angle()}")
            if i % 2 == 0:  # Check if the servo number is even
                servos.move(30)
            else:
                servos.move(120)
            print(f"Home Position: {servos.get_commanded_angle()}")
            print(f"Temp: {servos.get_temp()} Celsius")
            print(f"Voltage: {servos.get_vin() / 1000}V\n")

            # Boot testing
            if(servos.get_temp() > 80):
                print(f"Servo {i} is to hot!")
                quit()
            if(servos.get_vin() / 1000 > 8):
                print(f"Servo {i}'s voltage is too high!")
                quit()
            elif(servos.get_vin() / 1000 < 5):
                print(f"Servo {i}'s voltage is too low!")
                quit()
            
            
        # Double check to make sure feet are in the correct positions
        time.sleep(1)
        for i, servos in enumerate(servo, start=1):
            if i % 2 == 0:
                servos.move(120)
                time.sleep(1)
                servos.move(30)
                time.sleep(1)

    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

def moves(servo, movement):
    
    amplitude = 30
    a_vertical = 50
    a_horizontal = 30
    frequency = 1
    phase_shift = 3.14  # 180 degrees in radians
    h_range = 100  # horizontal range
    v_range = 45
    
    if movement.lower() == "move":
        print("Moving...")
        try:
            t = 0
            while t < 20:

                # Move the servos with a synchronized sine function for the front right and back left legs
                servo[0].move(sin(t * frequency) * a_horizontal + amplitude + h_range)
                servo[1].move(cos(t * frequency) * a_vertical + amplitude + v_range)
                servo[6].move(sin(t * frequency + phase_shift) * a_horizontal+ amplitude + h_range)
                servo[7].move(cos(t * frequency + phase_shift) * a_vertical + amplitude + v_range)

                # Move the servos with a synchronized cosine function for the front left and back right legs
                servo[2].move(cos(t * frequency) * a_horizontal + amplitude + h_range)
                servo[3].move(sin(t * frequency) * a_vertical + amplitude + v_range)
                servo[4].move(cos(t * frequency + phase_shift) * a_horizontal + amplitude + h_range)
                servo[5].move(sin(t * frequency + phase_shift) * a_vertical + amplitude + v_range)
                
                time.sleep(0.02)  # Sleep time for a slower/faster gait
                t += 0.1
                
            # Auto home without double checking
            for i, servos in enumerate(servo, start=1):
                time.sleep(0.1)
                if i % 2 == 0:
                    servos.move(30)
                else:
                    servos.move(120)
                
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()
            
    elif movement.lower() == "rabbit":
        print("Rabbiting...")
        try:
            t = 0
            while t < 45:

                # Move the servos with a synchronized sine function for the front right and back left legs
                servo[0].move(sin(t * frequency) * a_horizontal + amplitude + h_range)
                servo[1].move(cos(t * frequency) * a_vertical + amplitude + v_range)
                servo[6].move(sin(t * frequency + phase_shift) * a_horizontal+ amplitude + h_range)
                servo[7].move(cos(t * frequency + phase_shift) * a_vertical + amplitude + v_range)

                # Move the servos with a synchronized cosine function for the front left and back right legs
                servo[2].move(cos(t * frequency) * a_horizontal + amplitude + h_range)
                servo[3].move(sin(t * frequency) * a_vertical + amplitude + v_range)
                servo[4].move(cos(t * frequency + phase_shift) * a_horizontal + amplitude + h_range)
                servo[5].move(sin(t * frequency + phase_shift) * a_vertical + amplitude + v_range)
                
                time.sleep(0.015)  # Sleep time for a slower/faster gait
                t += 0.1
                
            # Auto home without double checking
            for i, servos in enumerate(servo, start=1):
                time.sleep(0.1)
                if i % 2 == 0:
                    servos.move(30)
                else:
                    servos.move(120)
                
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()
            
    elif movement.lower() == "dance":
        print("Dancing...")
        try:
            t = 0
            while t < 50:
                
                for i, servos in enumerate(servo, start=1):
                    if i % 2 != 0:  # For odd-numbered servos
                        servos.move(sin(t * frequency) * a_horizontal + amplitude + h_range)
                    else:  # For even-numbered servos
                        servos.move(cos(t * frequency) * a_vertical + amplitude + v_range)

                time.sleep(0.025)  # Sleep time for a slower/faster gait
                t += 0.1
                
            # Auto home without double checking
            for i, servos in enumerate(servo, start=1):
                if i % 2 == 0:
                    servos.move(30)
                else:
                    servos.move(120)
                
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()
            
    elif movement.lower() == "wave":
        print("Waving...")
        try:
            t = 0
            servo[5].move(210)
            time.sleep(.5)
            while t < 30:

                servo[4].move(cos(t * frequency) * a_horizontal + amplitude + h_range)

                time.sleep(0.025)  # Sleep time for a slower/faster gait
                t += 0.15
            
            servo[5].move(30)
                        
        except ServoTimeoutError as e:
            print(f"Servo {e.id_} is not responding. Exiting...")
            quit()
        
    else:
        print("Goodbye")
        quit()


def main():
    servo = initialize_servos()
    home(servo)

    movement = input("Enter 'move', 'rabbit', 'dance' or 'wave': ")

    moves(servo, movement)
    

if __name__ == "__main__":
    main()
