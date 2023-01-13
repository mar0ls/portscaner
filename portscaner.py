from socket import *
import optparse
from threading import *

def connscan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print ('[+] %d/tcp Open' % tgtPort)
    except:
        print ('[-] %d/tcp Closed' % tgtPort)
    finally:
        sock.close()

def portscan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print ('Unknown host %s' % tgtHost)

    try:
        tgtName = gethostbyaddr(tgtIP)
        print ('[+] Scan results for: ' + tgtName[0])
    except:
        print ('[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connscan, args=(tgtHost, int(tgtPort)))
        t.start()

        
def parse_port_spec(spec):
    if "," in spec:
        # Port list
        ports = spec.split(',')
    elif '-' in spec:
        # Port range
        start, end = map(int, spec.split('-'))
        ports = range(start, end + 1)
    else:
        # Single port
        ports = [spec]
    return map(int, ports)

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-t <target host> -p <targert port>' + 'ex. portscaner.py -t 192.168.1.1 -p 1-100' )
    parser.add_option('-t', dest='tgtHost', type='string', help='specify target host name or IP')
    parser.add_option('-p', dest='tgtPort', default='1-65535' ,type='string', help='specify terget ports separated by a comma "," or a dash "-". Default scan all ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = parse_port_spec(str(options.tgtPort))
#   tgtPorts = str(options.tgtPort).split(',')
    if not options.tgtHost or not options.tgtPort:
        print(parser.usage)
        exit(0)
    portscan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()