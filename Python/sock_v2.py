from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from threading import Thread
from json import dumps
def main():
    class FileTransHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            print('in filetranshandler')
            my_dict['filename'] = '1.jpg'
            my_dict['filedate'] = date
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            print('send fanish')
            self.cclient.close()
            print('close')
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1',5566))
    server.listen(512)
    print('into listen')
    with open('/users/zhangxu/2.jpg', 'rb') as f:
        date = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print('client ip is %s' % str(addr))
        FileTransHandler(client).start()
if __name__ == '__main__':
    main()
