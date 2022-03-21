import sqlite3


class DBManager:


  def __init__(self, directory):
    self.connection = sqlite3.connect(directory)
    self.cursor = self.connection.cursor()

  def create_database(self):
    """Создание начальной базы данных"""
    with self.connection:
      self.cursor.execute("""CREATE TABLE IF NOT EXISTS settings(choose_locale STR)""")
      self.cursor.execute("""CREATE TABLE IF NOT EXISTS locales(locale STR)""")

  
  def change_locale(self, choose):
    """Смена языка в настройках"""
    with self.connection:
      if self.cursor.execute("""SELECT choose_locale FROM settings""").fetchone():
        self.cursor.execute("""UPDATE settings SET choose_locale = ?""", (choose, ))
      else:
        self.cursor.execute("""INSERT INTO settings VALUES (?)""", (choose, ))

  def get_locales(self):
    """Получить список всех языков"""
    with self.connection:
      data = self.cursor.execute("""SELECT * FROM locales""").fetchall()
      locales = []
      for el in data:
        locales.append(el[0])
      return locales
  
  def get_locale(self):
    """Получить язык из настроек"""
    with self.connection:
      return self.cursor.execute("""SELECT choose_locale FROM settings""").fetchone()[0]

  def create_locale(self, locale):
    """Создание нового языка"""
    with self.connection:
      self.cursor.execute("""INSERT INTO locales(locale) VALUES (?)""", (locale, ))