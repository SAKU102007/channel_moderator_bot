from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


class FSM_create_user_role_content_manager(StatesGroup):
    user_id = State()


@dp.callback_query_handler(text='take_user_role_content_manager', state=None)
async def load_user_role_content_manager(callback_query: types.CallbackQuery):
    await FSM_create_user_role_content_manager.user_id.set()

    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           'Роль успешно выбрана\nПришлите ID пользователя, которого хотите добавить')


@dp.message_handler(state=FSM_create_user_role_content_manager)
async def load_user_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
        str_user_id = data['user_id']

        try:
            int_user_id = int(str_user_id)

            if int_user_id < 0:
                await state.finish()
                await bot.send_message(message.from_user.id, f'Отрицательный ID пользователя недопустим!\n'
                                                             f'Вы ввели следующий ID: {str_user_id}\n'
                                                             f'Попробуйте еще раз',
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
            else:
                await state.finish()
                await bot.send_message(message.from_user.id, f'Контент менеджер с ID {str_user_id} успешно добавен',
                                       reply_markup = admin_panel_keyboard_back_to_main_menu)
        except ValueError:
            await state.finish()
            await bot.send_message(message.from_user.id, 'ID должен содержать только цифры!\n'
                                                         f'Вы ввели следующий ID: {str_user_id}\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
