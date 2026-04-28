from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def inline_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🚀 Раздел 1", callback_data="section_1"),
                InlineKeyboardButton(text="⭐ Раздел 2", callback_data="section_2"),
            ],
            [
                InlineKeyboardButton(text="📊 Раздел 3", callback_data="section_3"),
            ],
            [
                InlineKeyboardButton(text="🔙 Закрыть", callback_data="close"),
            ],
        ]
    )

def back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_menu")]
        ]
    )
