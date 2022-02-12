import requests
def main():
    str1 = "http://api.tianapi.com/tianqi/index?key=24ed26685e8fd50b9cae20ffb41080b9&city="
    str2 = input('输入你想查询天气情况的城市名字')
    print(str1+str2)
    resp = requests.get(str1+str2)
    date_model = resp.json()
    for index in date_model['newslist']:
        for k,v in index.items():
            print(k,v)
if __name__ == '__main__':
    main()
