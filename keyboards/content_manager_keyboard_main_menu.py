from aiogram import types

content_manager_keyboard_main_menu = types.InlineKeyboardMarkup()

content_manager_button_create_post = types.InlineKeyboardButton('Создать пост', callback_data='create_post')
content_manager_button_delete_post = types.InlineKeyboardButton('Удалить пост', callback_data='delete_post')
content_manager_button_change_post = types.InlineKeyboardButton('Редактировать пост', callback_data='change_post')
content_manager_button_publish_post = types.InlineKeyboardButton('Опубликовать пост', callback_data='publish_post')
content_manager_button_check_post = types.InlineKeyboardButton('Просмотреть пост', callback_data='check_post')

content_manager_keyboard_main_menu.row(content_manager_button_create_post, content_manager_button_delete_post)
content_manager_keyboard_main_menu.row(content_manager_button_check_post)
content_manager_keyboard_main_menu.row(content_manager_button_change_post)
content_manager_keyboard_main_menu.row(content_manager_button_publish_post)
