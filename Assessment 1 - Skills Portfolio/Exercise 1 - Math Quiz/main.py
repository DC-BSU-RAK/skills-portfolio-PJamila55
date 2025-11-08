# Codelab II
# Assessment 1 - Exercise 1 : Math Quiz
# Princess Jamila Dinglasan

import tkinter as tk # Importing the Tkinter library for GUI
from tkinter import messagebox # For popup messages (Like the input valid number error)
import random # For number randomizer needed for questions

class MathQuiz: # Everything the game does lives in this class
    def __init__(self, root): # Basic customization
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("1024x576")
        self.root.configure(bg="#000000") # background color of the window to black
        
        # Variables to track (eg. How many questions user gets wrong)
        self.correct = 0
        self.wrong = 0
        self.question_num = 0
        self.difficulty = 0
        self.showMainMenu()
    
    def clearWindow(self): # used when window changes like eg. from menu to difficulty screen
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def showMainMenu(self): # Title screen things
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        canvas.create_rectangle(210, 85, 814, 465, fill="black", outline="white", width=3)
        
        canvas.create_text(380, 150, text="MATH", font=("Courier", 48, "bold"), fill="white")
        canvas.create_text(640, 150, text="QUIZ", font=("Courier", 48, "bold"), fill="white")
        
        canvas.create_oval(437, 255, 587, 355, fill="white", outline="black", width=5)
        canvas.create_text(512, 305, text="▶", font=("Arial", 50, "bold"), fill="black", tags="start_btn")
        canvas.tag_bind("start_btn", "<Button-1>", lambda e: self.displayMenu()) # Goes to difficulty screen
        
        tk.Button(canvas, text="INSTRUCTIONS", font=("Courier", 12, "bold"), bg="white", fg="black",
                 command=self.showInstructions, width=14, height=1, relief="raised", bd=3).place(x=280, y=400)
        tk.Button(canvas, text="ABOUT", font=("Courier", 12, "bold"), bg="white", fg="black",
                 command=self.showAbout, width=14, height=1, relief="raised", bd=3).place(x=440, y=400)
        tk.Button(canvas, text="CREDITS", font=("Courier", 12, "bold"), bg="white", fg="black",
                 command=self.showCredits, width=14, height=1, relief="raised", bd=3).place(x=600, y=400)
        
        canvas.bind("<Button-1>", lambda e: self.displayMenu() if 437 < e.x < 587 and 255 < e.y < 355 else None)
    
    def showInstructions(self): # makes new canvas, shows how to play
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        canvas.create_text(512, 130, text="INSTRUCTIONS", font=("Courier", 28, "bold"), fill="white")
        inst = "1. Choose difficulty level\n2. Type answer in text box\n3. Press Enter\n4. Answer more than half of 15 to win!"
        canvas.create_text(512, 280, text=inst, font=("Courier", 14), fill="white", justify="center")
        tk.Button(canvas, text="BACK", font=("Courier", 14, "bold"), bg="white", command=self.showMainMenu,
                 width=12, height=1, bd=3).place(x=432, y=400)
    
    def showAbout(self): # makes new canvas, shows info about the quiz
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        canvas.create_text(512, 130, text="ABOUT", font=("Courier", 28, "bold"), fill="white")
        canvas.create_text(512, 280, text="Some Math Quiz for a project I guess\n Goodluck gang ", 
                          font=("Courier", 16), fill="white", justify="center")
        tk.Button(canvas, text="BACK", font=("Courier", 14, "bold"), bg="white", command=self.showMainMenu,
                 width=12, height=1, bd=3).place(x=432, y=400)
    
    def showCredits(self): # Makes new canvas, credits with my name (hehe)
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        canvas.create_text(512, 130, text="CREDITS", font=("Courier", 28, "bold"), fill="white")
        canvas.create_text(512, 280, text="Created By: Princess Dinglasan\nThanks for playing!", 
                          font=("Courier", 16), fill="white", justify="center")
        tk.Button(canvas, text="BACK", font=("Courier", 14, "bold"), bg="white", command=self.showMainMenu,
                 width=12, height=1, bd=3).place(x=432, y=400)
    
    def displayMenu(self):
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        
        # Back arrow inside the box
        canvas.create_text(250, 120, text="◄", font=("Courier", 40, "bold"), fill="white", 
                          tags="back")
        canvas.tag_bind("back", "<Button-1>", lambda e: self.showMainMenu())
        
        canvas.create_text(512, 150, text="DIFFICULTY LEVEL", font=("Courier", 24, "bold"), fill="white")
        
        # Properly centered buttons (1024/2 = 512, button width ~240, so start at 512-120=392)
        tk.Button(canvas, text="EASY", font=("Courier", 16, "bold"), bg="white", fg="black",
                 command=lambda: self.startQuiz(1), width=18, height=2, bd=3).place(x=392, y=220)
        tk.Button(canvas, text="MEDIUM", font=("Courier", 16, "bold"), bg="white", fg="black",
                 command=lambda: self.startQuiz(2), width=18, height=2, bd=3).place(x=392, y=290)
        tk.Button(canvas, text="HARD", font=("Courier", 16, "bold"), bg="white", fg="black",
                 command=lambda: self.startQuiz(3), width=18, height=2, bd=3).place(x=392, y=360)
    
    def randomInt(self, level): # gives random numbers based on difficulty
        if level == 1: # Easy
            return random.randint(1, 9)
        elif level == 2: # Medium
            return random.randint(10, 99)
        else: # Hard
            return random.randint(1000, 9999)
    
    def decideOperation(self): # Randomizze questions between addition and subtraction
        return random.choice(['+', '-'])
    
    def startQuiz(self, level):# STARTS THE QUIZ
        self.difficulty = level
        self.correct = 0
        self.wrong = 0
        self.question_num = 0
        self.asked_questions = []
        self.displayProblem() # shows the first question
    
    def displayProblem(self):
        if self.question_num >= 10: # If you already answered 10 questions 
            self.displayResults() # show results
            return # exits displayProblem method (quiz over)
        
        self.clearWindow() # clears window for a new question
        self.question_num += 1 # question counter
        
        while True: # uses a while True loop to randomly generate a math problem
            num1, num2 = self.randomInt(self.difficulty), self.randomInt(self.difficulty) # generates 2 random numbers based on self.difficulty
            operation = self.decideOperation() # Randomly choose math operation
            question_key = (num1, num2, operation) # represents full math problem
            if question_key not in self.asked_questions: # sees if the new problem already exists in the self.asked_questions list
                self.asked_questions.append(question_key) # unique problem is saved to prevent repetition which I noticed keeps happening
                break # infinite loop is terminated
        
        self.current_answer = num1 + num2 if operation == '+' else num1 - num2
        
        # UI Things
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#000000", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        
        canvas.create_text(750, 110, text=f"Correct: {self.correct}", font=("Courier", 14, "bold"), 
                          fill="#90EE90", anchor="e")
        canvas.create_text(750, 135, text=f"Wrong: {self.wrong}", font=("Courier", 14, "bold"), 
                          fill="#FF6B6B", anchor="e")
        
        canvas.create_text(512, 140, text=f"QUESTION {self.question_num} OF 10", 
                          font=("Courier", 20, "bold"), fill="white")
        canvas.create_text(512, 220, text=f"{num1} {operation} {num2} = ?", 
                          font=("Courier", 40, "bold"), fill="white")
        
        self.answer_entry = tk.Entry(canvas, font=("Courier", 24), width=15, justify="center", bd=3)
        canvas.create_window(512, 300, window=self.answer_entry)
        self.answer_entry.focus()
        
        tk.Button(canvas, text="BACK", font=("Courier", 12, "bold"), bg="#FF6B6B", fg="black",
                 command=self.displayMenu, width=12, height=1, bd=3).place(x=320, y=370)
        tk.Button(canvas, text="ENTER", font=("Courier", 12, "bold"), bg="#90EE90", fg="black",
                 command=self.isCorrect, width=12, height=1, bd=3).place(x=520, y=370)
        
        self.answer_entry.bind('<Return>', lambda e: self.isCorrect())
    
    def isCorrect(self):
        # Checks if answer matches self.current_answer
        # If correct, adds 1 to self.correct
        # If wrong, adds 1 to self.wrong
        # Then shows the next question

        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_answer:
                self.correct += 1
            else:
                self.wrong += 1
            self.displayProblem()
        except ValueError: # If user types something that isn't a number
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def displayResults(self):
        self.clearWindow()
        canvas = tk.Canvas(self.root, width=1024, height=576, bg="#5B5B5B", highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(200, 75, 824, 475, fill="black", outline="white", width=8)
        
        # As mentioned earlier, if there is more self.correct than self.wrong, it'll change the end text accordingly
        result_text = "Great Job!" if self.correct > self.wrong else "Keep Practicing!"
        
        canvas.create_text(512, 160, text=result_text, font=("Courier", 36, "bold"), fill="white")
        canvas.create_text(512, 230, text=f"Correct: {self.correct}", 
                          font=("Courier", 20, "bold"), fill="#90EE90")
        canvas.create_text(512, 270, text=f"Wrong: {self.wrong}", 
                          font=("Courier", 20, "bold"), fill="#FF6B6B")
        
        tk.Button(canvas, text="PLAY AGAIN", font=("Courier", 14, "bold"), bg="#FF6B6B", fg="black",
                 command=self.displayMenu, width=12, height=1, bd=3).place(x=300, y=360)
        tk.Button(canvas, text="HOME", font=("Courier", 14, "bold"), bg="#90EE90", fg="black",
                 command=self.showMainMenu, width=12, height=1, bd=3).place(x=540, y=360)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuiz(root)
    root.mainloop() # Loops everything, keeps window up

    # Thank you hehe