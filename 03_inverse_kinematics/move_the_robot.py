import time
from client import RobotClient
from inverse_kinematics import position_to_dof


## Conectarse al robot

r = RobotClient(address="localhost")  # Recuerda usar una dirección válida
r.connect()
r.home()    # Revisa el archivo client.py para que veas qué hace esta función


## Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)


## Mover el robot (acá va tu código)
def cuadrado(l):
    assert type(l)==int and l>0 and l<100
    move_robot_to_xyz(robot, 100, 50, 80)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100, 50, 50)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100+l, 50, 50)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100+l, 50+l, 50)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100, 50+l, 50)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100, 50, 50)
    time.sleep(0.6)
    move_robot_to_xyz(robot, 100, 50, 80)
    time.sleep(0.6)



