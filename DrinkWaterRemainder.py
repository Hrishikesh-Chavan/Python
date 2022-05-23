import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water",
            app_icon = "D:\Programming\Cool Programs\Drink Water Remainder\icon.ico", # Change directory accorfing to icon folder.
            message = "Stay hydrated !! it helps to cool your mind, preventing constipation, stabilizing the heartbeat, hydrate Skin,, look cool, flushing bacteria from your bladder.",
            timeout = 5
        )
        time.sleep(60 * 60)

