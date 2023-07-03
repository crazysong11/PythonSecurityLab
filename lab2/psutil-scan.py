import psutil

# 获取CPU信息
cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
cpu_str = "CPU信息：\n" \
          "User Time: {}\n" \
          "System Time: {}\n" \
          "Wait IO: {}\n" \
          "Idle: {}\n".format(cpu_times_percent.user, cpu_times_percent.system, 
                              cpu_times_percent.iowait, cpu_times_percent.idle)

# 获取内存信息
vm = psutil.virtual_memory()
mem_str = "内存信息：\n" \
          "Total: {} MB\n" \
          "Used: {} MB\n" \
          "Free: {} MB\n" \
          "Buffers: {} MB\n" \
          "Cache: {} MB\n" \
          "Swap: {} MB\n".format(round(float(vm.total) / 1024 / 1024), round(float(vm.used) / 1024 / 1024), 
                                 round(float(vm.free) / 1024 / 1024), round(float(vm.buffers) / 1024 / 1024), 
                                 round(float(vm.cached) / 1024 / 1024), round(float(psutil.swap_memory().used) / 1024 / 1024))

# 获取磁盘信息
io_counters = psutil.disk_io_counters(perdisk=True)
disk_str = "磁盘信息：\n"
for disk_name in io_counters:
    disk_count = io_counters[disk_name]
    disk_str += "{}:\n" \
                "Read Count: {}\n" \
                "Write Count: {}\n" \
                "Read Bytes: {} MB\n" \
                "Write Bytes: {} MB\n" \
                "Read Time: {} 秒\n" \
                "Write Time: {} 秒\n".format(disk_name, disk_count.read_count, 
                                             disk_count.write_count, round(float(disk_count.read_bytes) / 1024 / 1024), 
                                             round(float(disk_count.write_bytes) / 1024 / 1024), disk_count.read_time, 
                                             disk_count.write_time)

# 获取网络信息
net_io_counters = psutil.net_io_counters()
net_str = "网络信息：\n" \
          "Bytes Sent: {} MB\n" \
          "Bytes Recv: {} MB\n" \
          "Packets Sent: {}\n" \
          "Packets Recv: {}\n".format(round(float(net_io_counters.bytes_sent) / 1024 / 1024), 
                                      round(float(net_io_counters.bytes_recv) / 1024 / 1024), 
                                      net_io_counters.packets_sent, net_io_counters.packets_recv)

# 写入结果到.txt文件中
with open('result.txt', 'w') as f:
    f.write(cpu_str + '\n')
    f.write(mem_str + '\n')
    f.write(disk_str + '\n')
    f.write(net_str + '\n')
