import tkinter as tk
from time import perf_counter

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.minsize(width=260, height=100)

        # Time tracking
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.has_started = False  # To manage "Ready!" state

        # Display label
        self.label = tk.Label(root, text="Ready!", font=("Verdana", 30, "bold"))
        self.label.pack(pady=5)

        # Buttons frame
        frame = tk.Frame(root)
        frame.pack()

        self.start_btn = tk.Button(frame, text="Start", width=7, command=self.start)
        self.stop_btn = tk.Button(frame, text="Stop", width=7, state="disabled", command=self.stop)
        self.reset_btn = tk.Button(frame, text="Reset", width=7, state="disabled", command=self.reset)

        self.start_btn.pack(side="left", padx=2)
        self.stop_btn.pack(side="left", padx=2)
        self.reset_btn.pack(side="left", padx=2)

        self.update_clock()

    def format_time(self, seconds):
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hrs:02}:{mins:02}:{secs:02}"

    def update_clock(self):
        if self.running:
            current_time = perf_counter() - self.start_time + self.elapsed_time
            self.label.config(text=self.format_time(current_time))
        self.root.after(200, self.update_clock)

    def start(self):
        if not self.running:
            self.start_time = perf_counter()
            self.running = True
            self.has_started = True

            # Change Ready → 00:00:00 immediately on first start
            if self.elapsed_time == 0:
                self.label.config(text="00:00:00")

            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.reset_btn.config(state="normal")

    def stop(self):
        if self.running:
            self.elapsed_time += perf_counter() - self.start_time
            self.running = False
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Match original behavior
        if not self.has_started:
            self.label.config(text="Ready!")
        else:
            self.label.config(text="00:00:00")

        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.reset_btn.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()