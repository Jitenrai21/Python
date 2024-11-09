import time
# pip install plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please! Drink water.",
            message = "Water is vital to our health. Water should almost always be your go-to beverage.",
            app_icon = r"C:\Users\ACER\OneDrive\Desktop\Python\glass_fill_water_icon_175790.ico",
            timeout = 3 #pops for 3 seconds
        )
        time.sleep(60*60)  # To set the timer of 60 seconds * 60 equals an hour.

# run: pythonw ./reminder_app.py  -> To the run the code in background.