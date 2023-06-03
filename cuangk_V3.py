import tkinter as tk
from tkinter import ttk
from start_ping import start_ping
from clear_output import clear_output

# 创建主窗口
window = tk.Tk()
window.title("Ping测试工具@叮当在上")

# 创建输入栏
frame_input1 = tk.Frame(window)
frame_input1.pack(pady=10)

label_address = tk.Label(frame_input1, text="请输入IP地址或网址：")
label_address.pack(side="left")

entry_address = tk.Entry(frame_input1)
entry_address.pack(side="left", padx=10)

label_count = tk.Label(frame_input1, text="请输入Ping次数：")
label_count.pack(side="left", padx=10)

entry_count = tk.Entry(frame_input1)
entry_count.pack(side="left")

frame_input2 = tk.Frame(window)
frame_input2.pack(pady=10)

label_interval = tk.Label(frame_input2, text="请输入Ping间隔时间（秒）：")
label_interval.pack(side="left")

entry_interval = tk.Entry(frame_input2)
entry_interval.pack(side="left", padx=10)

label_timeout = tk.Label(frame_input2, text="请输入超时时间（秒）：")
label_timeout.pack(side="left", padx=10)

entry_timeout = tk.Entry(frame_input2)
entry_timeout.pack(side="left")

frame_input3 = tk.Frame(window)
frame_input3.pack(pady=10)

label_color = tk.Label(frame_input3, text="选择字体颜色：")
label_color.pack(side="left")

combo_color = ttk.Combobox(frame_input3, values=["green", "black", "red", "orange", "purple", "pink"])
combo_color.current(0)
combo_color.pack(side="left", padx=10)

label_size = tk.Label(frame_input3, text="选择字体大小：")
label_size.pack(side="left", padx=10)

combo_size = ttk.Combobox(frame_input3, values=["10", "12", "14", "16", "18"])
combo_size.current(0)
combo_size.pack(side="left")

# 创建按钮区域
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# 创建开始Ping测试按钮
def ping_button_click():
    input_address = entry_address.get()
    count = int(entry_count.get())
    interval = float(entry_interval.get())
    timeout = float(entry_timeout.get())
    color = combo_color.get()
    size = combo_size.get()
    start_ping(input_address, count, interval, timeout, text_output, color, size)

button_ping = tk.Button(frame_buttons, text="开始Ping测试", command=ping_button_click)
button_ping.pack(side="left", padx=5)

# 创建清屏按钮
button_clear = tk.Button(frame_buttons, text="清屏", command=lambda: clear_output(text_output))
button_clear.pack(side="left", padx=5)

# 创建输出栏和滚动条
frame_output = tk.Frame(window)
frame_output.pack(pady=10)

label_output = tk.Label(frame_output, text="输出信息：")
label_output.pack(anchor="w")

text_output = tk.Text(frame_output, height=15, width=60)
text_output.pack(side="left", padx=10, pady=10)
text_output.config(state=tk.DISABLED)  # 初始化为禁用状态，不可编辑

scrollbar = tk.Scrollbar(frame_output)
scrollbar.pack(side="right", fill="y")

text_output.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=text_output.yview)

# 运行主循环
window.mainloop()
