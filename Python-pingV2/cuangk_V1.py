import tkinter as tk
from ping_test_V2 import ping_ip

def start_ping():
    ip_address = entry_ip.get()
    count = int(entry_count.get())
    interval = float(entry_interval.get())
    timeout = float(entry_timeout.get())

    text_output.delete(1.0, tk.END)  # 清空输出栏

    delays = ping_ip(ip_address, count, interval, timeout)
    for i, delay in enumerate(delays, start=1):
        if delay >= 0:
            print(f"第{i}次 Ping，延迟：{delay}ms")
        else:
            print(f"第{i}次 Ping，超时")

# 创建主窗口
window = tk.Tk()
window.title("Ping测试工具")

# 创建输入栏
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_ip = tk.Label(frame_input, text="请输入IP地址：")
label_ip.pack(side=tk.LEFT)
entry_ip = tk.Entry(frame_input)
entry_ip.pack(side=tk.LEFT)

label_count = tk.Label(frame_input, text="请输入Ping次数：")
label_count.pack(side=tk.LEFT)
entry_count = tk.Entry(frame_input)
entry_count.pack(side=tk.LEFT)

label_interval = tk.Label(frame_input, text="请输入Ping间隔时间（秒）：")
label_interval.pack(side=tk.LEFT)
entry_interval = tk.Entry(frame_input)
entry_interval.pack(side=tk.LEFT)

label_timeout = tk.Label(frame_input, text="请输入超时时间（秒）：")
label_timeout.pack(side=tk.LEFT)
entry_timeout = tk.Entry(frame_input)
entry_timeout.pack(side=tk.LEFT)

# 创建按钮
button_start = tk.Button(window, text="开始Ping", command=start_ping)
button_start.pack(pady=10)

# 创建输出栏
text_output = tk.Text(window, width=40, height=10)
text_output.pack()

# 运行主循环
window.mainloop()
