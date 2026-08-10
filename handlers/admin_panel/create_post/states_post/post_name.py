from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post


@dp.message_handler(state=FSM_create_post.post_name)
async def post_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_name'] = message.html_text
        await FSM_create_post.next()
        await bot.send_message(message.from_user.id, f'Название поста: {data["post_name"]}\n'
                                                     f'Введите описание поста:',
                               reply_markup=admin_panel_keyboard_back_to_main_menu, parse_mode='HTML')
