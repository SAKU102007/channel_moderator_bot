from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from db_handler.change_post.get_post_name import get_post_name


@dp.message_handler(state=FSM_change_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            row = await get_post_name(int(message.text))
            data['post_id'] = message.text
            await FSM_change_post.next()
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Название поста: {row["post_name"]}\n'
                                                         f'Пришлите новое название поста:',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
        except TypeError:
            await state.finish()
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Ошибка! Такого поста не существует\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)