from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



async def menu_keyboard():
  """Тестовый пользовательский функицонал"""

  markup = ReplyKeyboardMarkup(resize_keyboard=True)

  markup.add(
    KeyboardButton(text='Профиль'),
    KeyboardButton(text='Статистика'),
    KeyboardButton(text='Настройки'),
  )
  
  return markup


async def admin_menu_keyboard():
  """Тестовый функицонал администратора"""

  markup = ReplyKeyboardMarkup(resize_keyboard=True)

  markup.add(
    KeyboardButton(text='Сменить язык перевода'),
    KeyboardButton(text='Выход')
  )
  
  return markup