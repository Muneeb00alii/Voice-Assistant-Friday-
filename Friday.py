# import os
# import pyttsx3
# import smtplib
# import datetime
# import wikipedia
# import webbrowser
# import speech_recognition as sr
# import random
# import requests
# import json
# import pyjokes
# import pyautogui
# import psutil
# import pywhatkit
# from bs4 import BeautifulSoup
# import urllib.request
# from urllib.request import urlopen
# from urllib.parse import quote
# from time import sleep
# from datetime import datetime
# from googlesearch import search
# from googletrans import Translator
# from googletrans import LANGUAGES
# from googletrans import Translator
# from googletrans import LANGUAGES
# from pytube import YouTube
# from pytube import Playlist
# from pytube import exceptions


# # This a Female voice assistant of Muneeb named friday

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# recognizer = sr.Recognizer()

# # Function to convert text to speech
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # Function to greet the user
# def greet():
#     hour = int(datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")
#     speak("I am friday Muneeb's Personal Assistant. How may I help you?")

# # Function to take command from the user
# def takeCommand():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 1
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         command = recognizer.recognize_google(audio, language='en-in')
#         print(f"User said: {command}\n")

#     except Exception as e:
#         print("Say that again please...")
#         return "None"
#     return command

# # Function to send email
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('friday.wang.mq@outlook.com', 'Ma#78600') # Enter your email and password
#     server.sendmail('   ', to, content) # Enter your email  and password
#     server.close()

# # Function to get the news
# def getNews():
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3d4c7a3b7b4f4d8b9d9c0c6b3b4d8b9c"
#     news = requests.get(url).text
#     news_dict = json.loads(news)
#     articles = news_dict['articles']
#     speak("Here are some top news for you.")
#     for article in articles:
#         speak(article['title'])
#         speak("Moving on to the next news...")
#     speak("That's all for now.")

# # Function to get the weather
# def getWeather(city):
#     api_key = "3d4c7a3b7b4f4d8b9d9c0c6b3b4d8b9c"
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     weather_data = requests.get(base_url).json()
#     if weather_data['cod'] == '404':
#         speak("City not found.")
#     else:
#         main = weather_data['main']
#         temperature = main['temp']
#         humidity = main['humidity']
#         pressure = main['pressure']
#         weather_description = weather_data['weather'][0]['description']
#         speak(f"Temperature is {temperature} Kelvin, humidity is {humidity} percent, pressure is {pressure} hPa and weather description is {weather_description}.")

# # Function to get the stock price
# def getStockPrice(company):
#     url = f"https://www.google.com/search?q={company}+stock+price"
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     try:
#         stock_price = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
#         speak(f"The current stock price of {company} is {stock_price}.")
#     except:
#         speak("Stock price not found.")

# # Function to get the lyrics of a song
# def getLyrics(song):
#     song = song.replace(" ", "+")
#     url = f"https://www.google.com/search?q={song}+lyrics"
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     try:
#         lyrics = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text
#         speak(f"The lyrics of the song {song.replace('+', ' ')} are as follows.")
#         speak(lyrics)
#     except:
#         speak("Lyrics not found.")

# # Function to get the meaning of a word
# def getMeaning(word):
#     translator = Translator()
#     result = translator.translate(word, dest='en')
#     speak(f"The meaning of the word {word} is {result.text}.")

# # Function to get the translation of a word
# def getTranslation(text, dest):
#     translator = Translator()
#     result = translator.translate(text, dest=dest)
#     speak(f"The translation of the text is {result.text}.")

# # Function to get the jokes
# def getJoke():
#     joke = pyjokes.get_joke()
#     speak(joke)

# # Function to get the battery percentage
# def getBattery():
#     battery = psutil.sensors_battery()
#     speak(f"The battery percentage is {battery.percent} percent.")

# # Function to get the time
# def getTime():
#     time = datetime.now().strftime("%H:%M:%S")
#     speak(f"The current time is {time}.")

# # Function to get the date
# def getDate():
#     date = datetime.now().strftime("%d-%m-%Y")
#     speak(f"The current date is {date}.")

# # Function to open a website
# def openWebsite(website):
#     speak(f"Opening {website}.")
#     webbrowser.open(f"https://www.{website}.com")

# # Function to open YouTube
# def openYouTube():
#     speak("Opening YouTube.")
#     webbrowser.open("https://www.youtube.com")

# # Function to open Google
# def openGoogle():
#     speak("Opening Google.")
#     webbrowser.open("https://www.google.com")

# # Function to open WhatsApp Web
# def openWhatsApp():
#     speak("Opening WhatsApp Web.")
#     webbrowser.open("https://web.whatsapp.com")

# # Function to open Facebook
# def openFacebook():
#     speak("Opening Facebook.")
#     webbrowser.open("https://www.facebook.com")

# # Function to open Instagram
# def openInstagram():
#     speak("Opening Instagram.")
#     webbrowser.open("https://www.instagram.com")

# # Function to open Twitter
# def openTwitter():
#     speak("Opening Twitter.")
#     webbrowser.open("https://www.twitter.com")

# # Function to open LinkedIn
# def openLinkedIn():
#     speak("Opening LinkedIn.")
#     webbrowser.open("https://www.linkedin.com")

# # Function to open GitHub
# def openGitHub():
#     speak("Opening GitHub.")
#     webbrowser.open("https://www.github.com")

# # Function to open Stack Overflow
# def openStackOverflow():
#     speak("Opening Stack Overflow.")
#     webbrowser.open("https://www.stackoverflow.com")

# # Function of introduction
# def introduction():
#     speak("I am friday, a virtual assistant created by Muneeb. I can help you with a variety of tasks like sending emails, searching the web, getting the news, getting the weather, getting the stock price, getting the lyrics of a song, getting the meaning of a word, getting the translation of a text, getting jokes, getting the battery percentage, getting the time, getting the date, opening YouTube, opening Google, opening WhatsApp Web, opening Facebook, opening Instagram, opening Twitter, opening LinkedIn, opening GitHub, opening Stack Overflow and much more.")

# # Function to search the anything on wikipedia
# def searchWikipedia(command):
#     speak(f"Searching {command} on Wikipedia.")
#     results = wikipedia.summary(command, sentences=2)
#     speak("According to Wikipedia")
#     speak(results)

# # Function to search the anything on google
# def searchGoogle(command):
#     speak(f"Searching {command} on Google.")
#     for j in search(command, num=1, stop=1, pause=2):
#         webbrowser.open(j)


# # Function to to speak urdu
# def speakUrdu():
#     speak("میں چلو، منیب کی آپ کی معاون ہوں۔ میں آپ کی کس طرح مدد کر سکتی ہوں؟")

# # Function to exit
# def exit():
#     speak("Goodbye!")
#     exit()

# # Main function
# if __name__ == "__main__":
#     greet()
#     while True:
#         command = takeCommand().lower()

#         if 'wikipedia' in command:
#             speak("Searching Wikipedia...")
#             command = command.replace("wikipedia", "")
#             results = wikipedia.summary(command, sentences=2)
#             speak("According to Wikipedia")
#             speak(results)

#         elif 'open youtube' in command:
#             openYouTube()

#         elif 'open google' in command:
#             openGoogle()

#         elif 'open whatsapp' in command:
#             openWhatsApp()

#         elif 'open facebook' in command:
#             openFacebook()

#         elif 'open instagram' in command:
#             openInstagram()

#         elif 'open twitter' in command:
#             openTwitter()

#         elif 'open linkedin' in command:
#             openLinkedIn()

#         elif 'open github' in command:
#             openGitHub()

#         elif 'open stack overflow' in command:
#             openStackOverflow()

#         elif 'send email' in command:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 speak("Who should I send the email to?")
#                 to = takeCommand()
#                 sendEmail(to, content)
#                 speak("Email has been sent.")
#             except Exception as e:
#                 speak("Sorry, I am not able to send this email.")
#         elif 'Urdu' in command:
#             speakUrdu()





#! Importing Libraries
import os
import random
import smtplib
import pyttsx3
import warnings
import requests
import wikipedia
import webbrowser
import sympy as sp
from datetime import datetime
from bs4 import BeautifulSoup
import speech_recognition as sr
from googletrans import Translator
from packages import music_dict, jokes_list


#! Function to initialize the speech engine
def initialize_speech_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 249)
    engine.setProperty('volume', 1)
    engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Default to female English voice
    return engine


#! Function to convert text to speech as female
def speak(engine, text):
    engine.say(text)
    print(text)
    # print()
    engine.runAndWait()


#! Function to listen for command
def listen_for_command(recognizer, initial_timeout = 5, phrase_time_limit=None):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...\n")
        audio = recognizer.listen(source, initial_timeout = initial_timeout, phrase_time_limit=phrase_time_limit)
    return recognizer.recognize_google(audio)



def translate_phrase(engine):
    speak(engine, "What phrase would you like to translate?")
    phrase = listen_for_command(recognizer)
    print(phrase)
    print()

    speak(engine, "Which language do you want to translate it to?")
    language = listen_for_command(recognizer)
    print(language)
    print()

    translator = Translator()
    translation = translator.translate(phrase, dest=language)
    speak(engine, f"The translation is: {translation.text}")


#! Function to open a website
def open_website(command, engine):
    try:
        website = command.lower().split("open", 1)[1].strip()
        if website:
            webbrowser.open(f"https://www.{website}.com")
        else:
            raise ValueError("No website name provided")
    except Exception as e:
        speak(engine, "Sorry, I couldn't understand that.")
        print(f"Error: {str(e)}")


#! Function to search on YouTube
def search_on_youtube(query, engine):
    try:
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query}")
    except Exception as e:
        speak(engine, f"Sorry. I couldn't find this {query}.")

#! Function to search on Google
def google_search(query, engine):
    try:
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    except Exception as e:
        speak(engine, f"Sorry. I couldn't find this {query}.")


#! Function to play a song on YouTube
def play_song(song, engine):
    try:
        if song.lower() in music_dict:
            link = music_dict[song.lower()]
            webbrowser.open(link, new=2)
        else:
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={song.lower()}")

    except Exception as e:
        speak(engine, "Sorry. I couldn't find the song.")


#! Function to search on Wikipedia
def search_wikipedia(command, engine):
    try:
        print(command)
        summary = wikipedia.summary(command, sentences=2)
        speak(engine, f"According to Wikipedia, {summary}")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on that.")


#! Function to perform a calculations
def perform_calculation(engine):
    speak(engine, "What calculation would you like to perform?")
    expression = input("Enter the expression: ")
    try:
        result = sp.sympify(expression).evalf()
        result = round(result, 2) if isinstance(result, float) else result
        speak(engine, f"The result is {result}")
    except Exception as e:
        speak(engine, "Sorry, I couldn't perform the calculation.")


#! Function to get the weather of Lahore Pakistan. It is done using Google.
def get_weather(engine, city):
    url = f"https://www.google.com/search?q=weather+in+{city}+Pakistan"
    response = requests.get(url)

    if response.status_code == 200:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignore the warning
            soup = BeautifulSoup(response.text, "html.parser")
        weather = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        speak(engine, f"The current temperature in {city} is {weather}.")
    else:
        speak(engine, "Sorry, I couldn't fetch the weather at the moment.")


#! Function to get the current date and time in 12-hour format
def date_time(engine):
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A,%d %B, %Y")
    speak(engine, f"The current time is {current_time} and today is {current_date}.")


#! Function to process random commands like opening websites, playing songs, etc.
def process_commands(command, engine):

    # Open a website
    if "open" in command.lower():
        speak(engine, "Which website would you like to open?")
        website = listen_for_command(recognizer)
        open_website(website, engine)

    # Play a song on YouTube
    elif "play" in command.lower() or "song" in command.lower():
        speak(engine, "Which song would you like to play?")
        song = listen_for_command(recognizer)
        play_song(song, engine)

    # Search on YouTube
    elif "youtube" in command.lower():
        speak(engine, "What would you like to search on YouTube?")
        query = listen_for_command(recognizer)
        search_on_youtube(query, engine)

    # Search on Google
    elif "google" in command.lower():
        speak(engine, "What would you like to search on Google?")
        query = listen_for_command(recognizer)
        google_search(query, engine)

    else:
        speak(engine, "Sorry, I couldn't understand that.")



#! Funtion to tell jokes
def tell_joke(engine):
    joke = random.choice(jokes_list)
    speak(engine, joke)


#! Function to get the News using Goolge
def read_news(engine, recognizer):
    url = "https://news.google.com/rss"
    response = requests.get(url)

    if response.status_code == 200:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignore the warning
            soup = BeautifulSoup(response.text, "html.parser")
        news_list = soup.find_all("item")
        batch_size = 5
        index = 0

        # Here we are reading the news in batches of 5
        while index < len(news_list):
            speak(engine, f"Here are {batch_size} news headlines:\n")
            for news in news_list[index:index+batch_size]:
                speak(engine, news.title.text)
                print()
            index += batch_size

            # Here we are asking the user if they want to hear more news
            if index < len(news_list):
                speak(engine, "Would you like to hear more news headlines?")
                response = listen_for_command(recognizer)

                if "yes" in response.lower():
                    print(response)
                    continue
            else:
                speak(engine, "That's all for now. Exiting news headlines.")
    else:
        speak(engine, "Sorry, I couldn't fetch the news at the moment.")


#! Function to send an email
def send_email(engine):
    try:
        speak(engine, "Please enter the recipient's email address.")
        recipient_email = input("Recipient's Email: ")

        speak(engine, "What should I say?")
        message = input("Message: ")
        print()

        sender_email = "chloe.wang.mq@outlook.com"
        sender_password = "Ma#78600"

        # Compose the email
        subject = input("Subject: ")
        print()
        body = message
        mail = f"Subject: {subject}\n\n{body}"
        print(mail)

        print("Sending email please wait...\n")

        # Log in to the email server (Outlook.com)
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, mail)
        speak(engine, "Email sent successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")
        speak(engine, "Sorry, I couldn't send the email.")

    server.quit()


#! Function to leave a message for Muneeb
def leave_message_for_muneeb(engine):

    speak(engine, "What is your name?") # Asking for the user's name 
    user_name = listen_for_command(recognizer).capitalize()
    print("Name: ",user_name)
    print()

    speak(engine, f"Okay, {user_name} Please leave your message.") # Asking for the user's message
    user_message = listen_for_command(recognizer).capitalize()
    print("Message: ",user_message)
    print()

    with open("Muneeb_messages.txt", "a") as file: # Saving the message in a file (Muneeb_messages.txt)
        print(f"\nFrom: {user_name}\nMessage: {user_message}\n\n")
        speak(engine, f"{user_name}, Please Confirm the message. Do you want me to save it for Muneeb")

        response = listen_for_command(recognizer)
        print(response)
        print()

        if "yes" in response.lower() or "save" in response.lower() or "confirm" in response.lower() or "okay" in response.lower() or "sure" in response.lower():
            speak(engine, "Do you want to add any contact information?")
            contact_info_confirmation = listen_for_command(recognizer)
            print(contact_info_confirmation)
            print()
            
            if contact_info_confirmation:
                speak(engine,"Please write your contact information here")
                contact_info =  input("Contact Information: ")
                print(contact_info)

                file.write(f"\nFrom: {user_name}\nMessage: {user_message}\nContant Information: {contact_info}\n")
                speak(engine, f"{user_name}, Your message has been saved successfully.")
            else:
                file.write(f"\nFrom: {user_name}\nMessage: {user_message}\n")
                speak(engine, f"{user_name}, Your message has been saved successfully.")
        else:
            speak(engine, f"{user_name}, Your message has not been saved.")

    speak(engine, "Here is a Message from Muneeb. Hi it's Muneeb. I'm currently busy. I'll get back to you as soon as possible. Thank you for your message.")


#! Function to take a note
def Note(engine):
    speak(engine, "What should I write down?")
    note = listen_for_command(recognizer)

    with open("notes.txt", "a") as file:
        file.write(f"{note}\n")
        speak(engine, "Note saved successfully.")


#! Funcrtion to process random questions (Yet to be added in Main function)
def random_questions(engine, question):
    responses = {
        "how are you": "I'm here and ready to assist you, Boss!",
        "who created you": "I was created by Muneeb Ali, your loyal assistant!",
        "what is your name": "My name is Friday, at your service!",
        "what can you do": "I can open websites, play songs, and more. Just ask boss!",
    }

    question_lower = question.lower()

    if question_lower in responses:
        speak(engine, responses[question_lower])
    else:
        speak(engine, "Sorry, I'm still learning. I may not have an answer for that yet.")



def main():
    global recognizer

    # Initialize the recognizer and speech engine
    recognizer = sr.Recognizer()
    engine = initialize_speech_engine()

    # Clear the terminal
    os.system("cls")

    # Print the terminal title
    print("                                                                             ******************************")
    print("                                                                               Friday Muneeb's Assistant!")
    print("                                                                             ******************************")

    # Greet the user
    speak(engine, "Hey Boss! It's Friday. How can I help you?\n")

    while True:
        print("Recognizing...\n")

        # Try to recognize the user's command
        try:
            word = listen_for_command(recognizer)
            print(f"User said: {word}\n")

            # Listen for the wake word "Friday"
            if "friday" in word.lower():
                speak(engine, "Yes Boss?")
                print("Friday Active...\n")

                # Keep the assistant active until the user says "exit"
                while True:
                    command = listen_for_command(recognizer)
                    print(f"Command: {command}\n")

                    # Process command like opening websites, playing songs, searching on YouTube, searching on Google
                    if "open" in command.lower() or "play" in command.lower() or "song" in command.lower() or "search" in command.lower():
                        process_commands(command, engine)

                    # Get some News
                    elif "news" in command.lower() or "khabren" in command.lower() or "headlines" in command.lower():
                        read_news(engine, recognizer)

                    # Get the current time and date
                    elif "time" in command.lower() or "date" in command.lower():
                        date_time(engine)

                    # Get the weather
                    elif "weather" in command.lower():
                        speak(engine, "Which city do you want to know the weather for?")
                        city = listen_for_command(recognizer)
                        get_weather(engine, city)

                    # Search on Wikipedia
                    elif "wikipedia" in command.lower():
                        speak(engine, "What do you want to search for?")
                        search_query = listen_for_command(recognizer)
                        search_wikipedia(search_query, engine)

                    # Calculate any Math problem
                    elif "calculate" in command.lower() or "solve" in command.lower() or "math" in command.lower() or "calculation" in command.lower():
                        perform_calculation(engine)

                    # Take notes
                    elif "note" in command.lower() or "take a note" in command.lower() or "todo" in command.lower():
                        Note(engine)

                    # Leave a message for Muneeb
                    elif "message" in command.lower() and ("muneeb" in command.lower() or "boss" in command.lower() or "ali" in command.lower() or "owner" in command.lower() or "coder" in command.lower()):
                        leave_message_for_muneeb(engine)

                    # Send an email
                    elif "email" in command.lower() or "mail" in command.lower():
                        send_email(engine)

                    # Translate a phrase
                    elif "translate" in command.lower() or "translate" in command.lower():
                        translate_phrase(engine)

                    # Get contact information of Muneeb
                    elif "contact" in command.lower() or "contact information" in command.lower() or "raabta" in command.lower():
                        speak(engine, "Here is Muneeb's contact information.")
                        print_contact_info()

                    # Tell a joke
                    elif "joke" in command.lower():
                        tell_joke(engine)

                    # Exit the program
                    elif "exit" in command.lower() or "close" in command.lower() or "bye" in command.lower():
                        speak(engine, "Goodbye Boss!")
                        return

                    else:
                        process_commands(command, engine)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {str(e)}")

def print_contact_info():
    print("""
Name: Muneeb Ali
Phone Number: 0321-9697820
Email: muneeb00ali@gmail.com
""")

if __name__ == "__main__":
    main()