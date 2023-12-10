import speech_recognition as sr
from datetime import timedelta

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # Read the entire audio file
    return r.recognize_google(audio)  # Use Google Speech Recognition to transcribe the audio

def generate_subtitle(timestamp, text):
    subtitle = ""
    subtitle += f"{timestamp}\n"
    subtitle += f"{text}\n"
    subtitle += "\n"  # Add a blank line between subtitles
    return subtitle
def save_subtitles(subtitles, output_file):
    with open(output_file, "w") as file:
        file.writelines(subtitles)
def create_subtitles():
    video_file = input("Enter the path to the video file: ")
    audio_file = input("Enter the path to the audio file: ")
    output_file = input("Enter the path for the output subtitle file: ")    
    subtitles = []
    # Transcribe audio
    transcript = transcribe_audio(audio_file)
    # Generate subtitles
    lines = transcript.split(". ")  # Split transcript into lines based on periods followed by a space
    timestamp = timedelta(seconds=0)  # Initial timestamp
    for line in lines:
        text = line.strip()
        subtitle = generate_subtitle(timestamp, text)
        subtitles.append(subtitle)
        timestamp += timedelta(seconds=5)  # Increment timestamp by 5 seconds for the next subtitle
    # Save subtitles
    save_subtitles(subtitles, output_file)
# Usage
create_subtitles()
