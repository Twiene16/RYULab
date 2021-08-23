from mininet.topo import Topo
from mininet .net import Mininet , Host
from mininet .log import setLogLevel
from mininet.cli import CLI
from mininet . node import OVSSwitch , Controller , RemoteController
from mininet.link import TCLink
from time import sleep
from mininet.node import CPULimitedHost

#topos = {'custom':(lambda:SingleSwitchTopo ())}

class mytopo1( Topo ):

    def build( self ):

        # Add hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        #snort = self.addHost('snort', mac="00:00:00:00:10:00")

        # Add links
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s1)
        self.addLink(h4,s2)
        self.addLink(h5,s2)
        self.addLink(h6,s2)
        self.addLink(s1,s3)
        self.addLink(s2,s3)
        #self.addLink(snort,s3)
     
        
def runmytopo():
    topo = mytopo1() 
    net = Mininet ( topo =topo , host = CPULimitedHost , controller =lambda name: RemoteController(name, ip='192.168.16.4'))
    net. start ()
    CLI(net)
    net. stop ()
    
        
if  __name__ == "__main__":
 setLogLevel ('info')
 runmytopo()
 ##topo = mytopo () 
 
topos = { 
    'custom' : mytopo1
    }
