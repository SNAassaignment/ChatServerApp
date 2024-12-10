import socket,os

PORT_SERVICES = {
    22: "ssh",
    80: "http",
    631: "ipp",
    992: "telnets",
    3306: "mysql",
    9050: "tor-socks"
    # Add more service mappings as needed
}

def GetOpenPorts(host):
    packed_ports = []
    for o_ports in range(0,65535+1):
        scan_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        open_ports = scan_sock.connect_ex((host,o_ports))

        if open_ports == 0:
            packed_ports.append(o_ports)

    return packed_ports
    scan_sock.close()

def GetService(port) -> int:
    return PORT_SERVICES.get(port,'Unknown')

class BannerGrabber:
    def __init__(self,host,portObj:list,ServiceObj):
        self.host = host
        self.port = portObj
        self.service = ServiceObj
        self.protocol = 'tcp'

    def Grab(self):
        os.system('clear')
        print("Scan the ip : {}...\n".format(self.host))
        print("PORT\t\tSERVICE\t\tPROTOCOL\n")
        for ports in self.port:
            print(f"{ports}\t\t{GetService(ports)}\t\t{self.protocol}\n")
