import whisper
import os
import tqdm
import time
from tqdm import tqdm

# Load the Whisper model
print("Loading Whisper model... Please wait.")
model = whisper.load_model("large")  # Options: tiny, base, small, medium, large

# Path to the WAV file
audio_file = "Sinder Summons You to Hell 🔥【VTuber ASMR RP】 [BnlLUBwgaRk].wav"

# Check file existence
if not os.path.exists(audio_file):
    raise FileNotFoundError(f"Audio file '{audio_file}' not found.")

# Simulated Progress Bar for Loading Audio File
print("Loading audio file...")
for _ in tqdm(range(100), desc="Loading Audio", ncols=100):
    time.sleep(0.01)  # Simulated delay for the progress bar

# Transcribe the audio with progress updates
print("Transcribing audio... This may take some time.")
try:
    # Show progress in chunks
    with tqdm(total=100, desc="Transcribing", ncols=100) as pbar:
        result = model.transcribe(
            audio_file, 
            language="en",
            word_timestamps=True,
            initial_prompt="This is a roleplay involving a hellhound named Cinder, who summons a human to Hell. Dialogue includes fantasy and roleplay elements.",
            verbose=False
        )
        for _ in range(100):
            time.sleep(0.05)  # Simulated chunk progress
            pbar.update(1)
except Exception as e:
    print(f"An error occurred during transcription: {e}")
    exit(1)

# Save transcription to a file
output_file = "transcription_refined_large.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcription complete! Saved to {output_file}")
