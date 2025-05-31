import tkinter as tk
from datetime import datetime
import requests
import pytz


def get_location_and_timezone():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
        timezone = data.get("timezone", "UTC")
        return city, country, timezone
    except Exception as e:
        print("Error getting location:", e)
        return "Unknown", "Unknown", "UTC"

def update_time():
    now = datetime.now(pytz.timezone(user_timezone))
    time_str = now.strftime('%H:%M:%S')
    clock_label.config(text=time_str)
    root.after(1000, update_time)


city, country, user_timezone = get_location_and_timezone()

root = tk.Tk()
root.title('World Clock')
root.geometry("1920x1080")
root.configure(bg='black')
root.attributes('-topmost', True)

# Location label (city + country)
location_label = tk.Label(root, text=f"{city}, {country}", font=('Helvetica', 80), bg='black', fg='white')
location_label.pack(pady=50)

# Time label
clock_label = tk.Label(root, font=('Helvetica', 300), bg='black', fg='lime')
clock_label.pack(expand=True, fill='both')

update_time()
root.mainloop()
