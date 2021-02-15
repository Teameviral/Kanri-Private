from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from kanri import kanri

prvt_message = '''
Hey there! My name is Kanri - I'm here to help you manage your groups!
Click Help button to find out more about how to use me to my full potential.
Join [the bot support group](https://t.me/KanriGroup) if you need any bot support or help.
Follow [Kanri](https://t.me/KanriUpdates) if you want to keep up with the bot news, bot updates and bot downtime!
Made with love by @Intellivoid.
'''

grp_message = '''
Hello there! I'm Kanri.
'''

@kanri.on_message(~filters.me & filters.command('start', prefixes='/'), group=8)
async def start(client, message):
    self = await kanri.get_me()
    bothandle = self.username
    if message.chat.type != "private":
        await message.reply_text(grp_message)
        return
    else:
        buttons = [[InlineKeyboardButton("Add to group", url=f"t.me/{bothandle}?startgroup=true"),
                    InlineKeyboardButton('Help', callback_data='help_back')]]
        await message.reply_text(prvt_message, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)