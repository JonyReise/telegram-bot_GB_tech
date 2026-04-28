from aiogram import F
from aiogram.types import Message
from keyboards.reply import main_reply_keyboard
from keyboards.inline import inline_menu

def register_reply_handlers(dp):
    @dp.message(F.text == "🔁 Змінити магазин")
    async def cmd_about(message: Message):
        await message.answer(
            "ℹ️ <b>Магазини</b>\n\nавіпвіп",
            parse_mode="HTML",
        )

    @dp.message(F.text == "⚙️ Настройки")
    async def settings_handler(message: Message):
        await message.answer("⚙️ Настройки пока пустые.", parse_mode="HTML")

    @dp.message(F.text == "📞 Контакты")
    async def contacts_handler(message: Message):
        await message.answer("📞 Контакты: @yourhandle", parse_mode="HTML")

    @dp.message(F.text == "📋 Меню")
    async def cmd_menu(message: Message):
        await message.answer(
            "📋 Главное меню",
            reply_markup=inline_menu(),
            parse_mode="HTML",
        )

    @dp.message()
    async def echo(message: Message):
        await message.answer(
            f"🤖 Ты написал: {message.text}",
            reply_markup=main_reply_keyboard(),
        )
