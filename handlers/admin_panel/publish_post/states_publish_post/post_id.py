from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot, CHAT_ID
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.publish_post.publish_post import FSM_publish_post
from db_handler.get_post.get_post import get_post


@dp.message_handler(state=FSM_publish_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            row = await get_post(int(message.text))
            data['post_id'] = message.text

            await state.finish()
            await bot.send_photo(CHAT_ID, photo=row['post_image'],
                                 caption=f'{row["post_name"]}\n\n'
                                         f'{row["post_description"]}', parse_mode='HTML')
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Название поста: {row["post_name"]}\n'
                                                         f'Описание поста: {row["post_description"]}\n'
                                                         f'Пост был опубликован',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu, parse_mode='HTML')
        except TypeError:
            await state.finish()
            await bot.send_message(message.from_user.id, f'ID поста: {data["post_id"]}\n'
                                                         f'Ошибка! Такого поста не существует\n'
                                                         f'Попробуйте еще раз',
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
