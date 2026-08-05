from aiogram import types

admin_panel_keyboard_take_user_role = types.InlineKeyboardMarkup()

admin_panel_button_role_admin = types.InlineKeyboardButton('Администратор',
                                                           callback_data='take_user_role_admin')
admin_panel_button_role_content_manager = types.InlineKeyboardButton('Контент менеджер',
                                                           callback_data='take_user_role_content_manager')

admin_panel_keyboard_take_user_role.row(admin_panel_button_role_admin,
                                        admin_panel_button_role_content_manager)