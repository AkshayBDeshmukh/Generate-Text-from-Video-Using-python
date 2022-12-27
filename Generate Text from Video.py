import speech_recognition as sr 
r = sr.Recognizer() 
def Convert_to_text(): 
    with sr.Microphone() as source: 
        print("Speak Now...")
        audio = r.listen(source) 
    try: 
        generated_text = r.recognize_google(audio) 
        print("You said: \n" + generated_text) 
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    return generated_text 

if __name__ == '__main__': 
    Convert_to_text() 
