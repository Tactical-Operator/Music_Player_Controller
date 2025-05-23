import time
import requests
import pygame
import sys

pygame.mixer.init()

song_map = {
    "song1": "song1.mp3",
    "song2": "song2.mp3",
    "song3": "song3.mp3",
    "song4": "song4.mp3"
}

last_played = ""
REPLIT_URL = ""  # Replace this

while True:
    try:
        res = requests.get(f"{REPLIT_URL}/get")
        song_name = res.text.strip().lower()

        if song_name == "exit":
            print("🛑 Exit command received. Stopping player...")

            try:
                for _ in range(3):
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                        print("⏹️ Music stopped.")
                        time.sleep(0.5)
            except Exception as stop_err:
                print("⚠️ Error while stopping music:", stop_err)

            break

        if song_name and song_name != last_played and song_name in song_map:
            print(f"\n🎵 New song requested: {song_name}")

            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                print("⏹️ Stopped current song.")

            pygame.mixer.music.load(song_map[song_name])
            pygame.mixer.music.play()
            print(f"▶️ Now playing: {song_name}")
            last_played = song_name

        time.sleep(1)

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(5)

print("✅ Player exited cleanly.")
