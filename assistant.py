import speech_recognition as sr
import ollama
import winsound
import pyttsx3
import threading

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text, stop_event):
    engine.say(text)
    engine.runAndWait()
    stop_event.set()


def listen_for_stop(stop_event):
    stop_recognizer = sr.Recognizer()

    with sr.Microphone() as stop_source:
        while not stop_event.is_set():
            try:
                audio = stop_recognizer.listen(
                    stop_source,
                    timeout=0.5,
                    phrase_time_limit=2
                )

                text = stop_recognizer.recognize_google(audio)

                if text.lower().strip() in ["stop", "cancel"]:
                    print("Stop command detected.")
                    engine.stop()
                    stop_event.set()
                    break

            except (sr.WaitTimeoutError, sr.UnknownValueError):
                continue

            except sr.RequestError:
                continue


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
                print("Goodbye!")
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
                    "content": "You are a fast voice assistant. Give concise answers in 2 to 4 sentences unless the user asks for a more detailed explanation."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        print("AI response received")

        ai_text = response["message"]["content"]

        print(ai_text)

        stop_event = threading.Event()

        speech_thread = threading.Thread(
            target=speak,
            args=(ai_text, stop_event)
        )

        stop_thread = threading.Thread(
            target=listen_for_stop,
            args=(stop_event,)
        )

        speech_thread.start()
        stop_thread.start()

        speech_thread.join()

        stop_event.set()
        stop_thread.join()