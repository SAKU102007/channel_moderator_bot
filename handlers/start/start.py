from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.content_manager_keyboard_main_menu import content_manager_keyboard_main_menu
from db_handler.user_role.check_user_role import check_db_user_role


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = int(message.from_user.id)
    check_user_role = await check_db_user_role(user_id=user_id)

    if check_user_role == 'admin':
        await bot.send_message(message.from_user.id, 'Вы админ',
                               reply_markup=admin_panel_keyboard_main_menu)
    elif check_user_role == 'content_manager':
        await bot.send_message(message.from_user.id, 'Вы контент менеджер',
                               reply_markup=content_manager_keyboard_main_menu)
    else:
        await bot.send_message(message.from_user.id, 'Вас нет в базе данных')