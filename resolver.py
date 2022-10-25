import socket
import sys

host = sys.arg[1]

print host,"--->", socket.gethostbyname(host)