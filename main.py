from fastapi import FastAPI, Request
from secret import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET
from linebot import WebhookParser
from linebot.models import MessageEvent, TextMessage, TextMessage
from aiolinebot import AioLineBotApi

# APIクライアントとパーサーをインスタンス化
line_api = AioLineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(channel_secret=CHANNEL_SECRET)


app = FastAPI()

@app.get("/")
async def index(request:Request):
    events = parser.parse((await request.body()).decode("utf-8"), request.headers.get("X-Line-Signature"))

    for ev in events:
        await line_api.reply_message_async(ev.reply_token, TextMessage(text=f"You Said:{ev.message.text}"))
    return "OK"