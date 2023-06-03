import ping3
import time

def ping_ip(ip_address, count=1, interval=1, timeout=1):
    delays = []
    for _ in range(count):
        delay = ping3.ping(ip_address, timeout=timeout)
        if delay is not None:
            delays.append(delay * 1000)
        else:
            delays.append(-1)
        time.sleep(interval)
    return delays

while True:
    try:
        ip_address = input("请输入IP地址（输入'exit'退出）：")
        if ip_address == "exit":
            break

        count = int(input("请输入Ping次数："))
        interval = float(input("请输入Ping间隔时间（秒）："))
        timeout = float(input("请输入超时时间（秒）："))

        delays = ping_ip(ip_address, count, interval, timeout)
        for i, delay in enumerate(delays, start=1):
            if delay >= 0:
                print(f"第{i}次 Ping，延迟：{delay}ms")
            else:
                print(f"第{i}次 Ping，超时")

    except ValueError:
        print("输入错误，请重新开始程序。")
        continue
