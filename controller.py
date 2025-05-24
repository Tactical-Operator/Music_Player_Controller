import requests
import os
import platform


REPLIT_URL = ""

def clear():
    
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def send_command(command):
    try:
        response = requests.post(f"{REPLIT_URL}/set?name={command}")
        if response.status_code == 200:
            print(f"\n✅ Command sent: {command}")
        else:
            print(f"\n❌ Server error (status code {response.status_code})")
    except Exception as e:
        print(f"\n❌ Failed to send command: {e}")

def main():
    while True:
        clear()
        print("🎮 Remote Music Controller")
        print("-------------------------")
        print("1. Play Song 1")
        print("2. Play Song 2")
        print("3. Play Song 3")
        print("4. Play Song 4")
        print("5. Stop Music & Exit")

        choice = input("\nEnter your choice (1–5): ").strip()

        song_map = {
            "1": "song1",
            "2": "song2",
            "3": "song3",
            "4": "song4"
        }

        if choice == "5":
            send_command("exit")  
            print("\n👋 Music stopped. Controller exiting...")
            break
        elif choice in song_map:
            send_command(song_map[choice])
        else:
            print("\n❗ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
