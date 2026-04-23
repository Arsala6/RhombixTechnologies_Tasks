from assistant import speak, take_command
from commands import execute_command
import config

def start_assistant():
    speak(f"Hello {config.USER_NAME}, I am {config.ASSISTANT_NAME}")
    
    running = True
    while running:
        command = take_command()
        if command:
            running = execute_command(command)

if __name__ == "__main__":
    start_assistant()