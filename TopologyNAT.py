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

	for i in xrange(1):
		OFSwitchList.append(net.addSwitch("s%s"%str(i+1), cls = OVSSwitch))

	HostList.append(net.addHost("h1", ip = "10.0.0.1/24", mac = "00:04:00:00:00:01"))
        HostList.append(net.addHost("h2", ip = "10.1.0.2/24", mac = "00:04:00:00:00:02"))

	net.addLink(HostList[0], OFSwitchList[0])
	net.addLink(HostList[1], OFSwitchList[0])

	net.start()
        HostList[0].cmd("ip route add default via 10.0.0.1")
        HostList[1].cmd("ip route add default via 10.1.0.2")
	CLI(net)
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
