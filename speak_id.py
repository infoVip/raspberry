#!/usr/bin/env python3
# coding=utf-8

import time
import socket
import subprocess


def getLocalIP():
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 0))
        ip = s.getsockname()[0]
    except:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
    if ip.startswith("127."):
        cmd = '''/sbin/ifconfig | grep "inet " | cut -d: -f2 | awk '{print $1}' | grep -v "^127."'''
        a = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        a.wait()
        out = a.communicate()
        ip = out[0].strip().split("\n")  # 所有的列表
        if len(ip) == 1 and ip[0] == "" or len(ip) == 0:
            return False
        ip = "&".join(ip)
    return ip


def play(voice):
	cmd = "espeak -s 150 '%s'" % (voice,)
	a = subprocess.Popen(
		cmd,
		shell=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
	a.wait()



if __name__ == '__main__':
    count = 5
    while count > 0:
        ip = getLocalIP()
        if ip == False:
            play("ing")
        else:
            count -= 1
            play(ip)
        time.sleep(1)
