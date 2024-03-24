import datetime
import speak
import webbrowser
import weather
import os

def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("My name is Rith, your Virtual Assistant.")  
      return "My name is Rith, your Virtual Assistant."
    
    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hello, how can I help you?")  
        return "Hello, how can I help you?" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great, thank you for asking!") 
            return "I am doing great, thank you for asking!"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("It is my pleasure.")
           return "It is my pleasure."      

    elif "good morning" in data_btn:
           speak.speak("Good morning, how would you like to start your day?")
           return "Good morning, how would you like to start your day?"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour) + " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("Quitting now..")
            return "Quitting now.."  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")   
        speak.speak("Spotify is now ready for you, enjoy your music.")                   
        return "Spotify is now ready for you, enjoy your music."


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("Opening Google..")  
        return "Opening Google.."

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("Opening Youtube..") 
        return "Opening Youtube.."    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("Playing your music..")
        return "Playing your music.." 

    else :
        speak.speak( "I couldn't quite get that.")
        return "I couldn't quite get that."       

