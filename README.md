<div id="header" align="center">
  <img src="https://media2.giphy.com/media/JGUMPPTMRCVPbSncVF/giphy.webp?cid=6c09b9522e214fc409ce67211bae3730c1b65ee298cc4c77&rid=giphy.webp&ct=g" width="100"/>
</div>

# **Portscaner**
    Usage of program: -t <target host> -p <targert port> + ex. portscaner.py -t 192.168.1.1 -p 1-100
      -t, specify target host name or IP
      -p, specify terget ports separated by a comma "," or a dash "-". Default scan all ports.

# What does portscaner mean?
Port scanning is a method of determining which ports on a network are open and could be receiving or sending data. It is also a process for sending packets to specific ports on a host and analyzing responses to identify vulnerabilities.
This scanning can’t take place without first identifying a list of active hosts and mapping those hosts to their IP addresses. This activity, called host discovery, starts by doing a network scan.
The goal behind port and network scanning is to identify the organization of IP addresses, hosts, and ports to properly determine open or vulnerable server locations and diagnose security levels. Both network and port scanning can reveal the presence of security measures in place such as a firewall between the server and the user’s device.
After a thorough network scan is complete and a list of active hosts is compiled, port scanning can take place to identify open ports on a network that may enable unauthorized access.

It’s important to note that network and port scanning can be used by both IT administrators and cybercriminals to verify or check the security policies of a network and identify vulnerabilities — and in the attackers’ case, to exploit any potential weak entry points. In fact, the host discovery element in network scanning is often the first step used by attackers before they execute an attack.
As both scans continue to be used as key tools for attackers, the results of network and port scanning can provide important indications of network security levels for IT administrators trying to keep networks safe from attacks.

# Ports in networting
A network port is a process-specific or an application-specific software construct serving as a communication endpoint, which is used by the Transport Layer protocols of Internet Protocol suite, such as User Diagram Protocol (UDP) and Transmission Control Protocol (TCP).
A specific network port is identified by its number commonly referred to as port number, the IP address in which the port is associated with and the type of transport protocol used for the communication.
A port number is a 16-bit unsigned integer that ranges from 0 to 65535.

**LIST OF WELL-KNOWN PORTS**
Port numbers range from 0 to 65535, but only port numbers 0 to 1023 are reserved for privileged services and designated as well-known ports. The following list of well-known 
port numbers specifies the port used by the server process as its contact port.

**Port Number	Description**
*	1	TCP Port Service Multiplexer (TCPMUX)
*	5	Remote Job Entry (RJE)
*	7	ECHO
*	18	Message Send Protocol (MSP)
*	20	FTP — Data
*	21	FTP — Control
*	22	SSH Remote Login Protocol
*	23	Telnet
*	25	Simple Mail Transfer Protocol (SMTP)
*	29	MSG ICP
*	37	Time
*	42	Host Name Server (Nameserv)
*	43	WhoIs
*	49	Login Host Protocol (Login)
*	53	Domain Name System (DNS)
*	69	Trivial File Transfer Protocol (TFTP)
*	70	Gopher Services
*	79	Finger
*	80	HTTP
*	103	X.400 Standard
*	108	SNA Gateway Access Server
*	109	POP2
*	110	POP3
*	115	Simple File Transfer Protocol (SFTP)
*	118	SQL Services
*	119	Newsgroup (NNTP)
*	137	NetBIOS Name Service
*	139	NetBIOS Datagram Service
*	143	Interim Mail Access Protocol (IMAP)
*	150	NetBIOS Session Service
*	156	SQL Server
*	161	SNMP
*	179	Border Gateway Protocol (BGP)
*	190	Gateway Access Control Protocol (GACP)
*	194	Internet Relay Chat (IRC)
*	197	Directory Location Service (DLS)
*	389	Lightweight Directory Access Protocol (LDAP)
*	396	Novell Netware over IP
*	443	HTTPS
*	444	Simple Network Paging Protocol (SNPP)
*	445	Microsoft-DS
*	458	Apple QuickTime
*	546	DHCP Client
*	547	DHCP Server
*	563	SNEWS
*	569	MSN
*	1080	Socks

•	Well-known ports range from 0 through 1023.
•	Registered ports are 1024 to 49151.
•	Dynamic ports (also called private ports) are 49152 to 65535.

# What's work?
The simplest port scanners use the operating system's network functions and are generally the next option to go to when SYN is not a feasible option . This mode connect scan, named after the Unix connect() system call. If a port is open, the operating system completes the TCP three-way handshake, and the port scanner immediately closes the connection to avoid performing a Denial-of-service attack. Otherwise an error code is returned. This scan mode has the advantage that the user does not require special privileges. However, using the OS network functions prevents low-level control, so this scan type is less common. This method is "noisy", particularly if it is a "portsweep": the services can log the sender IP address and Intrusion detection systems can raise an alarm.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# HAVE FUN ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)    (/◕ヮ◕)/(/◕ヮ◕)/(/◕ヮ◕)/
