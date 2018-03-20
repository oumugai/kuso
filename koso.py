import json
import websocket
from numba import autojit

ws = websocket.create_connection("wss://saiyo2019.moi.st/websocket/42db11423e45481bafd02915487396c6")

ws.send(json.dumps({
    "signal": "start"
}))

while True:
    res = json.loads(ws.recv())
    come_num = int(res["number"])
    result = ""
    if come_num % 3 == 0:
        result += "Fizz"
    if come_num % 5 == 0:
        result += "Buzz"
    if come_num % 7 == 0:
        result += "Moi"
    if result == "":
        result = come_num
    ws.send(json.dumps({
      "answer": result
    }))      
