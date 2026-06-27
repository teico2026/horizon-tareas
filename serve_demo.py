import os, http.server, socketserver
PORT = int(os.environ.get("PORT", "3009"))
DIR = os.path.dirname(os.path.abspath(__file__))
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=DIR, **k)
    def do_GET(self):
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/index.html?demo=1")
            self.end_headers()
            return
        return super().do_GET()
with socketserver.TCPServer(("127.0.0.1", PORT), H) as httpd:
    httpd.serve_forever()
