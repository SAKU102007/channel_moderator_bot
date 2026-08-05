from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    user_id = str(message.from_user.id)

    if user_id == ADMIN:
        await bot.send_message(message.from_user.id, 'Вы админ', reply_markup=admin_panel_keyboard_main_menu)
    else:
        await bot.send_message(message.from_user.id, 'Вы не админ')