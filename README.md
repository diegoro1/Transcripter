# Transcripter

Transcripter is a command line app that takes .wav audio files and converts them into text. Transcripter uses the Speech Recognition python module to perform its operations offline using Sphinx. The audio files processed are split by a time differential given by the user without compromising the original audio. These split files are then converted into text and deleted once the process is done. All is done offline. 

A script is also provided to convert all mp3 files in the directory to .wav files if using a UNIX system.  

## Getting Started

This application is heavily dependent on the Speech Recognition module, therefore reading through their documentation is highly recommended but not completely necessary.  

### Prerequisites

- PocketSphinx
- SpeechRecognition Library
- Python 2.6, 2.7, or 3.3+ (required)


### Installing

First install PocketSphinx by running the following commands

```
pip install wheel
```

followed by

```
pip install ./third-party/WHEEL_FILENAME
```

If on OSX or on Linux please follow the amazing guide created by the creators of SpeechRecognition: [Here!](https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst)

Now install SpeechRecognition

```
pip install SpeechRecognition
```
Download transcripter.py and mp3_to_wav_converter.sh (optional)

You are all set!

## How to Run

Place transcripter.py in a directory with the .wav file to be converted. 
The format in which the command should be delivered is stated:

```
Python transcriter.py NAME_OF_FILE.wav
```

This will separate the text within a 1 minute time differential. To set a different time difference use the -td flag 

```
Python transcriter.py NAME_OF_FILE.wav -td [integer value of time in minutes]
```

The result will be placed in a .txt file named after the original audio. Running the program again with the same file or same file name will simply replace the former .txt file with the new text data. 

If the audio file is formatted as an mp3 and the user is running an UNIX machine, then run the following scrip to convert _ALL_ .mp3 files to .wav

```
chmod +x mp3_to_wav_converter.sh
```

Followed by

```
./script-name-here.sh
```

## Authors

* **Diego Rodrigues** ([diegoro1]( https://github.com/diegoro1))

## Acknowledgments

* Thank you SpeechRecognition team for the awesome library


