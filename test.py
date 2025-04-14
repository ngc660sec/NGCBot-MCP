import json

jsonString = "{\"status\":0,\"message\":\"成功\",\"data\":{\"wxId\":\"47442567074@chatroom\"}}"

jsonData = json.loads(jsonString)
print(type(jsonData))