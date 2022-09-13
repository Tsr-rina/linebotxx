from fastapi import FastAPI, Request, BackgroundTasks
from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi
from linebot.exceptions import InvalidSignatureError
from secret import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET


# APIクライアントとパーサーをインスタンス化
line_api = AioLineBotApi(channel_access_token=CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(channel_secret=CHANNEL_SECRET)


app = FastAPI()

@app.get("/")
async def index(request:Request, background_tasks: BackgroundTasks):
    events = parser.parse((await request.body()).decode("utf-8"), request.headers.get("X-Line-Signature",""))
    background_tasks.add_task(handle_events, events=events)
    return "OK"

async def handle_events(events):
    for ev in events:
        try:
            await line_api.reply_message_async(
                ev.reply_token,
                TextMessage(text=f"You said:{ev.message.text}")
            )
        except Exception:
            pass