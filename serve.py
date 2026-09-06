#!/usr/bin/env python3
"""Static dev server for ParcelPath that defeats browser caching.

python -m http.server sends only Last-Modified and no Cache-Control, so browsers
apply *heuristic* freshness (roughly 10% of the file's age) and will reuse
styles.css / chrome.js for hours without ever revalidating. That makes edits
look like they "didn't take". This server sends no-store on every response.

    python3 serve.py [port]      # default 8000
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_header(self, keyword, value):
        # Drop the upstream validator so conditional requests can't yield a 304.
        if keyword.lower() == "last-modified":
            return
        super().send_header(keyword, value)

    def send_head(self):
        # SimpleHTTPRequestHandler answers 304 from the file mtime inside
        # send_head(), before any of our response headers are written. Discard
        # the conditional request headers so every request gets a full 200.
        for h in ("If-Modified-Since", "If-None-Match"):
            del self.headers[h]
        return super().send_head()


if __name__ == "__main__":
    import os
    port = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    print(f"ParcelPath dev server (no-cache) -> http://{host}:{port}/")
    try:
        ThreadingHTTPServer((host, port), NoCacheHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
