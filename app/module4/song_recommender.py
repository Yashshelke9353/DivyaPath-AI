import pandas as pd
from pathlib import Path

# Path to CSV file
DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "mood_song.csv"

# Load CSV
df = pd.read_csv(DATA_PATH)

# Clean the dataset
# Remove rows where mood or song is missing
df = df.dropna(subset=["mood", "song"])

# Normalize mood values
df["mood"] = df["mood"].astype(str).str.strip().str.lower()

def recommend_songs(emotion, top_n=5):
    """
    Return a list of songs for the given emotion.
    Each item is a dict: {song, artist, language, category}
    """
    emotion = emotion.lower().strip()

    matches = df[df["mood"] == emotion]

    if matches.empty:
        return []

    # Randomly pick up to top_n songs
    result = matches.sample(min(top_n, len(matches)))

    return result[["song", "artist", "language", "category"]].to_dict(
        orient="records"
    )