import tkinter as tk
from gpiozero import LED

blueLED = LED(17)
greenLED = LED(27)
redLED = LED(22)

def toggle_led_state(led):
    if led.is_lit:
        led.off()
    else:
        led.on()

def toggle_button_background_color(button, color):
    if button.cget('bg') == "white":
        button.config(bg=color, fg="white")
    else:
        button.config(bg="white", fg="black")
    
    # Change activeforeground and activebackground to match the current bg and fg so that it doesnt change when hovering
    button.config(activebackground=button.cget('bg'), activeforeground=button.cget('fg'))

def toggle_button_and_led_state(led, button, color):
    toggle_led_state(led)
    toggle_button_background_color(button, color)
    
root = tk.Tk() # Creates the window

# Set up the buttons
blueButton = tk.Button(root, text="Blue", fg="black", bg="white", width=40, height=15, command= lambda: toggle_button_and_led_state(blueLED, blueButton, "blue"))
greenButton = tk.Button(root, text="Green", fg="black", bg="white", width=40, height=15, command= lambda: toggle_button_and_led_state(greenLED, greenButton, "green"))
redButton = tk.Button(root, text="Red", fg="black", bg="white", width=40, height=15, command= lambda: toggle_button_and_led_state(redLED, redButton, "red"))

# Send the buttons to the window
blueButton.pack()
greenButton.pack()
redButton.pack()

root.protocol("WM_DELETE_WINDOW", root.quit) # quits the window when closing it
root.mainloop() # Start GUI loop. Is a blocking function so wont register ctrl+c