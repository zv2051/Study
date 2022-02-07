import time

def main():
    f = None
    try:
        with open('/Users/zhangxu/github/Study/readme', 'r', encoding = 'utf-8') as f:
            print(f.read())
        with open('/Users/zhangxu/github/Study/readme', 'r', encoding = 'utf-8') as f:
            for line in f:
                print(line, end='')
                time.sleep(1)
        with open('/Users/zhangxu/github/Study/readme', 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
        print(lines)
    except FileNotFoundError:
        print("file not find")
    except LookupError:
        print('encodin error')
    except UnicodeDecodeError:
        print('decode error')
if __name__ == '__main__':
    main()
