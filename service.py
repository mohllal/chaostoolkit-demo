"""
This is a simple WSGI application that serves the content of a file.
It writes the current date and time into a file every second and serves that file over HTTP.
"""
from datetime import datetime
import io
import time
import threading
from wsgiref.simple_server import make_server
from logging import getLogger

LOGGER = getLogger(__name__)
EXAMPLE_FILE = "./example.dat"


def update_example_file():
    """
    Writes the current date and time every 1 seconds into the example file.
    The file is created if it does not exist.
    """
    LOGGER.info("Will update to example file")
    while True:
        with io.open(EXAMPLE_FILE, "w", encoding="utf-8") as f:
            f.write(datetime.now().isoformat())
        time.sleep(1)


# The WSGI application
def simple_app(_, start_response):
    """
    Read the content of the example file and return it.
    """
    start_response("200 OK", [("Content-type", "text/plain")])
    with io.open(EXAMPLE_FILE, encoding="utf-8") as f:
        return [f.read().encode("utf-8")]


if __name__ == "__main__":
    t = threading.Thread(target=update_example_file)
    t.start()

    httpd = make_server("0.0.0.0", 8080, simple_app)
    LOGGER.info("Listening to 0.0.0.0:8080...")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        t.join(timeout=1)
