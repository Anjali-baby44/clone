import random
from typing import Union
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PritiMusic import app
from PritiMusic.utils.formatters import time_to_seconds

# 🔥 PREMIUM EMOJIS LIST 🔥
PREMIUM_EMOJIS = [
    "5422831825178206894", 
    "5368324170673489600",
    "5206607081334906820",
    "5206380668048496464"
]

# 🎨 Dynamic Color Generator (Random Styles)
def get_style_map():
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    random.shuffle(styles)
    # Row me buttons ke hisaab se random color assign hoga
    return {1: styles[0], 2: styles[1], 3: styles[2]}

# 🔘 Smart Button Creator
def create_btn(text, callback_data=None, url=None, user_id=None, style=ButtonStyle.PRIMARY, no_emoji=False):
    kwargs = {"text": text, "style": style}
    if callback_data: kwargs["callback_data"] = callback_data
    if url: kwargs["url"] = url
    if user_id: kwargs["user_id"] = user_id
    if not no_emoji: kwargs["icon_custom_emoji_id"] = random.choice(PREMIUM_EMOJIS)
    return InlineKeyboardButton(**kwargs)


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    s_map = get_style_map()
    not_dur = [
        [
            create_btn(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=s_map[1]
            ),
            create_btn(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=s_map[1]
            ),
        ]
    ]
    dur_list = [
        [
            create_btn(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=s_map[1]
            )
        ],
        [
            create_btn(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=s_map[2]
            ),
            create_btn(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=s_map[2]
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_list)
    return upl


def queue_back_markup(_, CPLAY):
    s_map = get_style_map()
    upl = InlineKeyboardMarkup(
        [
            [
                create_btn(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=s_map[1]
                ),
                create_btn(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=s_map[1]
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    s_map = get_style_map()
    buttons = [
        [
            # Media controls me emoji off rakha hai clean UI ke liye
            create_btn(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=s_map[1], no_emoji=True),
            create_btn(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=s_map[1], no_emoji=True),
            create_btn(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=s_map[1], no_emoji=True),
            create_btn(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=s_map[1], no_emoji=True),
            create_btn(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=s_map[1], no_emoji=True),
        ],
        [
            create_btn(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=s_map[2]
            ),
        ],
    ]
    return buttons


def queuemarkup(_, vidid, chat_id):
    s_map = get_style_map()
    buttons = [
        [
            create_btn(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=s_map[1]
            ),
        ],
        [
            create_btn(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=s_map[2]
            ),
            create_btn(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}", style=s_map[2]),
            create_btn(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}", style=s_map[2]),
        ],
        [
            create_btn(
                text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}", style=s_map[3]
            ),
            create_btn(
                text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}", style=s_map[3]
            ),
        ],
        [
            create_btn(
                text="๏ ᴍᴏʀᴇ ๏",
                url="https://t.me/betabot_hub",
                style=s_map[1] # Loop back to style 1
            ),
        ],
    ]

    return buttons
