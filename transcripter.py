import speech_recognition as sr
from pydub import AudioSegment
from os import remove
from os import path
import sys

# transcribe function that takes audio file and splits it according to the value of td to then process
# by chuncks
def transcribe_by_minute(AUDIO_FILE, td, f):
    for i in range(15):
        t1 = i * td   
        t2 = t1 + td

        # breaks the audio file for better handling
        # split points are given by td
        newAudio = AudioSegment.from_wav(AUDIO_FILE)
        newAudio = newAudio[t1:t2]
        audioName = "segment" + str(i) + ".wav"
        newAudio.export(audioName, format="wav")

        #geats audio split for processing
        audio_split = path.join(path.dirname(path.realpath(__file__)), audioName)

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(audio_split) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Sphinx
        try:
            print("Converting...Time frame: {0:0.2f} - {1:0.2f}  minutes.".format(i, i + (td/60000)) + "\n")
            f.write("Time frame: {0:0.2f} - {1:0.2f}  minutes.\n".format(i, i + (td/60000)) + r.recognize_sphinx(audio) + "\n\n")
        #except sr.UnknownValueError:
        #   print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        
        remove(audioName)
        f.flush()

    print("Process complete")

def main():
    # obtains audio file
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), sys.argv[1])

    # if -td flag is used then set the time differential as the next cmd arg
    # else use standard 1 minute
    if len(sys.argv) >= 2 and sys.argv[2] == "-td":
        td = int(sys.argv[3]) * 60000
    else:
        td = 60000

    print("Processing {} for conversion".format(sys.argv[1]))
    print("Time differential set to {} minutes\n".format(td/60000))

    # creates .txt file to hold transcript
    try:
        file_name = sys.argv[1]
        file_name.replace('.','')
        file_name = file_name + ".txt"
        f = open(file_name, "w+")

    except Exception as e:
        print("Error {} : ".format(e) ) 

    transcribe_by_minute(AUDIO_FILE,td,f)
    f.close()


if __name__ == "__main__":
    main()