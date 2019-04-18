import http
from http import server

resp = """HTTP/1.1 200 OK
Server: BaseHTTP/0.3 Python/2.7.15+
Date: Tue, 16 Apr 2019 16:55:57 GMT
Connection: close
Content-Type: text/html

<p>You have reached the Underworld.</p>
"""

class RequestHandler(server.BaseHTTPRequestHandler):
    allow_reuse_address = True
    print('Server is up!')
    def handle_one_request(self):
        # respond with prepared message
        self.request.send(bytes(resp, 'utf-8'))

class CustomServer(server.HTTPServer):
    pass

server = CustomServer(('localhost', 3301), RequestHandler)
server.serve_forever()