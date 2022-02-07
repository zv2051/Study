def mai():
    f = None
    try:
        f = open('/Users/zhangxu/github/Study/readme', 'r', encoding = 'utf-8')
        print(f.read())
    except FileNotFoundError:
        print("file not find")
    except LookupError:
        print('encodin error')
    except UnicodeDecodeError:
        print('decode error')
    finally:
        if f:
            f.close()
mai()
