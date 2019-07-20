import requests
import json

url = 'http://192.168.1.11/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",   # 固定值
    "method": "apiinfo.version",  # 根据需求查手册获得
    "params": [],   # 参数
    "id": 1   # 随便给一个数字，表示任务编号
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())