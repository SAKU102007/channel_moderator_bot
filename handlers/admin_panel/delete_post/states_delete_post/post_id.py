from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.delete_post.delete_post import FSM_delete_post
from db_handler.change_post.get_post_name import get_post_name
from db_handler.delete_post.delete_post import delete_post


@dp.message_handler(state=FSM_delete_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            row = await get_post_name(int(message.text))
            data['post_id'] = message.text
            int_post_id = int(data['post_id'])

            await delete_post(post_id=int_post_id)
            await state.finish()
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Название поста: {row["post_name"]}\n'
                                                         f'Пост был удален',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
        except TypeError:
            await state.finish()
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Ошибка! Такого поста не существует\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
