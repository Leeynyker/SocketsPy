# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:40:30 2020

@author: leeyn
"""

import socket
import numpy as np

HOST = 'localhost'
PORT = 50007



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(1)

conn,addr = s.accept()
print(conn,' conectado por ', addr)
while 1:
    data = conn.recv(1024)
    print(type(data))
    cadena=data.decode("utf-8")
    Es=cadena.split("~")
    E1=Es[0].split(" ")
    E2=Es[1].split(" ")
    print("------------------------------------------------------")
    print(E2)
    print(E1)
    print("------------------------------------------------------")
    
    try:
        a=np.array([[float(E1[0]),float(E1[1])],[float(E2[0]),float(E2[1])]])
        b=np.array([float(E1[2]),float(E2[2])])
        x=np.linalg.solve(a,b)
        cad=str(x[0])+"-"+str(x[1])
    except:
        if (float(E1[2]) == 0 and float(E1[0])==0 and float(E1[1])==0) or (float(E2[2]) == 0 and float(E2[0])==0 and float(E2[1])==0):
            
            cad="Tiene infinitas soluciones"
        else:
            cad="No tiene solucion"
#    print(x)
    print("--")
    print(cad)
    
    conn.sendall(cad.encode("utf-8"))
    if not data:
        break
    

    
conn.close