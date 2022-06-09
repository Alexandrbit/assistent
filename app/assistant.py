import speech_recognition as sr
import pyaudio
import os
import random
import playsound
from gtts import gTTS


def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as sourse:
        print('Скажите что-то>>>')
        audio = voice_recognizer.listen(sourse)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: ... {voice_text}")
        return  voice_text
    except sr.UnknownValueError:
        return "ошибка распознания"
    except sr.RequestError:
        return "Ошибка запроса"


def say(text):
    voice = gTTS(text, lang="ru")
    unique_file = "audio_" + str(random.randint(0, 10000)) + ".mp3" # audio_10.mp3
    voice.save(unique_file)

    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f"Ассистент: ")


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say("Привет-привет")
    elif command == "пока":
        stop()
    else:
        say("Не понятно, повторите")


def stop():
    say("До скорого")
    exit()


def start():
    print("Запуск ассистента...")

    while True:
        command = listen()
        handle_command(command)


try:
    start()
except KeyboardInterrupt:
    stop()

