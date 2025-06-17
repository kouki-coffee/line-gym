import requests
import json
import os

ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
USER_ID = os.environ["LINE_USER_ID"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

body = {
    "to": USER_ID,
    "messages": [
        {
            "type": "text",
            "text": "筋トレの時間だ！💪 頑張れ！"
        }
    ]
}

response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, data=json.dumps(body))
print(f"ステータスコード: {response.status_code}")
