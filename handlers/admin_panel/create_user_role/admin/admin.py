from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


class FSM_create_user_role_admin(StatesGroup):
    user_id = State()


@dp.callback_query_handler(text='take_user_role_admin', state=None)
async def load_user_role_admin(callback_query: types.CallbackQuery):
    await FSM_create_user_role_admin.user_id.set()

    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           'Роль успешно выбрана\nПришлите ID пользователя, которого хотите добавить')


@dp.message_handler(state=FSM_create_user_role_admin)
async def load_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text

    await state.finish()
    await bot.delete_message(message.from_user.id, message_id=message.message_id)
    await bot.send_message(message.from_user.id,
                           f'Администратор с ID {data["user_id"]} успешно добавлен',
                           reply_markup=admin_panel_keyboard_back_to_main_menu)
