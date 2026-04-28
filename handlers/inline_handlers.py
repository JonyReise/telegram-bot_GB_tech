from aiogram import F
from aiogram.types import CallbackQuery
from keyboards.inline import inline_menu, back_keyboard

def register_inline_handlers(dp):
    @dp.callback_query(F.data == "section_1")
    async def section_1(callback: CallbackQuery):
        await callback.message.edit_text(
            "🚀 Раздел 1: добавь свою логику!",
            reply_markup=back_keyboard(),
            parse_mode="HTML",
        )
        await callback.answer()

    @dp.callback_query(F.data == "section_2")
    async def section_2(callback: CallbackQuery):
        await callback.message.edit_text(
            "⭐ Раздел 2: добавь свою логику!",
            reply_markup=back_keyboard(),
            parse_mode="HTML",
        )
        await callback.answer()

    @dp.callback_query(F.data == "section_3")
    async def section_3(callback: CallbackQuery):
        await callback.message.edit_text(
            "📊 Раздел 3: добавь свою логику!",
            reply_markup=back_keyboard(),
            parse_mode="HTML",
        )
        await callback.answer()

    @dp.callback_query(F.data == "back_to_menu")
    async def back_to_menu(callback: CallbackQuery):
        await callback.message.edit_text(
            "📋 Главное меню",
            reply_markup=inline_menu(),
            parse_mode="HTML",
        )
        await callback.answer()

    @dp.callback_query(F.data == "close")
    async def close_menu(callback: CallbackQuery):
        await callback.message.delete()
        await callback.answer("Меню закрыто")
