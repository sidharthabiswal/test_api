import json
import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer, op_type, *args):
        super().__init__(request, client_address, server)
        
    @property
    def api_response(self):
        if self.op_type == 'add':
            output = self.args[0] + self.args[1]
        elif self.op_type == 'subtract':
            output = self.args[0] - self.args[1]
        elif self.op_type == 'multiple':
            output = self.args[0] * self.args[1]
        return json.dumps({"output": output}).encode()

    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(self.api_response))

if __name__ == "__main__":
    PORT = 8000
    # Create an object of the above class
    my_server = socketserver.TCPServer(("0.0.0.0", PORT), Handler, op_type, args)
    # Star the server
    print(f"Server started at {PORT}")
    my_server.serve_forever()   
