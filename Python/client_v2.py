from socket import socket
from base64 import b64decode
from json import loads

def main():
    client = socket()
    client.connect(('127.0.0.1', 5566))
    in_date = bytes()
    data = client.recv(1024)
    print('first recv')
    while data:
        print('in while')
        in_date += data
        data = client.recv(1024)
    print('trans finash')
    my_dict = loads(in_date.decode('utf-8'))
    file_name = my_dict['filename']
    print(file_name)
    file_date = my_dict['filedate'].encode('utf-8')
    with open('/users/zhangxu/pic'+ file_name, 'wb') as f:
        f.write(b64decode(file_date))
        print('pic store')

if __name__=='__main__':
    main()
