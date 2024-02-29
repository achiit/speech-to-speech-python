

# import speech_recognition as sr
# import google.generativeai as genai
# from IPython.display import Markdown
# import PIL.Image
# import textwrap
# import pyttsx3



# def select_microphone():
#     recognizer = sr.Recognizer()
#     microphones = sr.Microphone.list_microphone_names()
#     print("Available microphones:")
#     for i, mic in enumerate(microphones):
#         print(f"{i+1}. {mic}")
    
#     while True:
#         try:
#             choice = int(input("Enter the number of the microphone you want to use: "))
#             if choice < 1 or choice > len(microphones):
#                 print("Invalid choice. Please enter a valid number.")
#             else:
#                 return choice - 1
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# # Function to convert speech to text
# def speech_to_text(selected_mic):
#     recognizer = sr.Recognizer()
#     with sr.Microphone(device_index=selected_mic) as source:
#         print("Speak something...")
#         audio = recognizer.listen(source)
    
#     try:
#         text = recognizer.recognize_google(audio)
#         print("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand audio.")
#         return ""
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         return ""

# # Function to convert text to speech
# def text_to_speech(text):
#     engine = pyttsx3.init()
#     # Set the voice to Microsoft Zira Desktop
#     engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
#     engine.say(text)
#     engine.runAndWait()




# # Function to generate content using Generative AI
# # Function to generate content using Generative AI
# def generate_content(input_text):
#     GOOGLE_API_KEY = "AIzaSyAeySqsJ7_cBnHhzeZqRU2HjOWV6QOsgnk"
#     genai.configure(api_key=GOOGLE_API_KEY)
    
#     # Read the content from the text file
#     with open("content.txt", "r") as file:
#         additional_info = file.read()
    
#     # Concatenate the input text with the content from the file
#     prompt = f"{input_text} tell the relevant information strictly from this question from the provided information {additional_info}"
    
#     # Generate content based on the updated prompt
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(prompt)
#     return response.text


# # Main function
# def main():
#     while True:
#         # Select microphone
#         selected_mic_index = select_microphone()
        
#         # Get input from the user via speech
#         user_input = speech_to_text(selected_mic_index)
        
#         # Generate content based on user input
#         if user_input:
#             generated_content = generate_content(user_input)
            
#             # Convert generated content to speech
#             text_to_speech(generated_content)
#             print("Generated Content:", generated_content)

# if __name__ == "__main__":
#     main()


import speech_recognition as sr
import google.generativeai as genai
import pyttsx3

# Function to select microphone (automatically set to number 5)
def select_microphone():
    return 4  # Index 4 corresponds to microphone number 5 (since indexing starts from 0)

# Function to convert speech to text
def speech_to_text(selected_mic):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=selected_mic) as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    # Set the voice to Microsoft Zira Desktop
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    engine.say(text)
    engine.runAndWait()

# Function to generate content using Generative AI
def generate_content(input_text):
    GOOGLE_API_KEY = "AIzaSyAeySqsJ7_cBnHhzeZqRU2HjOWV6QOsgnk"
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Read the content from the text file
    with open("content.txt", "r") as file:
        additional_info = file.read()
    
    # Concatenate the input text with the content from the file
    # prompt = f"{input_text} tell the relevant information strictly like if the name is asked then only name and who made you then tell that like that dont exceed beyond 100words from this question from the provided information {additional_info}"
    prompt = f"{input_text}"
    
    # Generate content based on the updated prompt
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Main function
def main():
    # Select microphone automatically
    
    selected_mic_index = select_microphone()
    microphones = sr.Microphone.list_microphone_names()
    print(microphones[selected_mic_index])
    while True:
        # Get input from the user via speech
        user_input = speech_to_text(selected_mic_index)
        
        # Generate content based on user input
        if user_input:
            generated_content = generate_content(user_input)
            
            # Convert generated content to speech
            text_to_speech(generated_content)
            print("Generated Content:", generated_content)

if __name__ == "__main__":
    main()
