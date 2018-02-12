#!/usr/bin/env python3

#TODO: get HTTP responses working, format responses

import sys
import socket

target_h = sys.argv[1]
target_p = int(sys.argv[2])
data = sys.argv[3]

print("Connecting to ",target_h," on port ",target_p," sending \"",data,"\"",sep="")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_h,target_p))
client.send(data.encode(encoding="utf-8"))
client.shutdown(socket.SHUT_WR)
print(client.recv(65535))
client.close()
