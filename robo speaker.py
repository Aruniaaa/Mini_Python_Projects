if __name__ == '__main__':
    pass

import pyttsx3 as pt

while True:
    cmd = input("Enter the command or enter Q to quit: ").lower()
    if cmd == 'q':
        quit()

    else:
        pt.speak(cmd)