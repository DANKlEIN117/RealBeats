import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Music control functions
def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def load_music():
    file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        music_title.set(os.path.basename(file))
        pygame.mixer.music.play()

# Main app window
app = tk.Tk()
app.title("RealBeats")
app.geometry("500x400")
app.configure(bg="#0A0A2A")

# Logo and screen placeholder
logo_frame = tk.Frame(app, bg="#0A0A2A", height=250)
logo_frame.pack(fill="both")

title_label = tk.Label(logo_frame, text="🎵 RealBeats 🎵", font=("Helvetica", 24, "bold"), fg="gold", bg="#0A0A2A")
title_label.pack(pady=60)

music_title = tk.StringVar()
music_label = tk.Label(app, textvariable=music_title, font=("Helvetica", 14), fg="white", bg="#0A0A2A")
music_label.pack(pady=5)

# Control buttons frame
controls_frame = tk.Frame(app, bg="#0A0A2A")
controls_frame.pack(pady=20)

btn_style = {"font": ("Arial", 18), "bg": "#0A0A2A", "fg": "white", "bd": 0, "activebackground": "#0A0A2A", "activeforeground": "gold"}

load_btn = tk.Button(controls_frame, text="📂", command=load_music, **btn_style)
play_btn = tk.Button(controls_frame, text="▶", command=play_music, **btn_style)
pause_btn = tk.Button(controls_frame, text="⏸", command=pause_music, **btn_style)
resume_btn = tk.Button(controls_frame, text="🔁", command=resume_music, **btn_style)
stop_btn = tk.Button(controls_frame, text="⏹", command=stop_music, **btn_style)

# Pack the controls inline
load_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
resume_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Start app loop
app.mainloop()
