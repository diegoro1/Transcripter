import speech_recognition as sr
from pydub import AudioSegment
import os

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "HashtagFundamental.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

for i in range(15):
    t1 = i * 240000    
    t2 = t1 + 240000

    newAudio = AudioSegment.from_wav(AUDIO_FILE)
    newAudio = newAudio[t1:t2]
    audioName = "test" + str(i) + ".wav"
    newAudio.export(audioName, format="wav")

    audio_split = path.join(path.dirname(path.realpath(__file__)), audioName)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(audio_split) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    
    os.remove(audioName)