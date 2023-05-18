import tkinter as tk
from tkinter import *
from init import *
from pytube import YouTube
from moviepy.editor import *
from pathlib import Path
from youtubesearchpython import VideosSearch
import string 

def SoundWave():

      input = txtBox.get()
         
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

      # Toca a música

      pygame.init()
      musica = pygame.mixer.Sound(f'C:/SoundWave/musics/{yt.title}.mp3')
      musica.set_volume(1.0)
      musica.play(-1)
      os.system('cls')
      time.sleep(8)
      musica.stop()


init()
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
txtbox_placeholder = Label(master=background, text="User choosen music")
txtbox_placeholder.place(x=484,y=200)
txtBox = tk.Entry(txtbox_placeholder, width=100, borderwidth=0)
txtBox.grid(row=1, column=0)
download = tk.Button(master=background, text="DOWNLOAD", background="#1D75DE", borderwidth=0, command=SoundWave)
imgButton = PhotoImage(file="button.png")
download.config(image=imgButton)
download.place(x=710, y=240)
janela1.resizable = (False, False)
time.sleep(10)
janela1.mainloop()