from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from db_handler.user_role.create_admin import create_admin
from db_handler.user_role.check_user_role import check_db_user_role


class FSM_create_user_role_admin(StatesGroup):
    user_id = State()
    user_name = State()


@dp.callback_query_handler(text='take_user_role_admin', state=None)
async def load_user_role_admin(callback_query: types.CallbackQuery):
    await FSM_create_user_role_admin.user_id.set()

    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           'Роль успешно выбрана\nПришлите ID пользователя, которого хотите добавить')


@dp.message_handler(state=FSM_create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    try:
        check = await check_db_user_role(user_id=int(message.text))

        if check == 'admin':
            await state.finish()
            await bot.send_message(message.from_user.id, f'Данный пользователь уже есть в базе данных\n'
                                                         f'Его роль - Администратор\n'
                                                         f'ID пользователя: {message.text}\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
        elif check == 'content_manager':
            await state.finish()
            await bot.send_message(message.from_user.id, f'Данный пользователь уже есть в базе данных\n'
                                                         f'Его роль - Контент менеджер\n'
                                                         f'ID пользователя: {message.text}\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
        else:
            async with state.proxy() as data:
                data['user_id'] = message.text
                str_user_id = data['user_id']
                int_user_id = int(str_user_id)

            if int_user_id < 0:
                await state.finish()
                await bot.send_message(message.from_user.id, f'Отрицательный ID пользователя недопустим!\n'
                                                             f'Вы ввели следующий ID: {str_user_id}\n'
                                                             f'Попробуйте еще раз',
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
            else:
                await FSM_create_user_role_admin.next()
                await bot.send_message(message.from_user.id, f'Администратор\n'
                                                             f'ID пользователя: {str_user_id}\n'
                                                             f'Отправьте имя пользователя',
                                       reply_markup = admin_panel_keyboard_back_to_main_menu)
    except ValueError:
        await state.finish()
        await bot.send_message(message.from_user.id, 'ID должен содержать только цифры!\n'
                                                     f'Вы ввели следующий ID: {message.text}\n'
                                                     f'Попробуйте еще раз',
                               reply_markup=admin_panel_keyboard_back_to_main_menu)


@dp.message_handler(state=FSM_create_user_role_admin.user_name)
async def load_user_name(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            res = message.text.isdigit()
            int_data_user_id = int(data['user_id'])

            if res:
                await state.finish()
                await bot.send_message(message.from_user.id, f'Вы прислали не строку!\n'
                                                             f'ID пользователя: {int_data_user_id}\n'
                                                             f'Попробуйте еще раз',
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
            else:
                data['user_name'] = message.text
                await create_admin(user_id=int_data_user_id, user_name=data['user_name'])
                await bot.send_message(message.from_user.id, f'Администратор успешно добавлен\n'
                                                             f'ID пользователя: {int_data_user_id}\n'
                                                             f'Имя пользователя: {data["user_name"]}',
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
