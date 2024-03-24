import pyttsx3

# Function to convert text to speech using pyttsx3 library
def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get the current speech rate
    rate = engine.getProperty('rate')

    # Decrease the speech rate by 70 units (adjust this value as needed)
    engine.setProperty('rate', rate - 70)

    # Convert the text to speech
    engine.say(text)

    # Run the speech engine to output the speech
    engine.runAndWait()