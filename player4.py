import os
import sys
import time
import threading
from flask import Flask, request
import requests

# 🧼 Hide pygame welcome message
sys.stdout = open(os.devnull, "w")
import pygame
sys.stdout = sys.__stdout__

# 🎵 Initialize Pygame Mixer
pygame.mixer.init()

# 🔊 Songs Mapping (with descriptive titles)
song_map = {
    "song1": {"file": "song1.mp3", "title": "🎶 Calm Piano Melody"},
    "song2": {"file": "song2.mp3", "title": "🎸 Rock Guitar Jam"},
    "song3": {"file": "song3.mp3", "title": "🌊 Ocean Vibes"},
    "song4": {"file": "song4.mp3", "title": "🕺 Dance Floor Beats"}
}

last_played = ""

# 🌐 Flask Setup
app = Flask(__name__)
current_song = {"song": ""}

@app.route('/set', methods=['POST'])
def set_song():
    song = request.args.get("name")
    current_song["song"] = song
    return f"Set to play: {song}"

@app.route('/get', methods=['GET'])
def get_song():
    return current_song["song"]

@app.route('/nowplaying', methods=['GET'])
def now_playing():
    if last_played and last_played in song_map:
        return f"Currently playing: {song_map[last_played]['title']}"
    return "Nothing is playing right now."

# 🚫 Hide Flask logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

# 🎵 Music Player Loop
def music_player():
    global last_played
    print("🎧 Waiting for commands...")
    while True:
        try:
            song_name = current_song["song"].strip().lower()

            if song_name == "exit":
                print("🛑 Exit command received. Stopping player...")
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                    print("⏹️ Music stopped.")
                break

            if song_name and song_name != last_played and song_name in song_map:
                title = song_map[song_name]["title"]

                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                    print("⏹️ Stopped current song.")

                print(f"\n🎵 New song requested: {title}")
                pygame.mixer.music.load(song_map[song_name]["file"])
                pygame.mixer.music.play()
                print(f"▶️ Now playing: {title}")
                last_played = song_name

            time.sleep(1)

        except Exception as e:
            print("❌ Error:", e)
            time.sleep(3)

# 🚀 Start Flask in background
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    print("🌐 Flask server running at: http://192.168.31.79:5000")
    music_player()
