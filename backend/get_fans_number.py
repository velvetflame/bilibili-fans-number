import requests, json, time

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bilibili.com/",
    "Content-Type": "application/json"
}
API = {
    "url": "https://api.bilibili.com/x/relation/stat",
    "params": {
        "vmid": 477792 #up主uid
    }
}

def get():
    req = requests.request("GET", **API, headers = DEFAULT_HEADERS)
    if req.ok:
        con = req.json()
        if con["code"] == 0:
            print('已获取粉丝数: {}'.format(con['data']['follower']))
            with open('fansnumber.json', 'w') as f:
                json.dump({
                    'id': con['data']['mid'],
                    'fensishu': con['data']['follower']
                }, f)
        else:
            print('接口返回了错误:')
            print(con)
    else:
        print(f'网络错误, 错误码: {req.status_code}')

while True:
    get()
    time.sleep(60) #叔叔接口拉取频率不建议过快，60秒经测试稳定
