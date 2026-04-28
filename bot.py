import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    BotCommand,
)
from aiogram.utils.markdown import hbold

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ─── Клавиатуры ───────────────────────────────────────────────────────────────

def main_reply_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Меню"), KeyboardButton(text="ℹ️ О боте")],
            [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="📞 Контакты")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери раздел...",
    )

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

# ─── Команды ──────────────────────────────────────────────────────────────────

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {hbold(message.from_user.full_name)}!\n\n"
        "Я бот с удобным меню. Используй кнопки ниже или команды:\n"
        "/menu — открыть меню\n"
        "/help — помощь\n"
        "/about — о боте",
        reply_markup=main_reply_keyboard(),
        parse_mode="HTML",
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "🆘 <b>Помощь</b>\n\n"
        "Доступные команды:\n"
        "/start — начать работу\n"
        "/menu — открыть инлайн-меню\n"
        "/about — информация о боте\n"
        "/help — эта справка\n\n"
        "Также можно использовать кнопки внизу экрана 👇",
        parse_mode="HTML",
    )

@dp.message(Command("menu"))
@dp.message(F.text == "📋 Меню")
async def cmd_menu(message: Message):
    await message.answer(
        "📋 <b>Главное меню</b>\n\nВыбери раздел:",
        reply_markup=inline_menu(),
        parse_mode="HTML",
    )

@dp.message(Command("about"))
@dp.message(F.text == "ℹ️ О боте")
async def cmd_about(message: Message):
    await message.answer(
        "ℹ️ <b>О боте</b>\n\n"
        "Версия: 1.0.0\n"
        "Создан на: aiogram 3.x\n"
        "Хостинг: Render\n\n"
        "Разработан как шаблон для быстрого старта.",
        parse_mode="HTML",
    )

@dp.message(F.text == "⚙️ Настройки")
async def settings_handler(message: Message):
    await message.answer(
        "⚙️ <b>Настройки</b>\n\n"
        "Здесь будут настройки бота.\n"
        "Добавьте свою логику!",
        parse_mode="HTML",
    )

@dp.message(F.text == "📞 Контакты")
async def contacts_handler(message: Message):
    await message.answer(
        "📞 <b>Контакты</b>\n\n"
        "Email: your@email.com\n"
        "Telegram: @yourhandle",
        parse_mode="HTML",
    )

# ─── Инлайн-кнопки ────────────────────────────────────────────────────────────

@dp.callback_query(F.data == "section_1")
async def section_1(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 <b>Раздел 1</b>\n\nЭто содержимое первого раздела.\nДобавьте свою логику здесь!",
        reply_markup=back_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()

@dp.callback_query(F.data == "section_2")
async def section_2(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ <b>Раздел 2</b>\n\nЭто содержимое второго раздела.\nДобавьте свою логику здесь!",
        reply_markup=back_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()

@dp.callback_query(F.data == "section_3")
async def section_3(callback: CallbackQuery):
    await callback.message.edit_text(
        "📊 <b>Раздел 3</b>\n\nЭто содержимое третьего раздела.\nДобавьте свою логику здесь!",
        reply_markup=back_keyboard(),
        parse_mode="HTML",
    )
    await callback.answer()

@dp.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "📋 <b>Главное меню</b>\n\nВыбери раздел:",
        reply_markup=inline_menu(),
        parse_mode="HTML",
    )
    await callback.answer()

@dp.callback_query(F.data == "close")
async def close_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer("Меню закрыто")

# ─── Эхо (на все остальные сообщения) ────────────────────────────────────────

@dp.message()
async def echo(message: Message):
    await message.answer(
        f"🤖 Ты написал: {message.text}\n\nИспользуй /help или кнопки меню.",
        reply_markup=main_reply_keyboard(),
    )

# ─── Запуск ───────────────────────────────────────────────────────────────────

async def set_commands():
    commands = [
        BotCommand(command="start", description="Начать работу"),
        BotCommand(command="menu", description="Открыть меню"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="about", description="О боте"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_commands()
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
