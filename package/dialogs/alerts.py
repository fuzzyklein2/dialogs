#!/usr/bin/env python3

from pathlib import Path

import tkinter as tk
from tkinter import ttk, messagebox

from .dialog import Dialog

class Alert(Dialog):
    def __init__(self, text: str, title: str = 'Alert'):
        super().__init__(title)
        self.text = text
        self.tk_msg_function = None

    def run(self):
        self.window = tk.Toplevel(self.parent)
        self.window.withdraw()
        result = self.tk_msg_function( self.title, self.text, parent=self.window)
        self.window.destroy()
        return result

class InfoDialog(Alert):
    def __init__(self, text: str, title: str = "Info"):
        super().__init__(text, title)
        self.tk_msg_function = messagebox.showinfo

class WarningDialog(Alert):
    def __init__(self, text: str, title: str = "Warning"):
        super().__init__(text, title)
        self.tk_msg_function = messagebox.showwarning
    
class ErrorDialog(Alert):
    def __init__(self, text: str, title: str = "Error"):
        super().__init__(text, title)
        self.tk_msg_function = messagebox.showerror

class QuestionDialog(Alert):
    def __init__(self, text: str, title: str = "Question"):
        super().__init__(text, title)
        self.tk_msg_function = messagebox.askyesno

class AboutDialog(Alert):
    def __init__(self, text: str = "", title: str = f"TODO: Put the calling program's name here."):
        super().__init__(title)
        self.tk_msg_function = messagebox.showinfo

# --- Convenience wrapper functions ---
def info(text: str, title: str = "Info"):
    return InfoDialog(text=text, title=title).run()

def warning(text: str, title: str = "Warning"):
    return WarningDialog(text=text, title=title).run()

def error(text: str, title: str = "Error"):
    return ErrorDialog(text=text, title=title).run()

def question(text: str, title: str = "Question") -> bool:
    return QuestionDialog(text=text, title=title).run()


if __name__ == '__main__':
    response = InfoDialog('This is just a test.').run()
    
