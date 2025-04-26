import pyautogui
import time
import os

# Changed from cc -> mouse
def collect_pixel_colors(num_samples=10, delay_between_samples=1):
    colors = []
    print(f"Starting color collection: {num_samples} samples...")
    for _ in range(num_samples):
        x, y = pyautogui.position()
        color = pyautogui.screenshot().getpixel((x, y))
        colors.append((x, y, color))
        print(f"Captured color at ({x},{y}): {color}")
        time.sleep(delay_between_samples)
    return colors

def build_godot():
    print("Starting Godot build...")
    os.system("scons platform=windows target=debug")  # work in progress need to work out build / flips

if __name__ == "__main__":
    collected_colors = collect_pixel_colors()
    for c in collected_colors:
        print(c)
    build_godot()