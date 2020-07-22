import pyautogui
import time

STRING = 'Look at me, I am a string!'
KEY_LIST_UPPER = ['W', 'A', 'S', 'D']
KEY_LIST_LOWER = ['w', 'a', 's', 'd']


def key_hold(key_to_hold):
    pyautogui.keyDown(key_to_hold)


def key_press(key_to_press):
    pyautogui.press(key_to_press)


def key_release(key_to_release):
    pyautogui.keyUp(key_to_release)


def prompt_to_start():
    msg = 'Click okay to start.\n Starts in 5 seconds.'
    pyautogui.alert(msg)


def remove_string(string_to_remove=STRING):
    string_length = len(string_to_remove)
    for i in range(string_length):
        key_press('backspace')


def type_string(string_to_type=STRING):
    for character in string_to_type:
        key_press(character)


def wait_this_many_seconds(seconds):
    time.sleep(seconds)


def main():
    for i in range(9999):
        time.sleep(2)
        type_string()
        time.sleep(2)
        remove_string()


if __name__ == '__main__':
    main()
