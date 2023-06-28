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
