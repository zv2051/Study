import re

def main():
    username = input("输入你的账号:")
    qq = input("in put you qq num:")
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m1:
        print("username error")
    if not m2:
        print("qq num error")
    if m1 and m2:
        print("right")

if __name__ == '__main__':
    main()
