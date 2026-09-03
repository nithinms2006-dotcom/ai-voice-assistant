import speech_recognition as sr
import ollama
import winsound
import pyttsx3
import threading

recognizer = sr.Recognizer()
engine = pyttsx3.init()
stop_speaking = threading.Event()

def speak(text):
    engine.say(text)
    engine.runAndWait() 

with sr.Microphone() as source:
    print("Calibrating microphone")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Ready!")

    while True:
        winsound.Beep(1000, 300)

        print("Listening...")

        audio = recognizer.listen(
            source,
            timeout=None,
            phrase_time_limit=5
        )

        print("Speech captured")

        try:
            text = recognizer.recognize_google(audio)
            print("Speech recognized successfully")
            if text.lower() in ["exit", "quit", "stop"]:
                print("goodbye!")
                engine.say("Goodbye!")
                engine.runAndWait()
                print("Exiting...")
                break

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            continue

        except sr.RequestError as e:
            print("Speech recognition service error:", e)
            continue

        print("Sending to AI...")

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content":"you are a fast voice assistant.give concise answers in 2 to 4 sentence unless the user asks for more detailed explanation."
                },
                { "role": "user", "content": text }
            ]
        )

        print("AI response received")
        print(response["message"]["content"])
        ai_text = response["message"]["content"]

        speech_thread = threading.Thread(target=speak, args=(ai_text,))
        speech_thread.start()
        