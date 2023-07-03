import os
import platform
import nmap
import psutil
import socket
import re
import uuid


def get_mac_address():
    # 获取本机MAC地址
    mac = ''
    # 正则匹配MAC地址
    try:
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    except Exception as e:
        print(str(e))
    return mac


def get_ip_address():
    # 获取本机IP地址
    ip = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        print(str(e))
    finally:
        s.close()
    return ip


# 创建nmap扫描器对象
nm = nmap.PortScanner()

# 扫描端口信息
nm.scan('192.168.219.129', '1-65535')

# 输出端口状态信息
with open('scan.txt', 'w') as f:
    f.write('Host: {0}\n'.format(nm['192.168.219.129'].hostname()))
    for port in nm['192.168.219.129']['tcp']:
        f.write(f'Port: {port}\tState: {nm["192.168.219.129"]["tcp"][port]["state"]}\n')

# 获取操作系统信息
os_name = platform.system() + ' ' + platform.release()

# 获取网络信息
ip_address = get_ip_address()
mac_address = get_mac_address()

# 获取USB接口信息
nm.scan('127.0.0.1', arguments='-sS -sU -vv -n --open -p U:137,T:139')
usb_ports = []
for host in nm.all_hosts():
    if 'udp' in nm[host]:
        for port in nm[host]['udp']:
            service = nm[host]['udp'][port]['name']
            usb_ports.append({'Host': host, 'Port': port, 'Service': service})
    if 'tcp' in nm[host]:
        for port in nm[host]['tcp']:
            if 'name' in nm[host]['tcp'][port]:
                service = nm[host]['tcp'][port]['name']
                usb_ports.append({'Host': host, 'Port': port, 'Service': service})

# 将结果输出到文件
with open('scan.txt', 'a') as f:
    f.write(f'\nOperating System: {os_name}\n')
    f.write(f'IP Address: {ip_address}\n')
    f.write(f'MAC Address: {mac_address}\n\n')
    f.write('USB Ports:\n')
    for p in usb_ports:
        f.write(f"Host: {p['Host']}\tPort: {p['Port']}\tService: {p['Service']}\n")