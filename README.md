# 🗣️ Voice Assistant Project

This is an offline voice assistant built with Python that can understand spoken commands, respond with speech, and control basic desktop functions. It uses **Vosk** for offline speech recognition and **pyttsx3** for text-to-speech.

---

## 🔧 Features

- 🎤 Offline voice recognition with Vosk
- 🗣️ Text-to-speech using pyttsx3
- 🧠 Understands and processes voice commands
- 🖥️ Controls desktop applications like:
  - Opening Notepad or Calculator
  - Typing text
  - Minimizing/maximizing/switching windows
  - Taking screenshots
  - Copying/pasting text
  - Opening a web browser and searching Google
  - Displaying an image
- 📋 Reads clipboard content
- ❌ Graceful exit with “exit assistant” voice command

---

## 📁 Project Structure

voice_assistant.py # Main script
.gitignore # Files/folders to exclude from Git tracking
README.md # You're reading it now!

yaml
Copy
Edit

---

## 🚀 How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/fatmamohamed1476/voice-assistant.git
cd voice-assistant
Install dependencies:

bash
Copy
Edit
pip install vosk pyttsx3 sounddevice pyautogui pyperclip opencv-python
Download the Vosk model:

Download a small English model from here (e.g., vosk-model-small-en-us-0.15), extract it, and place the folder in your project directory.

Run the assistant:

bash
Copy
Edit
python voice_assistant.py
Make sure your microphone works and you speak clearly!

🎯 Example Commands
hi

open notepad

open calculator

type I am Fatma

search Python voice assistant

take a screenshot

exit assistant

