import sys
import ctypes

class Caja_mensaje():
    def mbox(title, text, style):
        ctypes.windll.user32.MessageBoxW(0, text, title, style)