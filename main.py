import SocketServer
import netflow
import argparse
import threading
import NetflowServer

if __name__ == "__main__":
	HOST, PORT = "localhost", 9996
	ACTION = "/bin/true"
	LIMIT = 4294967296

	parser = argparse.ArgumentParser("sphx-server")
	parser.add_argument("-d", "--debug", help="Start in debug mode", action="store_true", default=False)
	parser.add_argument("-i", "--ip", help="IP to listen (default: {0})".format(HOST), type=str, default=HOST)
	parser.add_argument("-p", "--port", help="PORT to listen (default: {0})".format(PORT), type=int, default=PORT)
	parser.add_argument("-a", "--action", help="Action for host reached the limit (default: {0})".format(ACTION), type=str, default=ACTION)
	parser.add_argument("-l", "--limit", help="Packates limit (default: {0})".format(LIMIT), type=int, default=LIMIT)
	args = parser.parse_args()

	

	# Create the server, binding to localhost on port 9999
	server = NetflowServer.ThreadingUDPServer((HOST, PORT), NetflowServer.NetflowUDPHandler)

	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()
