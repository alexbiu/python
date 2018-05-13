# python

# cp_select_server.py
from socket import *
from select import *
import sys

s =socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)
rlist=[s]
wlist=[]
xlist=[s]
print("Waiting for the link.....")

while True:
    rs,ws,xs=select(rlist,wlist,xlist,3)
    for r in rs:
        if r is s:
            conntd,addr=r.accept()
            print("%s已经链接上"%addr[0])
            rlist.append(conntd)
        else:
            try:
                data=r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                else:
                    print('Messages are received is:',data.decode())
                    r.send("Please continue to".encode())
                    wlist.append(r)
            except Exception:
                pass
    for w in ws:
        pass
    for x in xs:
        pass


 

