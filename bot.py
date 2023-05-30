import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from core.config import config
from core.handlers.basic import get_inline


async def start_bot(bot: Bot):
    await bot.send_message(config.bot.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(config.bot.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=config.bot.bot_token, parse_mode='HTML')
    dp = Dispatcher(bot=bot)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_inline, Command(commands=['start']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
