from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Меню"), KeyboardButton(text="ℹ️ О боте")],
            [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="📞 Контакты")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери раздел...",
    )
