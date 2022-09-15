from fastapi import FastAPI, Request, BackgroundTasks
from secret import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET


# APIクライアントとパーサーをインスタンス化
# line_api = AioLineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
# parser = WebhookParser(channel_secret=CHANNEL_SECRET)


app = FastAPI()

@app.get("/")
async def index(event):
    headers = {"Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"}
    data = {"message": event}
    requests.post("https://notify-api.line.me/api/notify",headers=headers,data=data,)