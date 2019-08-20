#!/usr/bin/python3
# -*- coding: utf-8 -*-


import http.server


class Server:
    def __init__(self):
        pass


if __name__ == '__main__':
    PORT = 8888
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()
