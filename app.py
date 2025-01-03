# imports: 
import speech_recognition as sr
import pyttsx3
import datetime
import streamlit as st

# the text-to-speech engine: 
engine = pyttsx3.init()
engine.setProperty('rate', 150)       #speed of the speech
engine.setProperty('volume', 1.0)     #volume of the speech

