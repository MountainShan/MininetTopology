from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.node import RemoteController, OVSSwitch

def main():
	OFSwitchList = []
	HostList = []
	net = Mininet(controller = None, link = TCLink)

	for i in range(4):
		OFSwitchList.append(net.addSwitch("s%s"%str(i+1), cls = OVSSwitch))

	for i in range(4):
		HostList.append(net.addHost("h%s"%str(i+1), ip = "10.0.0.%s/24"%str(i+1), mac = "00:04:00:00:00:%s"%str(i+1)))

	net.addLink(HostList[0], OFSwitchList[0],port1=1,port2=4)
	net.addLink(HostList[1], OFSwitchList[1],port1=1,port2=4)
        net.addLink(HostList[2], OFSwitchList[2],port1=1,port2=4)
        net.addLink(HostList[3], OFSwitchList[3],port1=1,port2=4)

        net.addLink(OFSwitchList[0],OFSwitchList[1],port1=1,port2=1)
        net.addLink(OFSwitchList[0],OFSwitchList[3],port1=2,port2=2)
        net.addLink(OFSwitchList[0],OFSwitchList[2],port1=3,port2=3)
        net.addLink(OFSwitchList[1],OFSwitchList[2],port1=2,port2=2)
        net.addLink(OFSwitchList[1],OFSwitchList[3],port1=3,port2=3)
        net.addLink(OFSwitchList[2],OFSwitchList[3],port1=1,port2=1)

	net.start()
	CLI(net)
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
