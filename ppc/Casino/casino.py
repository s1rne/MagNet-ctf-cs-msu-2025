import time
import keyboard
import pyautogui


def run_macro():
    actions = ["1", "enter", "surrender", "enter"]
    for action in actions:
        if action == "enter":
            pyautogui.press("enter")
        else:
            pyautogui.write(action)
        time.sleep(0.1)


def main():
    macro_running = False

    print("Press S to start.")
    while True:
        if keyboard.is_pressed("s"):
            macro_running = True
        if macro_running:
            run_macro()
        if keyboard.is_pressed("q"):
            break

        time.sleep(0.1)


if __name__ == "__main__":
    main()
