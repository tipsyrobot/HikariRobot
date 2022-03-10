import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://telegra.ph/file/5b379775d68c5572ac167.png"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Hikari Robot.** \n\n"
  PRIME += f"🍻 **I'm Working Properly** \n\n"
  PRIME += f"🍻 **My Darling : [ʀᴇxᴧ-ᴇx](https://t.me/JustRex)** \n\n"
  PRIME += f"🍻 **Library Version :** `{telever}` \n\n"
  PRIME += f"🍻 **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"🍻 **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/HikariManageRobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/rexaprivateroom")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
