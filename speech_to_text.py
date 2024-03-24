import speech_recognition as sr
import speak

# Function to convert speech to text using the microphone input.
def speech_to_text():
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak.speak("Sorry, I didn't catch that.")  # Changed the text for unknown value error
        except sr.RequestError:
            speak.speak('No internet connection. Please check your internet.')  # Changed the text for request error

    return voice_data