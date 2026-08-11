from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from db_handler.change_post.change_post import change_post
from db_handler.create_post.check_user_name import check_db_user_name
import datetime


@dp.message_handler(content_types=['photo'], state=FSM_change_post.post_image)
async def post_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_image'] = message.photo[0].file_id

        post_name = str(data['post_name'])
        post_description = str(data['post_description'])
        post_tag = str(data['post_tag'])
        post_image = str(data['post_image'])
        post_id = int(data['post_id'])
        user_id = int(message.from_user.id)
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))

        await state.finish()
        user_name = await check_db_user_name(user_id=user_id)
        await change_post(post_name=post_name, post_description=post_description, post_tag=post_tag,
                          post_image=post_image, change_user_name=user_name, change_date=cur_date,
                          change_time=cur_time, post_id=post_id)

        await bot.send_message(message.from_user.id, f'ID поста: {post_id}\n'
                                                     f'Новое название поста: {post_name}\n'
                                                     f'Новое описание поста: {post_description}\n'
                                                     f'Новый тег поста: {post_tag}\n'
                                                     f'Пост успешно изменен',
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
