import SocketServer
import netflow
import argparse
import threading
import NetflowServer

class ThreadingUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer): pass

class NetflowUDPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the UDP socket connected to the client
        self.data = self.request[0]
        print("{0} wrote:".format(self.client_address[0]))
        nf = netflow.Netflow5(self.data)

	print(nf.version)
	print(nf.data)
