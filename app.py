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

# Streamlit App
st.title("Voice Assistant with Streamlit")
st.text("Click the buttons below to interact with the assistant.")

if 'response' not in st.session_state:
    st.session_state['response'] = ""

if st.button("Start Listening"):
    command = listen()
    if "hello" in command:
        response = "Hi there! How can I assist you?"
    elif "your name" in command:
        response = "I am your voice assistant. What can I do for you?"
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {now}"
    elif "exit" in command or "quit" in command:
        response = "Goodbye! Have a great day!"
    elif command:
        response = "Sorry, I didn't understand that. Can you try again?"
    else:
        response = "You didn't say anything."

    # Display and speak the response
    st.session_state['response'] = response
    st.success(response)
    speak(response)

# Display previous response
if st.session_state['response']:
    st.text_area("Assistant Response", st.session_state['response'], height=150)
        