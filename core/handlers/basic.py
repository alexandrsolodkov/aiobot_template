from aiogram.types import Message
from aiogram import Bot
from core.keyboards.inline import user_answer


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}',
                         reply_markup=user_answer
                         )
