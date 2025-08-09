# 🎵 Bwny Lyrics Player

A simple Python script to display song lyrics with timing effects.

---

## 📌 Add a Song

To add a new song, edit the `song.json` file and follow the format below:

**Example:**

```json
{
  "song": "your_song_name",
  "lyrics": "lyrics/your_song_name.json",
  "artist": "your_artist_name",
  "album": "your_album_name",
  "url": "https://your-song-url.com"
}
```

## 📌 Add Lyrics

To add a new lyrics file, create a JSON file in the lyrics/ directory.

**Example:**

```json
{
  "text": "This is an example lyric line.",
  "char_delay": 0.08,
  "delay": 0.5
}
```

- text: The lyric line to display.
- char_delay: Delay between each character (in seconds).
- delay: Delay after the line finishes (in seconds).

## 📌 Install Python
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

[Python Installation Guide](https://docs.python.org/3/using/index.html)

[Python Install Latest](https://www.python.org/downloads/)

## 🚀 How to Use

Clone this repository:

```bash
git clone https://github.com/brownyroll/bwny-lyrics.git
```

Navigate to the project directory:

```bash
cd bwny-lyrics
```

Run the script:

```bash
python main.py
```

### 🎯 How to Choose a Song

- When you run the script, you will see a list of available songs from song.json.

- Enter the number of the song you want to play.

- Type exit to quit the program.

### 💡 How to Contribute

- You can help improve this project by:

- Adding new songs and lyrics.

- Fixing timing or text errors in existing lyrics.

- Improving code or adding new features.

## Steps:

- Fork the repository.

- Make your changes.

- Submit a pull request.

### 📂 Project Structure

- `main.py`: The main script to run the lyrics player.
- `song.json`: Contains the list of songs and their metadata.
- `lyrics/`: Directory containing individual lyric files in JSON format.
- `README.md`: This file, providing an overview and instructions.

```bash
📁 bwny-lyrics
 ├── 📁 lyrics/
 │   ├── still_waiting_for_your_reply.json
 │   └── your_song_name.json
 ├── main.py
 ├── requirements.txt
 ├── song.json
 └── README.md
```
