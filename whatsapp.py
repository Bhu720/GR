import pyautogui as spam
import time

limit = int(input('Enter the number of messages: '))
msg = input('Enter the message to spam: ')
i = 0  # Initialize
time.sleep(10)

while i < limit:
    spam.typewrite(msg)
    spam.press('enter')
    i += 1
