import os
from uuid import uuid4

import speech_recognition as speech_recog
from googletrans import Translator
from gtts import gTTS
from loader import db
from moviepy.editor import AudioFileClip, VideoFileClip
from pydub import AudioSegment
from speech_recognition import UnknownValueError


def translate_from_to_choose_locale(text):
  """Перевод текста на выбранный язык"""

  translator = Translator()
  result=translator.translate(text=text, dest=db.get_locale())
  
  return result.text


def ogg_to_wav(path):
  """Конвертация файла из ogg в wav"""

  audio = AudioSegment.from_ogg(f'{path}')
  new_path = f'voices/{uuid4()}.wav'
  audio.export(new_path, format='wav')

  return new_path 


def wav_to_ogg(path):
  """Конвертация файла из wav в ogg"""
  audio = AudioSegment.from_file(f'{path}')
  new_path = f'voices/{uuid4()}.ogg'
  audio.export(new_path, format='ogg')

  return new_path 


def video_to_audio(path):
  """Конвертация видео в аудио """
  audio_clip = AudioFileClip(path)
  new_path = f'voices/{uuid4()}.wav'
  audio_clip.write_audiofile(new_path)

  return new_path


def audio_to_video(audio_path, video_path):
  """Смена аудиодорожки в видео"""
  video_clip = VideoFileClip(video_path)
  new_path = f'videos/{uuid4()}.mp4'
  video_clip.write_videofile(new_path, audio=audio_path)

  return new_path


def speech_to_text(path):
  """Преобразование голоса в текст"""
  try:
    new_path = ogg_to_wav(path)
    r = speech_recog.Recognizer()

    with speech_recog.AudioFile(new_path) as source:
      audio = r.record(source)
    text = r.recognize_google(audio, language='ru')
  except UnknownValueError:
    text='Не найдено'
  os.remove(new_path)
  return translate_from_to_choose_locale(text)


def text_to_speech(text):
  """Преобразование текста в голос"""

  s = gTTS(text)
  audio_path = f'voices/{uuid4()}.ogg'
  s.save(audio_path)

  return audio_path
