#自定义钉钉机器人

import json
import requests
import sys
import getpass

def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['136xxxx4373']
    url = getpass.getpass()
    print(send_msg(url, reminders, msg))
