 
# ---------------------------------------------------
# File Name: shrink.py
# Description: A Pyrogram bot for downloading files from Telegram channels or groups 
#              and uploading them back to Telegram.
# Author: Gagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Created: 2025-01-11
# Last Modified: 2025-01-11
# Version: 2.0.5
# License: MIT License
# ---------------------------------------------------

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
import string
import aiohttp
from devgagan import app
from devgagan.core.func import *
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB, WEBSITE_URL, AD_API, LOG_GROUP  
from pyrogram.types import Message
 
 
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
 
 
async def create_ttl_index():
    await token.create_index("expires_at", expireAfterSeconds=0)
 
 
 
Param = {}
 
 
async def generate_random_param(length=8):
    """Generate a random parameter."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
 
 
async def get_shortened_url(deep_link):
    api_url = f"https://{WEBSITE_URL}/api?api={AD_API}&url={deep_link}"
 
     
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()   
                if data.get("status") == "success":
                    return data.get("shortenedUrl")
    return None
 
 
async def is_user_verified(user_id):
    """Check if a user has an active session."""
    session = await token.find_one({"user_id": user_id})
    return session is not None
 
 
@app.on_message(filters.command("start"))
async def token_handler(client, message):
    """Handle the /start command."""
    join = await subscribe(client, message)
    if join == 1:
        return

    user = message.from_user
    user_mention = f"[{user.first_name}](tg://user?id={user.id})"

    # Random image selection
    images = [
        "https://ar-hosting.pages.dev/1751519808272.jpg",
        "https://ar-hosting.pages.dev/1751519809076.jpg",
        "https://ar-hosting.pages.dev/1751519807441.jpg",
        "https://ar-hosting.pages.dev/1751519809887.jpg",
        "https://ar-hosting.pages.dev/1751519810683.jpg",
        "https://myappme.shop/img/file_255.jpg",
        "https://myappme.shop/img/file_256.jpg",
        "https://myappme.shop/img/file_257.jpg"
    ]
    image_url = random.choice(images)

    join_button = InlineKeyboardButton("Join Channel", url="https://t.me/Team_Sonu1")
    premium = InlineKeyboardButton("Get Premium", url="https://t.me/sonuporsa")
    keyboard = InlineKeyboardMarkup([
        [join_button],
        [premium]
    ])

    if len(message.command) <= 1:
        await message.reply_photo(
            photo=image_url,
            caption=(
                f"Hi 👋 {user_mention}, welcome!\n\n"
                "✳️ I can save posts from channels or groups where forwarding is off.\n"
                "✳️ Simply send the post link of a public channel. For private channels, do /login. Send /help to know more."
            ),
            reply_markup=keyboard
        )
        return

    param = message.command[1] if len(message.command) > 1 else None
    freecheck = await chk_user(message, user.id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return

    if param:
        if user.id in Param and Param[user.id] == param:
            await token.insert_one({
                "user_id": user.id,
                "param": param,
                "created_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(hours=3),
            })
            del Param[user.id]
            await message.reply("✅ You have been verified successfully! Enjoy your session for next 3 hours.")
        else:
            await message.reply("❌ Invalid or expired verification link. Please generate a new token.")


@app.on_message(filters.command("token"))
async def smart_handler(client, message):
    user_id = message.chat.id

    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return

    if await is_user_verified(user_id):
        await message.reply("✅ Your free session is already active enjoy!")
    else:
        param = await generate_random_param()
        Param[user_id] = param

        bot_user = await client.get_me()
        deep_link = f"https://t.me/{bot_user.username}?start={param}"

        shortened_url = await get_shortened_url(deep_link)
        if not shortened_url:
            await message.reply("❌ Failed to generate the token link. Please try again.")
            return

        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Verify the token now...", url=shortened_url)]]
        )
        await message.reply(
            "Click the button below to verify your free access token:\n\n"
            "> What will you get?\n"
            "1. No time bound upto 3 hours\n"
            "2. Batch command limit will be FreeLimit + 20\n"
            "3. All functions unlocked",
            reply_markup=button
 )

# 🔗 /sharelink command
@app.on_message(filters.command("shareme"))
async def sharelink_handler(client, message: Message):
    bot = await client.get_me()
    bot_username = bot.username

    bot_link = f"https://t.me/{bot_username}?start=True"
    share_link = f"https://t.me/share/url?url={bot_link}&text=🚀%20Check%20out%20this%20awesome%20bot%20to%20unlock%20restricted%20Telegram%20content!%20Try%20now%20"

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Share Me With Others 🫠", url=share_link)]
    ])

    await message.reply_text(
        f"✨ **Spread the Magic!**\n\n"
        f"Help others discover this bot that can save **restricted channel media**, even if forwarding is off! 🔒\n\n"
        f"Click a button below 👇 share me with your friends!",
        reply_markup=reply_markup
    )

 
