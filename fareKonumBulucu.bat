@echo off
cls
python -c "import pyautogui; from time import sleep; sleep(10); a = pyautogui.position(); print(a)" >> burda.txt

