# ---------------------------------------------------
# File Name: start.py
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

from pyrogram import filters
from devgagan import app
from config import OWNER_ID
from devgagan.core.func import subscribe
import asyncio
from devgagan.core.func import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
 
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("You are not authorized to use this command.")
        return
     
    await app.set_bot_commands([
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("batch", "🫠 Extract in bulk"),
        BotCommand("login", "🔑 Get into the bot"),
        BotCommand("logout", "🚪 Get out of the bot"),
        BotCommand("token", "🎲 Get 3 hours free access"),
        BotCommand("adl", "👻 Download audio from 30+ sites"),
        BotCommand("dl", "💀 Download videos from 30+ sites"),
        BotCommand("freez", "🧊 Remove all expired user"),
        BotCommand("pay", "₹ Pay now to get subscription"),
        BotCommand("status", "⟳ Refresh Payment status"),
        BotCommand("transfer", "💘 Gift premium to others"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("add", "➕ Add user to premium"),
        BotCommand("rem", "➖ Remove from premium"),
        BotCommand("session", "🧵 Generate Pyrogramv2 session"),
        BotCommand("settings", "⚙️ Personalize things"),
        BotCommand("stats", "📊 Get stats of the bot"),
        BotCommand("plan", "🗓️ Check our premium plans"),
        BotCommand("terms", "🥺 Terms and conditions"),
        BotCommand("speedtest", "🚅 Speed of server"),
        BotCommand("lock", "🔒 Protect channel from extraction"),
        BotCommand("gcast", "⚡ Broadcast message to bot users"),
        BotCommand("help", "❓ If you're a noob, still!"),
        BotCommand("cancel", "🚫 Cancel batch process")
    ])
 
    await message.reply("✅ Commands configured successfully!")
 
 
 
 
help_pages = [
    (
        "📝 **Bot Commands Overview (1/2)**:\n\n"
        "1. **/add userID**\n"
        "> Add user to premium (Owner only)\n\n"
        "2. **/rem userID**\n"
        "> Remove user from premium (Owner only)\n\n"
        "3. **/get**\n"
        "> Get all user IDs (Owner only)\n\n"
        "4. **/lock**\n"
        "> Lock channel from extraction (Owner only)\n\n"
        "5. **/dl link**\n"
        "> Download videos (Not available Now)\n\n"
        "6. **/adl link**\n"
        "> Download audio (Not available Now)\n\n"
        "7. **/login**\n"
        "> Log into the bot for private channel access\n\n"
        "8. **/batch**\n"
        "> Bulk extraction for posts (After login)\n\n"
    ),
    (
        "📝 **Bot Commands Overview (2/2)**:\n\n"
        "9. **/logout**\n"
        "> Logout from the bot\n\n"
        "10. **/stats**\n"
        "> Get bot stats\n\n"
        "11. **/plan**\n"
        "> Check premium plans\n\n"
        "12. **/speedtest**\n"
        "> Test the server speed (not available Now)\n\n"
        "13. **/terms**\n"
        "> Terms and conditions\n\n"
        "14. **/cancel**\n"
        "> Cancel ongoing batch process\n\n"
        "15. **/myplan**\n"
        "> Get details about your plans\n\n"
        "16. **/session**\n"
        "> Generate Pyrogram V2 session\n\n"
        "17. **/settings**\n"
        "> 1. SETCHATID : To directly upload in channel or group or user's dm use it with -100[chatID]\n"
        "> 2. SETRENAME : To add custom rename tag or username of your channels\n"
        "> 3. CAPTION : To add custom caption\n"
        "> 4. REPLACEWORDS : Can be used for words in deleted set via REMOVE WORDS\n"
        "> 5. RESET : To set the things back to default\n\n"
        "> You can set CUSTOM THUMBNAIL, PDF WATERMARK, VIDEO WATERMARK, SESSION-based login, etc. from settings\n\n"
        "**__Powered by Team SONU__**"
    )
]
 
 
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return
 
     
    prev_button = InlineKeyboardButton("◀️ Previous", callback_data=f"help_prev_{page_number}")
    next_button = InlineKeyboardButton("Next ▶️", callback_data=f"help_next_{page_number}")
 
     
    buttons = []
    if page_number > 0:
        buttons.append(prev_button)
    if page_number < len(help_pages) - 1:
        buttons.append(next_button)
 
     
    keyboard = InlineKeyboardMarkup([buttons])
 
     
    await message.delete()
 
     
    await message.reply(
        help_pages[page_number],
        reply_markup=keyboard
    )
 
 
@app.on_message(filters.command("help"))
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
 
     
    await send_or_edit_help_page(client, message, 0)
 
 
@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def on_help_navigation(client, callback_query):
    action, page_number = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])
 
    if action == "prev":
        page_number -= 1
    elif action == "next":
        page_number += 1
 
     
    await send_or_edit_help_page(client, callback_query.message, page_number)
 
     
    await callback_query.answer()
 
 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "> 📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/sonuporsa")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)
 
@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    plan_text = (
        "💎 **Upgrade to Premium Plans** 💎\n\n"
        "Choose a plan to see full details:\n\n"
        "🔹 Basic Plan – 300 files\n"
        "🔸 Medium Plan – 500 files\n"
        "🔶 Pro Plan – 1000 files\n\n"
        "👇 Tap a button below to view plans:"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔹 Buy Basic", callback_data="buy_basic")],
            [InlineKeyboardButton("🔸 Buy Medium", callback_data="buy_medium")],
            [InlineKeyboardButton("🔶 Buy Pro", callback_data="buy_pro")],
        ]
    )

    await message.reply_text(plan_text, reply_markup=buttons)


# Callback: See Plan (also shown via "see_plan" button if used elsewhere)
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
        "💎 **Upgrade to Premium Plans** 💎\n\n"
        "Choose a plan to see full details:\n\n"
        "🔹 Basic Plan – 300 files\n"
        "🔸 Medium Plan – 500 files\n"
        "🔶 Pro Plan – 1000 files\n\n"
        "👇 Tap a button below to view plans:"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔹 Buy Basic", callback_data="buy_basic")],
            [InlineKeyboardButton("🔸 Buy Medium", callback_data="buy_medium")],
            [InlineKeyboardButton("🔶 Buy Pro", callback_data="buy_pro")],
        ]
    )

    await callback_query.message.edit_text(plan_text, reply_markup=buttons)


# Callback: Buy Basic Plan
@app.on_callback_query(filters.regex("buy_basic"))
async def buy_basic_plan(client, callback_query):
    text = (
        "💎 **Upgrade to Premium** 💎\n\n"
        "🚀 **Exclusive Premium Basic Features**\n"
        "✅ No need to verify every 3 hours ⏳\n"
        "✅ Bulk mode: Upload up to 300 files 📂\n"
        "✅ Unlimited Leeches\n\n"

        "🪙 **10-Day Plan**\n"
        "💰 Rs 30 🇮🇳 / **$0.36 USDT**\n\n"
        "🪙 **20-Day Plan**\n"
        "💰 Rs 60 🇮🇳 / **$0.72 USDT**\n\n"
        "🪙 **Monthly Plan**\n"
        "💰 Rs 90 🇮🇳 / **$1.08 USDT**\n\n"

        "📌 **Payment Methods**:\n"
        "- QR Code: [Click Here for QR](https://ar-hosting.pages.dev/1751282168015.jpg)\n"
        "- For International payment, Contact Admin\n\n"

        "📤 **After Payment**:\n"
        "1️⃣ Send a payment screenshot below 👇\n"
        "2️⃣ Contact: Admin to complete your purchase 🤝\n\n"
        "💌 We're here for you! 💕"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧾 Get QR Code", url="https://ar-hosting.pages.dev/1751282168015.jpg")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/sonuporsa")],
            [InlineKeyboardButton("⬅️ Back to Plans", callback_data="see_plan")],
        ]
    )

    await callback_query.message.edit_text(text, reply_markup=buttons, disable_web_page_preview=True)


# Callback: Buy Medium Plan
@app.on_callback_query(filters.regex("buy_medium"))
async def buy_medium_plan(client, callback_query):
    text = (
        "💎 **Upgrade to Premium** 💎\n\n"
        "🚀 **Exclusive Premium Medium Features**\n"
        "✅ No need to verify every 3 hours ⏳\n"
        "✅ Bulk mode: Upload up to 500 files 📂\n"
        "✅ Priority Admin Support\n"
        "✅ Unlimited Leeches\n\n"

        "🪙 **10-Day Plan**\n"
        "💰 Rs 50 🇮🇳 / **$0.60 USDT**\n\n"
        "🪙 **20-Day Plan**\n"
        "💰 Rs 100 🇮🇳 / **$1.20 USDT**\n\n"
        "🪙 **Monthly Plan**\n"
        "💰 Rs 130 🇮🇳 / **$1.56 USDT**\n\n"

        "📌 **Payment Methods**:\n"
        "- QR Code: [Click Here for QR](https://ar-hosting.pages.dev/1751282168015.jpg)\n"
        "- For International payment, Contact Admin\n\n"

        "📤 **After Payment**:\n"
        "1️⃣ Send a payment screenshot below 👇\n"
        "2️⃣ Contact: Admin to complete your purchase 🤝\n\n"
        "💌 We're here for you! 💕"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧾 Get QR Code", url="https://ar-hosting.pages.dev/1751282168015.jpg")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/sonuporsa")],
            [InlineKeyboardButton("⬅️ Back to Plans", callback_data="see_plan")],
        ]
    )

    await callback_query.message.edit_text(text, reply_markup=buttons, disable_web_page_preview=True)


# Callback: Buy Pro Plan
@app.on_callback_query(filters.regex("buy_pro"))
async def buy_pro_plan(client, callback_query):
    text = (
        "💎 **Upgrade to Premium** 💎\n\n"
        "🚀 **Exclusive Premium Pro Features**\n"
        "✅ No need to verify every 3 hours ⏳\n"
        "✅ Bulk mode: Upload up to 1000 files 📂\n"
        "✅ Priority Admin Support\n"
        "✅ Unlimited Leeches\n\n"

        "🪙 **10-Day Plan**\n"
        "💰 Rs 100 🇮🇳 / **$1.20 USDT**\n\n"
        "🪙 **20-Day Plan**\n"
        "💰 Rs 200 🇮🇳 / **$2.40 USDT**\n\n"
        "🪙 **Monthly Plan**\n"
        "💰 Rs 280 🇮🇳 / **$3.36 USDT**\n\n"

        "📌 **Payment Methods**:\n"
        "- QR Code: [Click Here for QR](https://ar-hosting.pages.dev/1751282168015.jpg)\n"
        "- For International payment, Contact Admin\n\n"

        "📤 **After Payment**:\n"
        "1️⃣ Send a payment screenshot below 👇\n"
        "2️⃣ Contact: Admin to complete your purchase 🤝\n\n"
        "💌 We're here for you! 💕"
    )

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧾 Get QR Code", url="https://ar-hosting.pages.dev/1751282168015.jpg")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/sonuporsa")],
            [InlineKeyboardButton("⬅️ Back to Plans", callback_data="see_plan")],
        ]
    )

    await callback_query.message.edit_text(text, reply_markup=buttons, disable_web_page_preview=True)
