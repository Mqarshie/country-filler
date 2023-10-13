import keyboard
import time

with open('countries.txt', 'r') as file:
    countries = file.read().splitlines()

def write_countries(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'shift':
        for country in countries:
            time.sleep(0.00001)
            keyboard.write(country)
keyboard.on_press(write_countries)
keyboard.wait('esc') 