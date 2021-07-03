import json
import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus
from functools import reduce


class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer, op_type, *args):
        super().__init__(request, client_address, server)              

    def add(*args):
        output = reduce(lambda x,y: x+y, args)
        return output

    def subtract(*args):
        output = reduce(lambda x,y: x-y, args)
        return output

    def multiply(*args):
        output = reduce(lambda x,y: x*y, args)
        return output

    def divide(*args):
        output = reduce(lambda x,y: x/y, args)
        return output

        
    @property
    def api_response(self):
        output = self.op_type(self.args)
        return json.dumps({"output": output})

    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.api_response

if __name__ == "__main__":
    PORT = 8000
    # Create an object of the above class
    my_server = socketserver.TCPServer(("0.0.0.0", PORT), Handler, op_type, args)
    # Star the server
    print(f"Server started at {PORT}")
    my_server.serve_forever()   
