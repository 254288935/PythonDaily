from flask import Flask
from flask_sockets import Sockets
import base64
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


app = Flask(__name__)
minicap = MiniCap('127.0.0.1', 1717)
sockets = Sockets(app)


@sockets.route('/img')
def echo_socket(ws):
    while not ws.closed:
        img = base64.b64encode(minicap.img)
        ws.send(img)


@app.route('/')
def hello():
    page = '''
        <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Cap</title>
    </head>
    <body onload="display();">
    <img id='img' width="360" height="720" src="">
    <script type="text/JavaScript">
        var ws;
        function display() {
            ws = new WebSocket("ws://127.0.0.1:5000/img");
            ws.onmessage = function (event) {
                var data = event.data;
                document.getElementById("img").src = "data:image/gif;base64," + data;
            };
        }
    </script>
    </body>
    </html>
    '''
    return page


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()

