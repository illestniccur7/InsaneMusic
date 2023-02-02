import asyncio
import math
import os
import shutil
import socket
import traceback
import psutil
import config
from pyrogram import Client, filters
from pyrogram.types import Message
from InsaneMusic  import app
from InsaneMusic .utils.database.memorydatabase import (active, activevideo)
from InsaneMusic .misc import SUDOERS
from InsaneMusic .utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#


LOGINGG = config.LOG_GROUP_ID


#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 📟\n•━━━━━━━━━━━━━━━━━━•\n🎙•Aᴜᴅɪᴏ  » {ac_audio} Gʀᴏᴜᴘs\n•───────•\n🖥• Vɪᴅᴇᴏ » {ac_video} Gʀᴏᴜᴘs\n•──────•", quote=True)


#--------------------------Clean_Commands------------------------#

@app.on_message(avoice(["/rm"]) & SUDOERS)
async def cleaning(client: Client, message: Message):
    A = 'rm -rf downloads'
    try:
        os.system(A)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Downloads", quote=True)

    
CPU_LOAD = psutil.cpu_percent(interval=0.5)
RAM_LOAD = psutil.virtual_memory().percent
DISK_SPACE = psutil.disk_usage("/").percent


#-----------------------------AUTO_CLEANER-&-SAFETY-------------------------------#
