
from pytube import YouTube
from pytube import Playlist
from tkinter import *
from tkinter import ttk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tkinter import messagebox as MessageBox
import FormPlaylist
import main
import ttkbootstrap as ttk
import moviepy.editor as mp

def center_window(window):

    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2*frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth()//2 - win_width//2
    y = window.winfo_screenheight()//2 - win_height//2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()


def poup():
    MessageBox.showinfo("Sobre el software","Programa creado para descaragr videos de youtube con el link")



def mp4():
    link = main.video.get()
    direct = main.video_carpeta.get()

    if len(link) == 0:
        MessageBox.showinfo("Campo vacío","Debe ingresar un link")
    else:
        if len(direct) == 0:
             MessageBox.showinfo("Campo vacío","Debe ingresar un nombre para crear una carpeta")
        else:
            Youtubevideo = YouTube(link)
            downloads = Youtubevideo.streams.get_highest_resolution()
            downloads.download(direct)
            MessageBox.showinfo("Estado de descarga","La descarga se realizó con exito")

def mp3():
    print("presiono boton")
