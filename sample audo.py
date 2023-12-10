from pydub import AudioSegment
from pydub.playback import play

audio_file = "C:\\Users\\91638\\Desktop\\Yellae Lama.mp3"

# Load audio file
audio = AudioSegment.from_file(audio_file)

# Play audio
play(audio)
