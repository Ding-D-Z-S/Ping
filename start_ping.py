import tkinter as tk
import socket
import time
from ping_test_V2 import ping_ip

def start_ping(input_address, count, interval, timeout, text_output, color, size):
    # 判断输入的是IP地址还是网址
    try:
        ip_address = socket.gethostbyname(input_address)
    except socket.gaierror:
        ip_address = input_address

    delays = ping_ip(ip_address, count, interval, timeout)

    # 清空输出栏
    text_output.config(state=tk.NORMAL)
    text_output.delete(1.0, tk.END)

    for i, delay in enumerate(delays, start=1):
        if delay >= 0:
            output = f"第{i}次 Ping，延迟：{delay}ms\n"
        else:
            output = f"第{i}次 Ping，超时\n"

        # 设置字体颜色和大小
        text_output.config(state=tk.NORMAL)
        text_output.insert(tk.END, output)
        text_output.tag_configure(f"color{i}", foreground=color)
        text_output.tag_configure(f"size{i}", font=("Arial", size))
        text_output.tag_add(f"color{i}", f"{i}.0", f"{i}.end")
        text_output.tag_add(f"size{i}", f"{i}.0", f"{i}.end")
        text_output.config(state=tk.DISABLED)  # 禁用输出栏

    return delays
