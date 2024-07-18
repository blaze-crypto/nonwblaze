from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

START = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Tap🖐 and Blaze🔥",
                web_app=WebAppInfo(url="https://localhost:8000/")  #<=======SHU YERGA URL NI YOZASIZ ===================>
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ]
    ]
)

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔥TAP🔥",
                web_app=WebAppInfo(url="https://localhost:8000/") #<=======SHU YERGA URL NI YOZASIZ ===================>
            )
        ],
        [
            InlineKeyboardButton(
                text="Invite Friends",
                callback_data="invite"
            )
        ]
    ]
)
