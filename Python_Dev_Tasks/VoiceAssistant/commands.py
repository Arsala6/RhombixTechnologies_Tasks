import datetime
import webbrowser
import wikipedia
import pywhatkit
import requests
from assistant import speak, take_command

# ================== WEATHER FUNCTION ==================
def get_weather(city):
    api_key = "2fd0de3671522bf3b32f81a295941a09"   # <-- put your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url).json()
        if response["cod"] != "404":
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            return f"Temperature is {temp} degree Celsius with {desc}"
        else:
            return "City not found"
    except:
        return "Weather service not working"

# ================== SIMPLE AI CHAT ==================
def chatbot_reply(command):
    # Simple logic-based chatbot (no API needed)
    if "hello" in command:
        return "Hello, how can I help you?"
    elif "your name" in command:
        return "I am your personal voice assistant"
    elif "what is ai" in command:
        return "Artificial Intelligence is the simulation of human intelligence in machines"
    else:
        return "That is interesting, tell me more"

# ================== MAIN FUNCTION ==================
def execute_command(command):

    try:
        # TIME
        if "time" in command:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f"Current time is {time}")

        # DATE
        elif "date" in command:
            date = datetime.datetime.now().strftime('%d %B %Y')
            speak(f"Today is {date}")

        # WIKIPEDIA
        elif "who is" in command:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, 1)
            speak(info)

        # PLAY YOUTUBE
        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        # OPEN WEBSITES
        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        # WEATHER
        elif "weather" in command:
            speak("Tell me the city name")
            city = take_command()
            weather = get_weather(city)
            speak(weather)

        # WHATSAPP MESSAGE
        elif "send message" in command:
            speak("What is the message?")
            message = take_command()

            number = input("Enter number with country code: ")
            speak("Sending message")

            # time must be ahead
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 2

            pywhatkit.sendwhatmsg(number, message, hour, minute)
            speak("Message scheduled")

        # JOKE
        elif "joke" in command:
            speak("Why do programmers hate nature? Because it has too many bugs.")

        # CHATBOT
        elif "ask" in command:
            reply = chatbot_reply(command)
            speak(reply)

        # GREETING
        elif "how are you" in command:
            speak("I am fine and ready to help you")

        # CUSTOM MODE
        elif "study mode" in command:
            speak("Study mode activated. Stay focused!")

        # EXIT
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            return False

        # DEFAULT
        else:
            speak("Sorry, I did not understand")

    except Exception as e:
        speak("There was an error processing your request")
        print("Error:", e)

    return True