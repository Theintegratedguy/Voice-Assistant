# imports: 
import speech_recognition as sr
import pyttsx3
import datetime
import streamlit as st

# the text-to-speech engine: 
engine = pyttsx3.init()
engine.setProperty('rate', 150)       #speed of the speech
engine.setProperty('volume', 1.0)     #volume of the speech

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait() 
    
def listen(): 
    """Listen to user's voice and return the text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            st.success(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            st.error("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            st.error("Sorry, I'm having trouble connecting. Please try again later.")
            return ""
        except sr.WaitTimeoutError:
            st.warning("You were silent. Try again.")
            return ""
        