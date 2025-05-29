import ffmpeg
from faster_whisper import Whisper

# Extract audio from video
def extract_audio(video_path, audio_path="audio.wav"):
    ffmpeg.input(video_path).output(audio_path, format="wav").run()
    return audio_path

# Transcribe audio to text
def transcribe_audio(audio_path):
    model = Whisper("medium")  # You can use "small", "medium", or "large"
    segments, _ = model.transcribe(audio_path)
    subtitles = []
    for segment in segments:
        subtitles.append(f"{segment.start:.2f} --> {segment.end:.2f}\n{segment.text}\n")
    return subtitles

# Save subtitles to file
def save_subtitles(subtitles, output_file="subtitles.srt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for i, subtitle in enumerate(subtitles, start=1):
            f.write(f"{i}\n{subtitle}\n")

# Example Usage
video_path = "input.mp4"
audio_path = extract_audio(video_path)
subtitles = transcribe_audio(audio_path)
save_subtitles(subtitles)

print("Subtitles generated successfully!")