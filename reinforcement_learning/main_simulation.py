#! /usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

import numpy as np


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        self.wfile.write(b"<body><p>This is a test.</p>")
        self.wfile.write(f"<p>You accessed path: {self.path}</p>".encode("ascii"))
        self.wfile.write(
            f"<p>Here is a random number: {np.random.randint(0, 10)}</p>".encode(
                "ascii"
            )
        )
        self.wfile.write(b"</body></html>")


httpd = HTTPServer(("localhost", 8000), MyHandler)
httpd.serve_forever()
