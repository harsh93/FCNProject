import SimpleHTTPServer
import SocketServer
import socket

TCP_FASTOPEN = 23

class FastOpenServer(SocketServer.TCPServer):
  def server_bind(self):
    SocketServer.TCPServer.server_bind(self)
    self.socket.setsockopt(socket.SOL_TCP, TCP_FASTOPEN, 5)

class CS534Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def address_string(self):
        return str(self.client_address[0])


PORT = 80

Handler = CS534Handler
httpd = FastOpenServer(("", PORT), Handler)
print "Server1: httpd serving at port", PORT
httpd.serve_forever()
