from webbrowser import open
from pynput.keyboard import Key, Controller
from time import sleep

def open_page():
    return open("https://docs.google.com/presentation/d/1A_gSpGxHqsjckKzlNhxSvht-lioFmDR8sUTRrJwur04/edit#slide=id.p")
    
def keycommand(key1, key2):
    keyboard = Controller()
    keyboard.press(key1)
    keyboard.press(key2)
    keyboard.release(key1)
    keyboard.release(key2)

def main():
    open_page()
    sleep(5)
    keycommand(Key.ctrl, Key.f5)


if __name__ == "__main__":
    main()