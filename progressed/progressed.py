# -- encoding: UTF-8 --

import re
import sys

SVG_TEMPLATE = u"""
<svg height="18" width="90" xmlns="http://www.w3.org/2000/svg">
  <linearGradient id="a" x2="0" y2="100%%">
    <stop offset="0" stop-color="#fff" stop-opacity=".7"/>
    <stop offset=".1" stop-color="#aaa" stop-opacity=".1"/>
    <stop offset=".9" stop-opacity=".3"/>
    <stop offset="1" stop-opacity=".5"/>
  </linearGradient>
  <rect fill="#555" height="18" rx="4" width="90"/>
  <rect fill="%(color)s" height="18" rx="4" width="%(width)d" x="0"/>
  <rect fill="url(#a)" height="18" rx="4" width="90"/>
  <g fill="#fff" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11" text-anchor="middle">
    <text fill="#010101" fill-opacity=".3" x="45" y="13">%(progress)d%%</text>
    <text x="45" y="12">%(progress)d%%</text>
  </g>
</svg>
""".strip()


def get_svg(progress):
    """
    Render SVG XML of the given progress indicator (0..100).
    """
    width = 90.0 * progress / 100.0
    if progress < 30:
        color = "#d9534f"
    elif progress < 70:
        color = "#f0ad4e"
    else:
        color = "#5cb85c"

    return SVG_TEMPLATE % {
        "width": width,
        "color": color,
        "progress": progress
    }


def simple_response(start_response, content, status_line="200 OK",
                    content_type="text/html; charset=utf-8"):
    """
    Start and return a simple WSGI response.
    :param start_response: The WSGI `start_response` callable.
    :param content: The actual text content. Will be encoded into UTF-8.
    :param status_line: The status line to be passed.
    :param content_type: The content type header. Defaults to UTF-8 HTML.
    :return: An iterable of content ready to be returned to the WSGI server.
    """
    if (sys.version_info > (3, 0)):
        content = str(content).encode("UTF-8")
    else:
        content = unicode(content).encode("UTF-8")
    start_response(status_line, [
        ("Content-Length", str(len(content))),
        ("Content-Type", content_type)
    ])
    return [content]


BAR_PATH_RE = re.compile("^/bar/(\d+)$")


def application(environ, start_response):
    path = environ.get("PATH_INFO", "")
    match = BAR_PATH_RE.match(path)
    if match:
        progress = int(match.group(1))
        if not 0 <= progress <= 100:
            return simple_response(
                start_response,
                "progress must be [0-100]",
                status_line="400 Bad Request"
            )
        return simple_response(
            start_response,
            get_svg(progress),
            content_type="image/svg+xml"
        )
    elif path == "/ping":
        return simple_response(start_response, u"pong")
    else:
        return simple_response(
            start_response, u"Not found.", status_line="404 Not Found")


def standalone():
    print("Serving progress bars on port 8080.")
    from wsgiref.simple_server import make_server
    make_server('', 8080, application).serve_forever()


if __name__ == "__main__":
    standalone()
