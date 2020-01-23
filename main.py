import sys
import pyautogui
import time
import pyperclip
import os
import random


def send_msg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('esc')


def click_image(path, offset=0):
    location = pyautogui.locateCenterOnScreen(path)
    if location:
        x, y = location
        print(x/2, y/2)
        pyautogui.moveTo(x/2 + offset,y/2)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        # pyautogui.mouseUp()
    else:
        return False
        
def click(x, y):
    pyautogui.mouseDown(x, y)
    pyautogui.mouseUp(x, y)


def search_user(user):
    pyautogui.hotkey('command', '1')
    click_image(f'{MEDIA_PATH}search_icon.png', 30)
    pyperclip.copy(user)
    pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('down')
    pyautogui.keyDown('enter')
    time.sleep(1)


def add_all_users():
    with open("user_list.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        for user in text.split('\n'):
            print(user)
            pyautogui.hotkey('command', '2')
            pyautogui.hotkey('command', '1')
            # click_image(f'{MEDIA_PATH}add_user.png')
            click(1415.0, 22.0)
            pyperclip.copy(user)
            pyautogui.hotkey('command', 'v')
            pyautogui.keyDown('tab')
            pyautogui.hotkey('command', 'v')
            # click_image(f'{MEDIA_PATH}add_user_submit_button.png')
            click(1270.5, 362.0)
            # time.sleep(10)


def send_to_all_users():
    with open("user_list.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        for user in text.split('\n'):
            search_user(user)
            send_msg()




def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print(text)
        return text


def initialize():
    print(f'Monitor size : {pyautogui.size()}')
    print(pyautogui.position())
    msg = set_import_msg()
    return msg


def main():
    msg = initialize()
    add_all_users()
    # send_to_all_users()
    # search_user()
    # send_msg(msg)
    return


# config
MEDIA_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static/'
# pyautogui.PAUSE = 0.1

if __name__ == "__main__":
    main()