from aiogram.dispatcher.filters.state import State, StatesGroup


class ChangeLocaleState(StatesGroup):

  choose = State()
