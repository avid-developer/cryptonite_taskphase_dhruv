import time
import pyautogui
import subprocess

# Define the game command and keystrokes
game_command = "python3 handout/tetris.py"
keystrokes = "waaaaaaaaaaaaaaa aaaaaaaaaaaawww aaaaaaaaa aaaaaaaa aaaaaa aaaaaw aaaw aa a dd da ddd dddd ddd dddd ddddddd ddddd dddddddd ddddddddd dddddddddd ddddddddddd dddddddddddddddd ddddddddddddd dddddddddddddddww ddddddddddddddwww ddddddddddddd dddddddddddd dddddddddddd ddddddddddd dddddddddd ddddddddddd dddddddd ddddddddddww dddddddddddddw dddddd ddddd ddddd ddddd dddd dddwww dd d da awww aaaa aaaw wwwaaaaa aaaaaaa aaaaaaaa aaaaaaaaaw aaaaaaaaaa aaaaaaaaaaa aaaaaaaaaaaaaaw aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaa aaaaaaaaaaaa aaaaaaaaaaaaaw aaaaaaaaaaaaaaaa waaaaaaaaaaaaaaaa waaaaaaaaaaaa aaaaaaaaaawww aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaaa aaaaaaaaaaaa wwwaaaaaa waaaaa waaaa aa a aa a  d dd  d dd wwwddddd ddddddd wddddddddd wddddddddddddd wwwdddddddddddddd dddddddddddddddd dddddddddddddddd wdddd wddddddd dddddddd wwwddddddddd dddddddddd wddddddddd ddddddddddddd dddddddddddddd ddddddddddddddd wddddddddddddddd wwdddddddddddddd dddddddddddd dddddddddddddddd ddddddddddddddd  ddddd dddd ddd dd d aa waaaaaaa aaaa aaaaa aaaaaa aaaaaaa aaaa  a aa a ww ddddddddddddd wdddddddddddd dddddddddd wddddddddddd dddddddddddddddd dddddddddddddddd dddddddd ddddddddd ddddddd ddddd dddddd dddddd dddddddddddddd dddddddddddd ddddddddd ddddddddd dddddddddd dd dd aaaaaaaaaaaaaa aaaaaaaaaaaa waaaaaaaaa wwaaaaa aaaa aaaaaaa aaaaaaa aaaaaa aaaaaa wwwaaaaaaaaaa aaaaaaaaaa ddddddd ddddd wddd dddd ddd www dd ddd dddd wwd wdddd wwdddddd wddddddd ddddd ddddd dddddddd ddddddddd ddddddd ddddddddd dddddddd dddddddddd dddddddddd ddddddddddddd dddddddddddddd wdddddddddddddddd dddddddddddd ddddddddddddddd dddddddddddddddd ddddddddddddd ddddddddddddd dddddddddddddd ddddddddddddddd dddddddddddddddd dddddddddddddddd dddddddddddddd wddddddddddd dddddddd dddddddddd ddddddddd dddddddddd ddddddddddd dddddddddddd wwwddddddddddddd dddddddddddddddd dddddddddddddddd dddddddddddddd wddddddddddddd ddddddddddd wddddddd wdddddddd wwdddddd ddddd ddddddddddd ddddddddddddd wwdddddddd wwwddddddddddddddd dddddddddddd dddddddddddd ddddddddddddd dddddddddddddd dddddddddd dddddddd ddddddd dd ddd dddd  d d d dd ddd dddd wwwdd wdddddd dddd ddddd dddddd dddddddd wdddd wdddddd wwdddddddddd ddddddd ddddddddd ddddddddddd dddddddddddd ddddddddddddd dddddddddddddd ddddddddddddd dddddddd dddddddd dddddddd ddddd ddddddd dddddddddd dddddddddd ddddddddddd dddddddddddd wwdddddd ddddddddd dd d d wdddddddddddddddd ddddddddddddddd wdddddddddddddd wwwddddddddd wwdddddddddddd dddddddddd ddddddd ddddd wwwdddddddd wwdddddd wwdddddddd dddddddd dddddd dddddd dddddd ddddddd dddd wdd dd ddd ddddd d dd wdddddddddddd wwwaaa a aaaa aaa aa aa a aaaaaa waaaaa aaaaaaa a  a  aa aa aa aa wwa aa a d d d d dddddddddd ddd ddd wwwdd wddd wwdd wwdddddd dddddddd wddddddddd wdddddd wwddd ddddd ddddd ddddddddd ddddddd ddddddd wwwd ddddd ddd  a aa aa aa a  waaaa aaaa aaa aaaa aaaa aaaa waaa waaaa aaaa aaaa wwaaa a  aa a a a aaa aaaa aaaa waaaa aa w d  d dd dd wwwaaaaa wwaa aaaa aaaa aa aaa a aaaaa aaaa aaaaa "

# Function to run the game
def start_game(command):
    subprocess.Popen(command, shell=True)

# Function to send keystrokes
def send_keystrokes(keystrokes):
    for key in keystrokes:
        pyautogui.press(key)  # Simulate the keypress
        time.sleep(0.05)  # Delay between keypresses

# Start the game
print("Starting the game...")
start_game(game_command)

# Wait for 2 seconds to let the game load
time.sleep(2)

# Send keystrokes to the game
print("Sending keystrokes...")
send_keystrokes(keystrokes)

print("Automation completed.")