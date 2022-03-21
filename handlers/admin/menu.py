from aiogram import types
from filters.is_admin import IsAdmin
from keyboards.default.keyboard import admin_menu_keyboard, menu_keyboard
from keyboards.inline.keyboard import languages_keyboard, menu_languages_cd
from loader import db, dp


@dp.message_handler(IsAdmin(), commands='admin')
async def admin_panel(message: types.Message):
  markup = await admin_menu_keyboard()
  await message.answer('Привет, админ!', reply_markup=markup)


@dp.message_handler(IsAdmin(), lambda m: m.text == 'Выход')
async def admin_panel(message: types.Message):
  markup = await menu_keyboard()
  await message.answer('Пока, админ!', reply_markup=markup)


@dp.message_handler(IsAdmin(), lambda m: m.text == 'Сменить язык перевода')
async def change_locale(message: types.Message):
  await message.answer('Выберите нужный язык: ', reply_markup=languages_keyboard())

@dp.callback_query_handler(menu_languages_cd.filter())
async def languages_navigate(message: types.CallbackQuery, callback_data: dict):

  db.change_locale(callback_data.get('locale'))
  await message.message.edit_text('Вы успешно сменили язык')
