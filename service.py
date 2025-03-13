"""
This is a simple WSGI application that serves the content of a file.
It writes the current date and time into a file every second and serves that file over HTTP.
"""
from datetime import datetime
import io
import os.path
import time
import threading
from wsgiref.simple_server import make_server


EXAMPLE_FILE = "./example.dat"


def update_example_file():
    """
    Writes the current date and time every 1 seconds into the example file.
    The file is created if it does not exist.
    """
    print("Will update to example file")
    while True:
        with io.open(EXAMPLE_FILE, "w", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())
        time.sleep(1)


# The WSGI application
def simple_app(environ, start_response):
    """
    Read the content of the example file and return it.
    """
    if not os.path.exists(EXAMPLE_FILE):
        start_response("404 Not Found", [("Content-type", "text/plain")])
        return [b"File not found"]

    start_response("200 OK", [("Content-type", "text/plain")])
    with io.open(EXAMPLE_FILE, encoding="utf-8") as f:
        return [f.read().encode("utf-8")]


if __name__ == "__main__":
    t = threading.Thread(target=update_example_file, daemon=True)
    t.start()

    httpd = make_server("0.0.0.0", 8080, simple_app)
    print("Listening on all interfaces on port 8080...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Server shutdown complete")
