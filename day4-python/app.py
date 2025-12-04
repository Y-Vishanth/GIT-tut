#!/bin/bash
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv("APP_PORT", 5000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Python Backend App")

if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Starting server on port {PORT}")
    server.serve_forever()

