import requests

url = "http://127.0.0.1:8000/mcp/"

headers = {
    "Accept":"application/json,text/event-stream",
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {},
    "id": 1


}

response = requests.post(url=url, headers=headers, json=body)
print(response.text)