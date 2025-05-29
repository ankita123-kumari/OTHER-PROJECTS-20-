import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand."
        except sr.RequestError:
            return "Speech recognition service unavailable."

def chatbot_response(user_input):
    """Generate chatbot response"""
    responses = {
        "hello": "Hi there! How can I help?",
        "how are you": "I'm just a chatbot, but I'm here to assist you!",
        "bye": "Goodbye! Have a great day!",
    }
    return responses.get(user_input, "I'm not sure how to respond to that.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice chatbot. How can I assist you?")
    while True:
        user_input = listen()
        print(f"You said: {user_input}")
        if user_input == "bye":
            speak("Goodbye!")
            break
        response = chatbot_response(user_input)
        speak(response)