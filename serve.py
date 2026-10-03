"""Preview the birthday cake locally: run `python serve.py`, then the browser opens."""
import http.server
import socketserver
import webbrowser
from functools import partial
from pathlib import Path

PORT = 8000
handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(Path(__file__).parent))

with socketserver.TCPServer(("", PORT), handler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"Serving at {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    httpd.serve_forever()
