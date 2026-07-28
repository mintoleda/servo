from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18,
                     initial_angle=70,
                     max_angle=360,
                     min_angle=0,
                     min_pulse_width=0.0005,
                     max_pulse_width=0.0025)
print(servo.min_angle)
print(servo.max_angle)
print("the current pulse_width is printed after each move\n")

while True:
    cmd = input("position: ").strip()

    match cmd:
        case 'q':
            break
        case "min":
            servo.min()
        case "mid":
            servo.mid()
        case "max":
            servo.max()
        case _:
            try:
                angle = float(cmd)
                if servo.min_angle <= angle <= servo.max_angle:
                    servo.angle = angle
                else:
                    print("nope")
                    continue
            except ValueError:
                print("invalid input")
                continue
            print(f"  pulse_widh: {servo.pulse_width:.6f}s")
servo.detach()