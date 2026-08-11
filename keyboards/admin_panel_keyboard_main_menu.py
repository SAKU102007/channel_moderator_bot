from aiogram import types

admin_panel_keyboard_main_menu = types.InlineKeyboardMarkup()

admin_panel_button_create_post = types.InlineKeyboardButton('Создать пост', callback_data='create_post')
admin_panel_button_delete_post = types.InlineKeyboardButton('Удалить пост', callback_data='delete_post')
admin_panel_button_change_post = types.InlineKeyboardButton('Редактировать пост', callback_data='change_post')
admin_panel_button_make_user_role = types.InlineKeyboardButton('Назначить роль пользователю',
                                                               callback_data='make_user_role')
admin_panel_button_delete_user_role = types.InlineKeyboardButton('Удалить роль у пользователя',
                                                               callback_data='delete_user_role')

admin_panel_keyboard_main_menu.row(admin_panel_button_make_user_role)
admin_panel_keyboard_main_menu.row(admin_panel_button_delete_user_role)
admin_panel_keyboard_main_menu.row(admin_panel_button_create_post, admin_panel_button_delete_post)
admin_panel_keyboard_main_menu.row(admin_panel_button_change_post)
