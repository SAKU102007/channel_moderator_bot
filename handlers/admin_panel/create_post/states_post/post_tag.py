from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot, CHAT_ID
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post
from db_handler.create_post.create_post import create_post
from db_handler.create_post.check_user_name import check_db_user_name
import datetime


@dp.message_handler(state=FSM_create_post.post_tag)
async def post_tag(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_tag'] = message.html_text
        await state.finish()

        user_id = int(message.from_user.id)
        post_name = str(data['post_name'])
        post_description = str(data['post_description'])
        post_image = str(data['post_image'])
        post_tag = str(data['post_tag'])
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        user_name = await check_db_user_name(user_id=user_id)

        await create_post(post_name=post_name, post_description=post_description, post_tag=post_tag,
                          post_image=post_image, user_name=user_name, create_time=cur_time, create_date=cur_date)

        await bot.send_photo(message.from_user.id, photo=post_image,
                             caption=f'Название поста: {post_name}\n'
                                     f'Текст поста: {post_description}\n'
                                     f'Тэг поста: #{post_tag}\n'
                                     f'Создатель: {user_name}\n'
                                     f'Дата создания: {cur_date}\n'
                                     f'Время создания: {cur_time}\n'
                                     f'Вы успешно создали пост',
                             reply_markup=admin_panel_keyboard_back_to_main_menu, parse_mode='HTML')

        await bot.send_photo(CHAT_ID, photo=post_image, caption=f'{post_name}\n\n'
                                                                f'{post_description}', parse_mode='HTML')
