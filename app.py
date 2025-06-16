import requests
import json

ACCESS_TOKEN = "NUyEmcZG35WBLmFejy80h8j4zHheBuI1/F87NKNCbJmr92p0hrrEsorgIjGKrGmBD0hBicDHMFqBhpNvyzpWod9ccEByUyFx2X9xBNggheWHar4/7s+IQ1E/JCD8g1u9b/uWo50x/bz2ihWIF1sjwQdB04t89/1O/w1cDnyilFU="
USER_ID = "Udbbe886b3396b1bb672e1e6fb980cc80"

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
