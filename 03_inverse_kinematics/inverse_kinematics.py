from numpy import *
from math import *

def position_to_dof(x, y, z):
    """Acá va tu código para calcular la cinemática inversa
    
    La función debe recibir (x,y,z) en milimetros y retornar q0, q1 y q2 en grados"""

    Q0 = arctan(y/x) #(x,y)
    Q2 = arccos((((x/cos(Q0))-66.3)**2+(z-94)**2-147**2-135**2)/(2*147*135))  #(x,y,z)
    Q1 = arctan(((x/cos(Q0))-66.3)/(z-94))-arctan((147*sin(Q2))/(135+147*cos(Q2)))  #(x,y,z)
    q0 = degrees(Q0)
    q1 = degrees(Q1)
    q2 = degrees(Q2)

    return int(q0), int(q1), int(q2)    # El robot solo entiende grados sexagesimales y enteros

    #return int(q0), int(q1), int(q2)    # El robot solo entiende grados sexagesimales y enteros
