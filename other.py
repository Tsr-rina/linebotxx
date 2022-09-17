from fastapi import FastAPI, Request, BackgroundTasks
from secret import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET
from linebot import WebhookParser
from linebot.models import MessageEvent, TextMessage, TextMessage
from aiolinebot import AioLineBotApi

# APIクライアントとパーサーをインスタンス化
line_api = AioLineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(channel_secret=CHANNEL_SECRET)


app = FastAPI()

async def handle_events(events):
    for ev in events:
        try:
            await line_api.reply_message_async(ev.reply_token, TextMessage(text=f"You Said:{ev.message.text}"))
        except Exception:
            pass

@app.post("/")
async def index(request:Request, background_tasks:BackgroundTasks):
    events = parser.parse((await request.body()).decode("utf-8"), request.headers.get("X-Line-Signature"))
    background_tasks.add_task(handle_events, events=events)
    return "OK"
