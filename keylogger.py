import keyboard
keys = keyboard.record(until="ESC")
input("ready")
keyboard.play(keys)
