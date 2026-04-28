from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Меню"), KeyboardButton(text="🔁 Змінити магазин")],
            [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="📞 Контакты")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери раздел...",
    )
