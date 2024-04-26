# copyleft dobrostvari, 2024

import ping
import socket
import random as rand

def rand_string(length):
    i = length

    while i != 0:
        out += '\u' + hex(rand.randint(0, 65535))
        i -= 1

def crawl():
    while true:
        try:
            ping.verbose_ping(rand_string(rand.randint(0, 63)))