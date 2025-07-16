import sounddevice as sd
import json
import os
import pyperclip
import queue
import pyautogui
import pyttsx3
import webbrowser
import cv2
from vosk import Model, KaldiRecognizer

# setup TTS

engine = pyttsx3.init()
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# commands


def greet():
    speak("Hi! I am your assistant nice to meet you.")

def open_notepad():
    os.startfile("notepad.exe")
    speak("Notepad opened.")

def open_calculator():
    os.startfile("calc.exe")
    speak("Calculator opened.")

def show_image():
    img_path = "C:\\Users\\BS\\Pictures\\a9a09c55-65b6-41b7-b369-3bcf74834ee4.png"
    if os.path.exists(img_path):
        img= cv2.imread(img_path)
        cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        speak("Here is your image.")
    else:
        speak("Image not found.")

def copy_text():
    pyperclip.copy("This is a predefined text to copy.")
    speak("Text copied to clipboard.")

def paste_text():
    pyautogui.hotkey("ctrl","v")
    speak("Text pasted.")

def close_window():
    speak("The current window is closing.")
    pyautogui.hotkey("alt","f4")

def type_text(user_text):
    pyautogui.write(user_text)
    speak("Your text was typed successfully.")

def min_all_win():
    speak("Minimizing all windows.")
    pyautogui.hotkey("win","d")

def max_win():
    pyautogui.hotkey("win","up")
    speak("Window maximized")

def switch_win():
    pyautogui.hotkey("alt","tab")
    speak("window switched.")

def open_webbroswer():
    webbrowser.open("https://www.google.com")
    speak("Web browser opened.")

def search_query(query):
    url= f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query}")

def take_screenshot():
    screenshot_path= "screenshot.png"
    speak("screenshot will be taken")
    screenshot=pyautogui.screenshot()
    screenshot.save(screenshot_path)
    speak("Screenshot taken and saved")

def read_clipboard():
    text= pyperclip.paste()
    if text:
        speak(f"The clipboard contains {text}")
    else:
        speak("Clipboard is empty.")

running=True
def exit_assistant():
    global running
    speak("Bye see you soon.")
    running=False


# commands processing


def process_commands(text):
    text=text.lower()

    if text == "hi":
        greet()
    elif text == "open notepad":
        open_notepad()
    elif text == "open calculator":
        open_calculator()
    elif text == "show image":
        show_image()
    elif text == "copy this text":
        copy_text()
    elif text == "paste clipboard":
        paste_text()
    elif text == "close window":
        close_window()
    elif text.startswith("type "):
        user_text= text.replace("type ","",1)
        type_text(user_text)
    elif text == "minimize all windows":
        min_all_win()
    elif text == "maximize window":
        max_win()
    elif text == "switch window":
        switch_win()
    elif text == "open web browser":
        open_webbroswer()
    elif text.startswith("search "):
        query=text.replace("search ","",1)
        search_query(query)
    elif text == "take a screenshot":
        take_screenshot()
    elif text == "read clipboard":
        read_clipboard()
    elif text == "exit assistant":
        exit_assistant()
    else:
        speak("Sorry I did not get that command.")


# speech recognition

model_path = "vosk-model-small-en-us-0.15"
model=Model(model_path)
sample_rate=16000
buff = queue.Queue()

def callback(indata, frames, time, status):
    buff.put(bytes(indata))

# start listening

with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype='int16', device=None, channels=1, callback=callback):
    print("Listening.. Speak your command.")
    rec=KaldiRecognizer(model,sample_rate)

    while running:
        data=buff.get()
        if rec.AcceptWaveform(data):
            result=json.loads(rec.Result())
            text=result.get("text","")
            if text:
                print("You said:",text)
                process_commands(text)