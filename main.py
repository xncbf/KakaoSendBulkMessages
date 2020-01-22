import sys
import pyautogui
import time
import pyperclip
import os
import random


def send_msg(msg):
    for i in range(1):
        time.sleep(1)
        pyautogui.keyDown('enter')
        pyperclip.copy(msg)
        pyautogui.hotkey('command', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')


def add_user():
    time.sleep(1)
    pyautogui.hotkey('command', '1')
    time.sleep(1)
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    click_image(f'{MEDIA_PATH}add_user.png')
    pyperclip.copy('010')
    pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('tab')
    pyautogui.hotkey('command', 'v')
    click_image(f'{MEDIA_PATH}add_user_submit_button.png')
    # pyautogui.keyDown('esc')
    
    # for i in range(1):
    #     pyautogui.keyDown('down')
    time.sleep(2)


def search_user():
    time.sleep(1)
    pyautogui.hotkey('command', '1')
    time.sleep(1)
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    click_image(f'{MEDIA_PATH}search_icon.png', 30)
    pyperclip.copy('도희')
    pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('down')
    pyautogui.keyDown('enter')
    # pyautogui.keyDown('esc')
    
    # for i in range(1):
    #     pyautogui.keyDown('down')
    time.sleep(2)


def click_image(path, offset=0):
    location = pyautogui.locateCenterOnScreen(path)
    if location:
        x, y = location
        pyautogui.moveTo(x/2 + offset,y/2, 0.5)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        # pyautogui.mouseUp()
    else:
        return False



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
    search_user()
    # add_user()
    # send_msg(msg)
    return


# config
MEDIA_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static/'
pyautogui.PAUSE = 0.5

if __name__ == "__main__":
    main()