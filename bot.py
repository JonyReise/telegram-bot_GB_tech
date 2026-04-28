import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand

from keyboards.reply import main_reply_keyboard
from handlers.reply_handlers import register_reply_handlers
from handlers.inline_handlers import register_inline_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привіт, {message.from_user.full_name}!",
        reply_markup=main_reply_keyboard(),
    )

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
    register_reply_handlers(dp)
    register_inline_handlers(dp)
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
