import http.server, mimetypes, socketserver, webbrowser, os, threading

mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("text/html; charset=utf-8", ".html")

PORT = 8777
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()
    def log_message(self, *a):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), H) as httpd:
    url = f"http://127.0.0.1:{PORT}/"
    print("გახსენი:", url, "  (დახურვა: Ctrl+C)")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    httpd.serve_forever()
