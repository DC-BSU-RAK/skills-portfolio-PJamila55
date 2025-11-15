# Codelab II
# Assessment 1 - Exercise 2 : Alexa tell me a Joke
# Princess Jamila Dinglasan

import tkinter as tk # used to make the GUI window
import random # randomizer

def load_jokes(): # opens the txt file containing all the jokes
    jokes = [] # Makes an empty list to store the jokes
    file = open('Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/randomJokes.txt', 'r') # where to find the txt file
    for line in file:
        line = line.strip()
        if '?' in line: # splits the line into the joke / punchline depending on where ? is
            parts = line.split('?', 1)
            setup = parts[0] + '?' # Re-add the ? so the joke looks natural
            punchline = parts[1]
            jokes.append({'setup': setup, 'punchline': punchline})
    file.close()
    return jokes # loads all jokes into a list

all_jokes = load_jokes()
current_joke = None

def tell_joke(): # picks a random joke and saves it in current_joke
    global current_joke
    current_joke = random.choice(all_jokes)
    setup_label.config(text=current_joke['setup'])
    punchline_label.config(text="")

def show_punchline(): # If a joke has been selected, itll show punchline
    if current_joke:
        punchline_label.config(text=current_joke['punchline'])

def quit_app(): # closes the window
    window.quit()

window = tk.Tk() # main Tkinter window
window.title("Funny-Ish Jokes") # title you see on top
window.geometry("600x600") # size / dimensions of the window
window.config(bg="lightgray")

main_frame = tk.Frame(window, bg="lightgray")
main_frame.pack(expand=True, fill="both", padx=30, pady=30)

inner_frame = tk.Frame(main_frame, bg="#3E4A59", width=540, height=540) # gray box where stuff is in
inner_frame.pack(expand=True)
inner_frame.pack_propagate(False)

setup_label = tk.Label(inner_frame, text='Click below to hear a joke!', font=("Courier", 18, "bold"), 
                       bg="#3E4A59", fg="white", wraplength=480, justify="center")
setup_label.pack(pady=(80,10))

punchline_label = tk.Label(inner_frame, text='', font=("Courier", 14, "bold"),  # Empty until user clicks “Show Punchline”
                           bg="#3E4A59", fg="cyan", wraplength=480, justify="center")
punchline_label.pack(pady=10)

joke_button = tk.Button(inner_frame, text="Alexa, tell me a joke!", command=tell_joke, # Shows the joke
                        font=("Courier", 12, "bold"), bg="cyan", fg="indigo", 
                        width=25, height=2)
joke_button.pack(pady=(40, 10))

punchline_button = tk.Button(inner_frame, text="Show Punchline", command=show_punchline, # shows the punchline
                             font=("Courier", 12, "bold"), bg="indigo", fg="white", 
                             width=25, height=2)
punchline_button.pack(pady=10)

button_frame = tk.Frame(inner_frame, bg="#3E4A59")
button_frame.pack(pady=50)

quit_button = tk.Button(button_frame, text="Quit", command=quit_app, # closes the window
                       font=("Courier", 11, "bold"), bg="white", fg="dodgerblue", 
                       width=12, height=2)
quit_button.pack(side="left", padx=15)

next_button = tk.Button(button_frame, text="Next Joke", command=tell_joke, # shows another different joke
                       font=("Courier", 11, "bold"), bg="white", fg="dodgerblue", 
                       width=12, height=2)
next_button.pack(side="left", padx=15)

window.mainloop() # keeps window open with loop

# Thank you! :)