# 💬 Abii's Voice Assistant with Text Input and gTTS Speech Output 🎤

import tkinter as tk            # GUI library
from gtts import gTTS           # Google Text-to-Speech
import pygame                   # For playing sound
import os
import time

# 🎵 Initialize the pygame mixer for audio playback
pygame.mixer.init()

# 🗣️ Function to speak the given text using gTTS + pygame
def speak(text):
    tts = gTTS(text=text, lang='en')         # Convert text to speech
    tts.save("voice.mp3")                    # Save it as an mp3
    pygame.mixer.music.load("voice.mp3")     # Load the mp3
    pygame.mixer.music.play()                # Play it
    while pygame.mixer.music.get_busy():     # Wait till it's done
        time.sleep(0.5)
    os.remove("voice.mp3")                   # Delete file after speaking

# 🔄 Function to handle user command from text box
def handle_command():
    command = entry.get()
    label.config(text=f"You said: {command}")
    speak(f"You said {command}")

# 🖼️ GUI Window Setup
app = tk.Tk()
app.title("Abii's Assistant 💬")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

# 🔤 Label at the top
label = tk.Label(app, text="💬 Type something and click 'Speak'", 
                 font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=20)

# ✍️ Text input field
entry = tk.Entry(app, font=("Arial", 14), width=30)
entry.pack(pady=10)

# 🔘 Speak button
btn = tk.Button(app, text="Speak", font=("Arial", 16), 
                command=handle_command, bg="#28a745", fg="white")
btn.pack(pady=10)

# 🚀 Launch the assistant app
app.mainloop()