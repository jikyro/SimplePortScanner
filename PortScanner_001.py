#!/usr/bin/python3

import socket #Socket Programming is a way of connecting two nodes on a network to communicate with each other.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET specifies that you are working with IPv4. IPv4 is the fourth version of the Internet Protocol and one of the core protocols of standards-based internetworking in the internet and other packet-switched networks.

s.settimeout(5) #Set a timeout of 5 seconds
host = input("Please enter the IP you want to scan: ")  #IP Address of targeted site. EX:hackthissite.
port = int(input("Please enter the port you want to scan: ")) #Port number youa re scanning.

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)