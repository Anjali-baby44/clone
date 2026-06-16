import random
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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


# --- OPTION 1: Static ---
s_map_static = get_style_map()

buttons = InlineKeyboardMarkup(
    [
        [
            create_btn(text="▷", callback_data="resume_cb", style=s_map_static[1], no_emoji=True),
            create_btn(text="II", callback_data="pause_cb", style=s_map_static[1], no_emoji=True),
            create_btn(text="‣‣I", callback_data="skip_cb", style=s_map_static[1], no_emoji=True),
            create_btn(text="▢", callback_data="end_cb", style=s_map_static[1], no_emoji=True),
        ],
        [
            create_btn(text="『 ✦ 𝐂ʟᴏηє 𝐌є ✦ 』", url="https://t.me/clone_MUSICrobot", style=s_map_static[2])
        ],
    ]
)

close_key = InlineKeyboardMarkup(
    [
        [
            create_btn(text="『 ♡ 𝐀ᴅᴅ 𝐌є 𝐁ᴀʙʏ ♡ 』", url="https://t.me/clone_MUSICrobot?startgroup=true", style=s_map_static[1]),
            create_btn(text="✯ CLOSE ✯", callback_data="close", style=s_map_static[2], no_emoji=True)
        ]
    ]
)


# --- OPTION 2: Dynamic (RECOMMENDED) ---
def stream_markup(chat_id):
    s_map = get_style_map()
    return InlineKeyboardMarkup(
        [
            # Top Row: Basic Controls
            [
                create_btn(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=s_map[1], no_emoji=True),
                create_btn(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=s_map[1], no_emoji=True),
                create_btn(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=s_map[1], no_emoji=True),
                create_btn(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=s_map[1], no_emoji=True),
            ],
            # Middle Row: Seek, Loop & Shuffle
            [
                create_btn(text="<- 20s", callback_data=f"ADMIN SeekBack|{chat_id}", style=s_map[2], no_emoji=True),
                create_btn(text="🔁", callback_data=f"ADMIN Loop|{chat_id}", style=s_map[2], no_emoji=True),
                create_btn(text="🔀", callback_data=f"ADMIN Shuffle|{chat_id}", style=s_map[2], no_emoji=True),
                create_btn(text="20s + ->", callback_data=f"ADMIN SeekForward|{chat_id}", style=s_map[2], no_emoji=True),
            ],
            # Bottom Row 1: Clone
            [
                create_btn(text="『 ✦ 𝐂ʟᴏηє 𝐌є ✦ 』", url="https://t.me/clone_MUSICrobot", style=s_map[3])
            ],
            # Bottom Row 2: Add Me & Close
            [
                create_btn(text="『 ♡ 𝐀ᴅᴅ 𝐌є 𝐁ᴀʙʏ ♡ 』", url="https://t.me/clone_MUSICrobot?startgroup=true", style=s_map[1]),
                create_btn(text="✯ CLOSE ✯", callback_data="close", style=s_map[2], no_emoji=True)
            ]
        ]
    )
