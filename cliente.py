# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:39:42 2020

@author: leeyn
"""

import socket

HOST = 'localhost'
PORT = 50007
E1=str(input("Escriba los valores de la primera ecuacion separados por - "))
E2=str(input("Escriba los valores de la segunda ecuacion separados por - "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
cad=str(E1+"~"+E2)
s.sendall(cad.encode())

data=s.recv(1024)
caden = data.decode("utf-8")
print("La solucion es: "+ caden)

