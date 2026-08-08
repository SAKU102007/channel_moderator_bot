from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='main_menu', state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        await bot.send_message(callback_query.from_user.id, 'Вы в главном меню',
                               reply_markup=admin_panel_keyboard_main_menu)
    else:
        await state.finish()
        await bot.delete_message(callback_query.from_user.id, message_id=callback_query.message.message_id)
        await bot.send_message(callback_query.from_user.id, 'Вы в главном меню',
                               reply_markup=admin_panel_keyboard_main_menu)
