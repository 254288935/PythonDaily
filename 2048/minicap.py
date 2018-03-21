import socket
import struct
import binascii

Host = '127.0.0.1'
Port = 1717

ip_port = '192.168.1.3:1717'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host,Port))
# s.connect(ip_port)


# data = s.recv(6)
# a = struct.unpack('BBBBBB', data)
# for x in a:
#     print x

data = s.recv(24)
a = struct.unpack('24B', data)
b = list(a)
print b
c= [b[0], b[1], b[3]*256+b[2], b[7]*256+b[6], b[11]*256+b[10], b[15]*256+b[14], b[19]*256+b[18], b[-2], b[-1]]
print c
picture_data = s.recv(4)
a = struct.unpack('4B', picture_data)
print a
picture_size = (a[1]*256 + a[0])
print picture_size
length = picture_size
data = ''
while 1:
    data += s.recv(length)
    length = picture_size - len(data)
    if length <= 0:
        break

with open('pppp.jpg', 'wb') as p:
    p.write(data)


