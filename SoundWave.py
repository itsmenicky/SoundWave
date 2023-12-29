import tkinter as tk
from tkinter import *
import time
import os
import pygame
from pytube import YouTube
from moviepy.editor import *
from pathlib import Path
from youtubesearchpython import VideosSearch
import string 
import sys

output = open("output.txt", "wt")
sys.stdout = output
sys.stderr = output

def startSoundWave():
      # SoundWave Storage

      if not os.path.isdir("C:/SoundWave"):
         os.mkdir('C:/SoundWave')
      if not os.path.isdir("C:/SoundWave/musics"):
         os.mkdir("C:/SoundWave/musics")
      if not os.path.isdir("C:/SoundWave/videos"):
         os.mkdir("C:/SoundWave/videos")

def baixar():

      input = txtBox.get()
      music_isdownloading.place(x=880, y=165)
      music_isdownloading.config(text = "Downloading your music, please wait...")
      janela1.update_idletasks()
         
      # Realiza a busca da música

      pesquisa = VideosSearch(input)

      # Armazena os links dos vídeos encontrados

      resultado = pesquisa.result()

      # Obter o primeiro link

      url = resultado['result'][0]['link']
      print(url)

      
      # Faz o download do vídeo em forma mp4

      yt = YouTube(url)
      for char in string.punctuation:
         yt.title = yt.title.replace(char, ' ').lower()
      stream = yt.streams.filter(only_audio=True).first().download("C:/SoundWave/videos")

      # Converte o vídeo em mp3

      clip = AudioFileClip(f"C:/SoundWave/videos/{yt.title}.mp4")
      clip.write_audiofile(f"C:/SoundWave/musics/{yt.title}.mp3")
      os.remove(f'C:/SoundWave/videos/{yt.title}.mp4')
      music_isdownloading.config(text = "Finished! Playing ;)")
      janela1.update_idletasks()

      # Toca a música
      pygame.init()
      musica = pygame.mixer.music.load(f'C:/SoundWave/musics/{yt.title}.mp3')
      pygame.mixer.music.set_volume(1.0)
      pygame.mixer.music.play(-1)
      os.system('cls')


def download_status():
    music_isdownloading.place(x=880, y=165)

startSoundWave()
janela1 = tk.Tk()
janela1.resizable(False, False)
janela1.title("SoundWave")
header = tk.Frame(janela1, width=1500, height=101, bg="#000000")
header.pack()
soundwave_header = Label(master=header, text="SoundWave", background="#000000", foreground="white", font=('Roboto',64, 'bold'))
soundwave_header.place(x=530, y=2)
background = tk.Frame(janela1, width=1500, height=528, bg="#1D75DE")
background.pack()
music_orientation = Label(master=background, text="Enter the name of the music", background="#1D75DE", foreground="white", font=('Roboto',15,'bold'))
music_orientation.place(x=480, y=160)
music_isdownloading = Label(master=background, text=" ", background="#1D75DE", foreground="white", font=('Roboto',12))
music_isdownloading.pack_forget()
txtbox_placeholder = Label(master=background, text="User choosen music")
txtbox_placeholder.place(x=484,y=200)
txtBox = tk.Entry(txtbox_placeholder, width=100, borderwidth=0)
txtBox.grid(row=1, column=0)
download = tk.Button(master=background, text="DOWNLOAD", background="#1D75DE", borderwidth=0, command=baixar)
imgButton = PhotoImage(file="button.png")
download.config(image=imgButton)
download.place(x=710, y=240)
janela1.iconbitmap("soundwave.ico")
janela1.mainloop()