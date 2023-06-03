import tkinter as tk
#用于清空输出栏的内容
def clear_output(text_output):
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)
    text_output.config(state=tk.DISABLED)
