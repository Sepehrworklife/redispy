import socket


"""NOTICE
The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the socket() function returns a socket object whose methods implement the various socket system calls. Parameter types are somewhat higher-level than in the C interface: as with read() and write() operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.
"""

""" Some Definations
AF_INET: IPv4 Internet protocols
SOCK_STREAM: Provides sequenced, reliable, two-way, connection-based
            byte streams.  An out-of-band data transmission mechanism
            may be supported.
SO_SOCKET: Use this constant as the level argument to getsockopt or setsockopt to manipulate the socket-level options.
SO_REUSEADDR: This option controls whether bind should permit reuse of local
            addresses for this socket. If you enable this option, you can actually have two sockets with the same Internet port number; but the system won’t allow you to use the two identically-named sockets in a way that would confuse the Internet. The reason for this option is that some higher-level Internet protocols, including FTP, require you to keep reusing the same port number.
SOMAXCONN: The maximum backlog queue length.
"""


def do_something(conn):
    print(f"Cleint says: {conn.recv()} \n")
    conn.send("World")

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(socket.SOMAXCONN)
        conn, addr = sock.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv()
                if not data: break
                do_something(conn)
                sock.close()
                



