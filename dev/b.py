from pynput.keyboard import KeyCode, Key
import string

a = "a"


if a in string.ascii_letters + string.digits:
    print(a)
else:
    for i in Key:
        if a.upper() == str(i).split(".")[1].upper():
            print(i)
