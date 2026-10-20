#!/usr/bin/env python3

from pathlib import Path

from abc import ABC, abstractmethod
import tkinter as tk

from . import get_root
from .constants import *

class Dialog(ABC):
    def __init__(self, title: str = "", width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        self.title = title
        self.width = width
        self.height = height
        self.parent = get_root()
        self.window = None

    @abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError

    def _center_window(self):
        self.window.update_idletasks()
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()
        x = (screen_w - self.width) // 2
        y = (screen_h - self.height) // 2
        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
