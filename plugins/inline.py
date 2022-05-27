#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.handlers import InlineQueryHandler
from youtubesearchpython import VideosSearch
from config import Config
from utils import LOGGER
from pyrogram.types import (
    InlineQueryResultArticle, 
    InputTextMessageContent, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)
from pyrogram import (
    Client, 
    errors
)


buttons = [
    [
        InlineKeyboardButton('🌀 𝖩𝗈𝗂𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 🌀', url='https://t.me/dk_botx'),
        InlineKeyboardButton('✨ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖢𝗁𝖺𝗍 ✨', url='https://t.me/dkbotxchats'),
    ]
    ]
def get_cmd(dur):
    if dur:
        return "/play"
    else:
        return "/stream"
@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "ETHO_ORUTHAN_PM_VANNU":
        answers.append(
            InlineQueryResultArticle(
                title="𝙀𝙉𝙏𝙃𝘼𝘿𝘼 𝙈𝙊𝙒𝙉𝙀",
                input_message_content=InputTextMessageContent(f"{Config.REPLY_MESSAGE}\n\n<b>𝖤𝗇𝗍𝗁𝖺𝖽𝖺 𝗆𝗈𝗐𝗇𝗈𝗈𝗌𝖾 𝗇𝖾𝖾 𝗇𝗈𝗄𝖺𝗇𝖾 , 𝗌𝖺𝗆𝗌𝗁𝖺𝗒𝖺𝗆 𝗈𝗄𝖾 𝖾𝗇𝗍𝖾 𝗆𝗈𝗍𝗁𝖺𝗅𝖺𝗅𝗂𝖽𝖾 𝖺𝖽𝗎𝗍𝗁 [Dᴋ 🇮🇳](https://t.me/aboutme_DK).</b>", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("Search a youtube video"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "{} https://www.youtube.com/watch?v={}".format(get_cmd(v["duration"]), v["id"])
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("Nothing found"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
