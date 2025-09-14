import tkinter as tk
from tkinter import messagebox

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.resizable(False, False)

        self.running = False
        self.time_left = 0
        self.timer_id = None

        self.min_var = tk.StringVar()
        self.sec_var = tk.StringVar()

        tk.Label(root, text="Minutes:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.min_var, width=5, font=("Consolas", 14)).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Seconds:").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(root, textvariable=self.sec_var, width=5, font=("Consolas", 14)).grid(row=0, column=3, padx=5, pady=5)

        self.display = tk.Label(root, text="00:00", font=("Consolas", 40), fg="blue")
        self.display.grid(row=1, column=0, columnspan=4, pady=20)

        tk.Button(root, text="Start", command=self.start, width=10, font=("Consolas", 12)).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(root, text="Pause", command=self.pause, width=10, font=("Consolas", 12)).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(root, text="Reset", command=self.reset, width=10, font=("Consolas", 12)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(root, text="Exit", command=root.quit, width=10, font=("Consolas", 12)).grid(row=2, column=3, padx=5, pady=5)

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.display.config(text=f"{minutes:02d}:{seconds:02d}")

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.timer_id = self.root.after(1000, self.countdown)
        elif self.time_left == 0 and self.running:
            self.running = False
            self.update_display()
            messagebox.showinfo("Time's up!", "The timer has finished!")

    def start(self):
        if not self.running:
            try:
                mins = int(self.min_var.get() or 0)
                secs = int(self.sec_var.get() or 0)
                self.time_left = mins * 60 + secs
                if self.time_left <= 0:
                    messagebox.showwarning("Error", "Enter a valid time!")
                    return
            except ValueError:
                messagebox.showwarning("Error", "Enter valid numbers!")
                return
            self.running = True
            self.update_display()
            self.countdown()

    def pause(self):
        if self.running:
            self.running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

    def reset(self):
        self.running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.time_left = 0
        self.update_display()
        self.min_var.set("")
        self.sec_var.set("")

root = tk.Tk()
app = Timer(root)
root.mainloop()
