import os
from pathlib import Path
from uuid import uuid4

from aiogram import types
from keyboards.default.keyboard import menu_keyboard
from loader import bot, dp
from utils.speech_to_text import (audio_to_video, speech_to_text,
                                  text_to_speech, video_to_audio)


@dp.message_handler(commands='start')
async def start(message: types.Message):
  markup = await menu_keyboard()
  await message.answer(f"""
Добро пожаловать, <b>{message.from_user.full_name}</b>
""", reply_markup = markup)



async def handle_file(file: types.File, file_name: str, path):

  Path(f"{path}").mkdir(parents=True, exist_ok=True)
  destination =f"{path}/{file_name}"

  await bot.download_file(file_path=file.file_path, destination=destination)

  return destination


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(message: types.Message):
  voice = await message.voice.get_file()

  path = await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path="voices")
  text = speech_to_text(path)
  audio = text_to_speech(text)

  await message.reply_audio(types.InputFile(audio))

  os.remove(audio)
  os.remove(path)



@dp.message_handler(content_types=types.ContentTypes.VIDEO_NOTE)
async def video_handler(message: types.Message):
  video = await message.video_note.get_file()
  path = await handle_file(file=video, file_name=f"{uuid4()}.mp4", path="videos")

  audio_path = video_to_audio(path)
  text = speech_to_text(audio_path)
  audio = text_to_speech(text)
  new_video = audio_to_video(audio_path=audio, video_path=path)

  await message.reply_video_note(types.InputFile(new_video))

  os.remove(path)
  os.remove(new_video)
  os.remove(audio_path)
  os.remove(audio)


@dp.channel_post_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(message: types.Message):

  voice = await message.voice.get_file()

  path = await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path="voices")
  text = speech_to_text(path)
  audio = text_to_speech(text)

  await message.reply_audio(types.InputFile(audio))

  os.remove(audio)
  os.remove(path)



@dp.channel_post_handler(content_types=types.ContentTypes.VIDEO_NOTE)
async def video_handler(message: types.Message):
  video = await message.video_note.get_file()
  path = await handle_file(file=video, file_name=f"{uuid4()}.mp4", path="videos")

  audio_path = video_to_audio(path)
  text = speech_to_text(audio_path)
  audio = text_to_speech(text)
  new_video = audio_to_video(audio_path=audio, video_path=path)

  await message.reply_video_note(types.InputFile(new_video))

  os.remove(path)
  os.remove(new_video)
  os.remove(audio_path)
  os.remove(audio)

