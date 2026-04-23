import tkinter as tk
from assistant import speak, take_command
from commands import execute_command

# Function to handle voice command
def start_listening():
    speak("Listening...")
    command = take_command()
    
    if command:
        running = execute_command(command)
        if not running:
            window.destroy()

# GUI Window
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("400x300")

label = tk.Label(window, text="Arsala Voice Assistant", font=("Arial", 16))
label.pack(pady=20)

listen_btn = tk.Button(window, text="🎤 Speak", command=start_listening)
listen_btn.pack(pady=20)

exit_btn = tk.Button(window, text="Exit", command=window.destroy)
exit_btn.pack(pady=10)

# Greeting when app starts
speak("Hello, I am your voice assistant")

window.mainloop()
status_label = tk.Label(window, text="Status: Idle")
status_label.pack()

def start_listening():
    status_label.config(text="Listening...")
    window.update()
    
    command = take_command()
    
    status_label.config(text="Processing...")
    window.update()
    
    if command:
        execute_command(command)
    
    status_label.config(text="Idle")