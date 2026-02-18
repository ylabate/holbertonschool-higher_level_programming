#!/usr/bin/python3
import http.server
import json


class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found\n")


server = http.server.HTTPServer(('localhost', 8000), Server)
server.serve_forever()
