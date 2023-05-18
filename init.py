import os
import time
from pytube import YouTube
from moviepy.editor import *
from pathlib import Path
import pygame

def init():
      # SoundWave Storage

      if not os.path.isdir("C:/SoundWave"):
         os.mkdir('C:/SoundWave')
      if not os.path.isdir("C:/SoundWave/musics"):
         os.mkdir("C:/SoundWave/musics")
      if not os.path.isdir("C:/SoundWave/videos"):
         os.mkdir("C:/SoundWave/videos")