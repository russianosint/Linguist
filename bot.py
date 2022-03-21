import asyncio

from aiogram import executor

from loader import db, dp

db.create_database()


async def check_settings():
  locales = ['en', 'ru', 'de']
  try:
    for locale in locales:
      if locale not in db.get_locales():
        db.create_locale(locale)
  except:
    print('[*] Fail create locale')


if __name__=='__main__':
  import handlers
  loop = asyncio.get_event_loop()
  loop.create_task(check_settings())
  executor.start_polling(dp)
