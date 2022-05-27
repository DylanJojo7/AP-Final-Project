import pydub
from pydub import AudioSegment
import os

file = ""
name = ""
format = ""
bitrate = ""

def tryCreate():
    exists = os.path.exists("./output")

    if (not exists):
        os.mkdir("./output")


    fileName()

def fileName():

    print("Enter the name of your converted file (without format)")
    global name
    name = str(input(""))

    fileLocation()

def fileLocation():

    print("Enter the file location that you would like to convert.")
    f = str(input(""))
    try:
        global file
        file = AudioSegment.from_file(f)
    except:
        print("Invalid file location. Try again.")
        fileLocation()


    audioFormat()

def audioFormat():
    print("Select a Audio Type to convert to [mp2, mp3, flv, wav, ogg, opus]")
    global format
    format = " "

    while (format == " "):
        format = input(str(""))


        if (format == "mp3"):
            format = "mp3"
        elif (format == "flv"):
            format = "flv"
        elif (format == "wav"):
            format = "wav"
        elif (format == "ogg"):
            format = "ogg"
        elif (format == "opus"):
            format = "opus"
        elif (format == "mp2"):
            format = "mp2"
        else:
            print("Invalid audio format. Please try again.")
            format = " "


    bitrate()

def bitrate():

    print("Select a Bitrate to conver to [64k, 92k, 128k, 256k, 320k]")

    global bitrate
    bitrate = " "
    while (bitrate == " "):
        bitrate = str(input(""))

        if (bitrate == "64k"):
            bitrate = "64k"
        elif (bitrate == "92k"):
            bitrate = "92k"
        elif (bitrate == "128k"):
            bitrate = "128k"
        elif (bitrate == "256k"):
            bitrate = "256k"
        elif (bitrate == "320k"):
            bitrate = "320k"
        else:
            print("Invalid bitrate. Please try again.")
            birate = " "

    finalConvert()

def finalConvert():

    file.export("./output/" + name + "." + format, format=format, bitrate=bitrate)
    print("File has been converted and is in output folder.")

if __name__ == "__main__":
    tryCreate()