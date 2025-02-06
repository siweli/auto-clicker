from pynput.keyboard import KeyCode, Key
a = str(Key.f9)
b = str(KeyCode(char="b"))


b = b.strip("'")
print(b)

