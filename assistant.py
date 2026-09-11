import speech_recognition as sr
import ollama
import winsound
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

messages = [
    {
        "role": "system",
        "content": "You are a helpful and accurate voice assistant. Answer the user's question clearly and completely. Give concise answers by default, but include the important facts needed to properly answer the question. For follow-up questions, use the previous conversation to understand what the user means."
    }
]


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
            phrase_time_limit=10
        )

        print("Speech captured")

        try:
            text = recognizer.recognize_google(audio)

            print("you said:", text)

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

        messages.append({
            "role": "user",
            "content": text
        })

        response = ollama.chat(
            model="llama3.2:3b",
            messages=messages
        )

        print("Ollama finished")

        messages.append({
            "role": "assistant",
            "content": response["message"]["content"]
        })

        print("AI response received")

        print(response["message"]["content"])

        ai_text = response["message"]["content"]

        speak(ai_text)