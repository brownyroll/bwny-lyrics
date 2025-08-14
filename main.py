import sys
import time
import json
import os

SONG_LIST_FILE = "song.json"

def load_song_list():
    with open(SONG_LIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def choose_song(songs):
    print("\nSelect song :")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['song']} - {song['artist']}")
    choice = int(input("\ntype number song : ")) - 1
    if 0 <= choice < len(songs):
        return songs[choice]
    else:
        print("\nNumber not valid")
        return None

def load_lyrics(file_path):
    if not os.path.exists(file_path):
        print(f"\nNot found: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def printLyrics(lyrics_data):
    for line in lyrics_data:
        text = line.get("text", "")
        char_delay = float(line.get("char_delay", 0.05))
        after_delay = float(line.get("delay", 0.5))

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            # print(char, end="")
            # sys.stdout.flush()
            time.sleep(char_delay)
        print()
        time.sleep(after_delay)

        sys.stdout.write("\r" + " " * len(text) + "\r")
        sys.stdout.flush()

def main():
    songs = load_song_list()
    song = choose_song(songs)
    if not song:
        print("\nNo song selected.")
        print("Exiting...")
        # main()
        return

    lyrics_data = load_lyrics(song["lyrics"])

    print(f"\nPlaying : {song['song']} - {song['artist']}")
    print(f"Album : {song['album']}")
    print(f"URL: {song['url']}\n")

    printLyrics(lyrics_data)

if __name__ == "__main__":
    main()
