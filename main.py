from fastapi import FastAPI, Request
from linebot import WebhookParser
from linebot.models import TextMessage
from aiolinebot import AioLineBotApi
from .secret.py import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET

import os
from os.path import join, dirname
from dotenv import load_dotenv

line_api = AioLineBotApi(channel_access_token=os.environ.get("token"))


app = FastAPI()

@app.get("/")
async def index():
    return {"Hello world":"Yes"}