import socket
hostname = socket.gethostname()
IPaddr = socket.gethostbyname(hostname)
print('My IP address is:' + IPaddr)
#Done
