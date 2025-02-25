###############################################################################################
#                                      Simple Port Scanner                                     #
#                    Most of Internet accessible applications reside on the TCP.               #
#     * Web server [TCP Port 80] Email Server [TCP Port 25] File Transfer Server [TCP Port 21] #
################################################################################################

import optparse
from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send("Macavelli\r\n")
		results = connSkt.recv(100)
		screenLock.acquire()

		print ("[+] %d/tcp open" % tgtPort)
		print ("[+]" + str(results))

	except:
		screenLock.acquire()
		print ("[-] %d/tcp closed" % tgtPort)
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print ("[-] Cannot resolve '%s': Unknown host" %tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print ("\n[+] Scanned Results for: " + tgtName[0])
	except:
		print ("\n[+] Scanned Results for: " + tgtIP)
	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser("Usage%prog "+\
		"-H <Target Host> -p <Target Port> \n eg:- python scan.py -H 192.168.5.1 -p  80,21,445,25,1720")
	
	parser.add_option("-H", dest = "tgtHost", type = "string", \
		help = "Specify Yor Target Host")

	parser.add_option("-p", dest = "tgtPort", type = "string", \
		help = "Specify target port[s] separated by a comma.")

	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(",")

	if (tgtHost == None) | (tgtPorts[0] == None):
		print (parser.usage)
		exit(0)

	portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
	main()
