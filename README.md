# portScanner

In order to interact with TCP ports, we will need to first construct TCP sockets.

Python provides access to the BSD socket interface. BSD sockets provide an application-programming interface that allows
coders to write applications in order to perform network communications
between hosts. 

The majority of Internet accessible applications reside on the TCP. For example,
in a target organization, the web server might reside on TCP port 80, the email
server on TCP port 25, and the file transfer server on TCP port 21

To connect to any of these services in our target organization, an attacker must know both the
Internet Protocol Address and the TCP port associated with the service.

We will input a hostname and a comma separated list of ports
to scan. Next, we will translate the hostname into an IPv4 Internet address.
For each port in the list, we will also connect to the target address and specific port. Finally, to determine the specific service running on the port, we
will send garbage data and read the banner results sent back by the specific
application.

Optparse liblary helps parse command-line  options

The PortScan() function takes the hostname and target ports as arguments. It will first attempt to resolve an IP address 
to a friendly hostname using the gethostbyname() function. Next, it will print the hostname (or IP address) and enumerate
through each individual port attempting to connect using the connScan function. 

The connScan() function will take two arguments: tgtHost and tgtPort and attempt
to create a connection to the target host and port. If it is successful, connScan()
will print an open port message. If unsuccessful, it will print the closed port
message.

After discovering an open port, we send a string of data to the port and wait for the response. Gathering
this response might give us an indication of the application running on the
target host and port which will prove to be useful for targeting the application

Threading provides a way to scan sockets(multiple hosts and ports) simultaneously
as opposed to sequentially. To do this, we modify the iteration loop in our portScan() function 
then call the connScan() function as a thread. 
Each thread created in the iteration will now appear to execute at the same time.

Our function connScan() prints an output to the screen.
If multiple threads print an output at the same time, it could appear garbled
and out of order. In order to allow a function to have complete control of the
screen, we will use a semaphore which provides us a lock to prevent other threads from proceeding. 

Prior to printing an output, we grab a hold of the lock using screenLock.acquire(). If open, the semaphore
will grant us access to proceed and we will print to the screen. 

If locked, we will have to wait until the thread holding the semaphore releases the lock. 
By utilizing this semaphore, we now ensure only one thread can print to the screen at
any given point in time.
