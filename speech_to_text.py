import speech_recognition as sr
import os.path

recognizer = sr.Recognizer()

def listen():
    # obtain audio from the microphone
    with sr.Microphone() as mic:
        print("Say something : ")
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        audio = recognizer.listen(mic)
        return audio
def to_text(audio):
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(recognizer.recognize_google(audio))

        # calls save_txt with the text that was generated
        save_txt(recognizer.recognize_google(audio))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def save_mp3(audio):
    save_into_file = input("Do you want to save your recording into an mp3 file? y/n: ")
    if (save_into_file == "y"):

        # create directory Voice Results
        dirName = "Voice Results"
        if not os.path.isdir(dirName):
            os.mkdir(dirName)

        # write audio to a WAV file, then it is converted to an MP3 file + asks for filename etc...
        check = True
        while check == True:
            filename = input("Save recording as: ")
            if (os.path.exists(filename + ".mp3")):
                overwrite = input("This file already exists, do you want to overwrite it? y/n: ")
                if (overwrite == "y"):
                    check = False
            else:
                check = False

        with open(os.path.join(dirName, filename + ".mp3"), "wb") as f:
            f.write(audio.get_wav_data())

def save_txt(text):
    save_into_file = input("Do you want to save your recording into a txt file? y/n: ")
    if (save_into_file == "y"):

        # create directory Text Results
        dirName="Text Results"
        if not os.path.isdir(dirName):
            os.mkdir(dirName)

        # write audio to a TXT file + asks for filename etc...
        check = True
        while check == True:
            filename = input("Save recording as: ")
            if (os.path.exists(filename + ".txt")):
                overwrite = input("This file already exists, do you want to overwrite it? y/n: ")
                if (overwrite == "y"):
                    check = False
            else:
                check = False

        with open (os.path.join(dirName,filename+".txt"), "w") as f:
            f.write(text)



def main():
    audio=listen()
    to_text(audio)
    save_mp3(audio)

if __name__== "__main__":
   main()