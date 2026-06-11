import os
import threading
import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import winsound
import pystray
import schedule

def show_reminder():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    root = tk.Tk()
    root.withdraw()

    root.attributes("-topmost", True)

    messagebox.showinfo("Clock in reminder", "Time to Clock in!!!")

    root.destroy()


def run_scheduler():

    REMINDER_TIME = "8:57"

    schedule.every().monday.at(REMINDER_TIME).do(show_reminder)
    schedule.every().tuesday.at(REMINDER_TIME).do(show_reminder)
    schedule.every().wednesday.at(REMINDER_TIME).do(show_reminder)
    schedule.every().thursday.at(REMINDER_TIME).do(show_reminder)
    schedule.every().friday.at(REMINDER_TIME).do(show_reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)

def create_thumbnail(): ##Create Stray app Icon 
    image = Image.new("RGB", (64,64), "blue")
    dc = ImageDraw.Draw(image)
    dc.ellipse((16,16,48,48), fill = "white")
    return image

def on_quit():
    icon.stop()
    os._exit(0)

icon = pystray.Icon(
    "ClockInReminder",
    icon=create_thumbnail(),
    title="Clock In Reminder Active",
    menu=pystray.Menu(pystray.MenuItem("Exit Program", on_quit)),
)

scheduler_thread = threading.Thread(target=run_scheduler, daemon = True)
scheduler_thread.start()
print("Application running in system stray")
icon.run()
