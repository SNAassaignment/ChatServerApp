import PortScanner
import argparse

gethost = '192.168.31.226'
getport = PortScanner.GetOpenPorts(gethost)
getserv = PortScanner.GetService(getport[0])
ports = list(getport)

banner = PortScanner.BannerGrabber(gethost,ports,getserv)
banner.Grab()


#make argument commands like help
