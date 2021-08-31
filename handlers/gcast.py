import asyncio
import os
import subprocess
import time

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

import psutil
from pyrogram import filters
from pyrogram import Client
from pyrogram.errors import FloodWait
from config import SUDO_USERS

@Client.on_message(
    filters.command("gcast")
    & filters.user(SUDO_USERS)
    & ~filters.edited
)
async def gcast(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await edit_or_reply(event, "This Command Is Sudo Restricted.")
    xx = event.pattern_match.group(1)
    if not xx:
        return edit_or_reply(event, "Give some text to Globally Broadcast")
    tt = event.text
    msg = tt[6:]
    event = await edit_or_reply(event, "Globally Broadcasting Msg...")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")
