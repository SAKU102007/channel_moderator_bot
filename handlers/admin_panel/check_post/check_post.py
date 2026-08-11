from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_check_post(StatesGroup):
    post_id = State()


@dp.callback_query_handler(text='check_post')
async def admin_panel_delete_post_callback(callback_query: types.CallbackQuery):
    await FSM_check_post.post_id.set()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, f'Пришлите ID поста:',
                           reply_markup=admin_panel_keyboard_back_to_main_menu)
