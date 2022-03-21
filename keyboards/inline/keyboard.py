from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db



menu_languages_cd = CallbackData("show_menu_languages", "locale")


def make_callback_data(locale="-"):
  """Формирование callback data для кнопок"""
  return menu_languages_cd.new(locale=locale)


def languages_keyboard():
  """Формирование клавиатуры выбора языка"""

  markup = InlineKeyboardMarkup(row_width=3)

  locales = db.get_locales()

  for locale in locales:
    button = InlineKeyboardButton(text=locale, callback_data=make_callback_data(locale=locale))
    markup.insert(button)

  return markup