
import sockets
import sys


if __name__ == '__main__':  
    if len(sys.argv) < 2:
        sys.argv.append(str(8080))  
    if len(sys.argv) < 3:
        sys.argv.append(str(20))  
    if len(sys.argv) < 4:
        sys.argv.append(str(3))  
    print('startserver')
    sockets.server_start(sys.argv)
else:
    def start(port, maxmoves, timeout):
        sockets.server_start((-1, port, maxmoves, timeout))
