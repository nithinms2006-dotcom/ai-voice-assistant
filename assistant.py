import speech_recognition as sr
import ollama
import winsound
import pyttsx3
import time


def speak(text):
    voice_engine = pyttsx3.init()
    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()


recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0
recognizer.non_speaking_duration = 0.5
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


messages = [
    {
        "role": "system",
        "content": "You are a helpful voice assistant. Give clear and concise answers."
    }
]


while True:
    try:
        winsound.Beep(1000, 200)

        with sr.Microphone() as source:
            print("\nListening...")
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        print("Recognizing...")
        user_text = recognizer.recognize_google(audio)
        print("You:", user_text)

        if user_text.lower() in ["exit", "quit", "stop", "goodbye"]:
            speak("Goodbye!")
            break

        messages.append({
            "role": "user",
            "content": user_text
        })

        print("Thinking...")

        response = ollama.chat(
            model="llama3.2:3b",
            messages=messages
        )

        ai_text = response["message"]["content"]
        print("Assistant:", ai_text)

        messages.append({
            "role": "assistant",
            "content": ai_text
        })

        speak(ai_text)
        print("Finished speaking.")

    except sr.WaitTimeoutError:
        print("No speech detected. Please try again.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")

    except sr.RequestError as error:
        print("Speech recognition service error:", error)

    except Exception as error:
        print("An error occurred:", error)

    time.sleep(0.5)