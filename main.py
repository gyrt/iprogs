import SocketServer
import netflow

class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request[0]
        print("{0} wrote:".format(self.client_address[0]))
        nf = netflow.Netflow5(self.data)

	print(nf.version)
	print(nf.data)

        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9996

    # Create the server, binding to localhost on port 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
