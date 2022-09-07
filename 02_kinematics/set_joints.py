import time
from client import RobotClient


## Conectarse al robot

robot = RobotClient(address="localhost")  # Recuerda usar una dirección válida
robot.connect()

## Mover el robot (acá va tu código)

HOME_Q0 = 0
HOME_Q1 = 0
HOME_Q2 = 90

##Variables Posicion

Q0 = 0
Q1 = 0
Q2 = 90

def reset_pos():
    Q0 = HOME_Q0
    Q1 = HOME_Q1
    Q2 = HOME_Q2
    robot.set_joints(q0=HOME_Q0, q1=HOME_Q1, q2=HOME_Q2)
    time.sleep(0.6)


def turn_left(): #Esta funcion mueve el brazo 10 grados a la izquierda (visto de frente)
    Q0 = Q0
    Q1 = Q1 - 10
    Q2 = Q2
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)




def turn_right(): #Esta funcion mueve el brazo 10 grados a la derecha (visto de frente)
    Q0 = Q0
    Q1 = Q1 + 10
    Q2 = Q2
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)
def go_forward(): #Esta funcion mueve el brazo 10 grados hacia adelante (visto de frente)
    Q0 = Q0 + 10
    Q1 = Q1
    Q2 = Q2
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)

def go_backward(): #Esta funcion mueve el brazo 10 grados hacia atras (visto desde frente)
    Q0 = Q0
    Q1 = Q1 - 10
    Q2 = Q2
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)

def up(): #Esta funcion mueve el brazo 10 grados hacia arriba (visto desde frente)
    Q0 = Q0
    Q1 = Q1
    Q2 = Q2 + 10
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)

def down(): #Esta funcion mueve el brazo 10 grados hacia abajo (visto desde frente)
    Q0 = Q0
    Q1 = Q1
    Q2 = Q2 - 10
    robot.set_joints(q0=Q0, q1=Q1, q2=Q2)
    time.sleep(0.6)