# created by @youngchris
"""animebot: Avaible commands: .whatanime 
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="whatanime?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@WhatAnimeBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=394963134)
            )
            await event.client.send_message(chat, "anify{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @WhatAnimeBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)
