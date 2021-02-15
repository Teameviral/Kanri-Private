from pyrogram import filters
from pyrogram.errors import BadRequest
from pyrogram.types import ChatPermissions
from kanri import kanri, CF_API_KEY
import aiohttp, json, asyncio

session = aiohttp.ClientSession()


@kanri.on_message(filters.text & filters.group, group=3)
async def nlp_detect(client, message):
    url = "https://api.intellivoid.net/coffeehouse/v1/nlp/spam_prediction/chatroom"
    user = message.from_user
    chat = message.chat
    msg = message.text
    if CF_API_KEY:
        try:
            payload = {'access_key': CF_API_KEY, 'input': msg}
            data = await session.post(url, data=payload)
            res_json = json.loads(await data.text())
            if res_json['success']:
                spam_check = res_json['results']['spam_prediction']['is_spam']
                if spam_check == True:
                    pred = res_json['results']['spam_prediction']['prediction']
                    await kanri.restrict_chat_member(chat.id, user.id, ChatPermissions(can_send_messages=False))
                    try:
                        await message.reply_text(
                        f"**⚠ SPAM DETECTED!**\nSpam Prediction: `{pred}`\nUser: `{user.id}` was muted.",
                        parse_mode="md",
                    )
                    except BadRequest:
                        await message.reply_text(
                        f"**⚠ SPAM DETECTED!**\nSpam Prediction: `{pred}`\nUser: `{user.id}`\nUser could not be restricted due to insufficient admin perms.",
                        parse_mode="md",
                    )

            elif res_json['error']['error_code'] == 21:
                payload = {'access_key': CF_API_KEY, 'input': msg}
                data = session.post(url, data=payload)
                res_json = json.loads(await data.text())
                spam_check = res_json['results']['spam_prediction']['is_spam']
                if spam_check is True:
                    pred = res_json['results']['spam_prediction']['prediction']
                    await kanri.restrict_chat_member(chat.id, user.id, ChatPermissions(can_send_messages=False))
                    try:
                        await message.reply_text(
                            f"**⚠ SPAM DETECTED!**\nSpam Prediction: `{pred}`\nUser: `{user.id}` was muted.", parse_mode="markdown")
                    except BadRequest:
                        await message.reply_text(f"**⚠ SPAM DETECTED!**\nSpam Prediction: `{pred}`\nUser: `{user.id}`\nUser could not be restricted due to insufficient admin perms.", parse_mode="markdown")
        except (aiohttp.ClientConnectionError, asyncio.TimeoutError):
            log.warning("Can't reach SpamProtection API")
            await asyncio.sleep(0.5)
