import socket
import struct

class MiniCap(object):
    def __init__(self, host, port):
        self.address = (host, port)
        self.socket = self.create_socket()
        self.banner = self.parser_banner()
        self._img = None

    @property
    def img(self):
        return self.parser_img()

    def create_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(self.address)
        return s

    def parser_banner(self):
        data = self.socket.recv(24)
        return struct.unpack("<2B5I2B", data)

    def parser_img(self):
        data = self.socket.recv(4)
        img_len = struct.unpack("<I", data)[0]
        data = ""
        length = img_len
        while True:
            data += self.socket.recv(length)
            length = img_len - len(data)
            if length <= 0:
                break
        return data

