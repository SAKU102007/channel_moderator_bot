from aiogram import types

admin_panel_keyboard_back_to_main_menu = types.InlineKeyboardMarkup()

admin_panel_button_main_menu = types.InlineKeyboardButton('Вернуться в главное меню', callback_data='main_menu')

admin_panel_keyboard_back_to_main_menu.row(admin_panel_button_main_menu)
