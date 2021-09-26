from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
      await message.reply_text("""@ELECTRO_UPDATES
/help - """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ßƐSŦĪƐS ZᎾИƐ", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
