# -*- coding: utf-8 -*-
"""IOT Project
"""
import uasyncio

from femtoweb import (
    filesystem_http_endpoints,
    machine_http_endpoints,
)
from femtoweb.server import (
    _200,
    GET,
    as_type,
    route,
    serve,
)

PUBLIC_ROOT = '/'

async def init_app():
    # Define a root endpoint handler.
    @route('/', methods=(GET,))
    async def index(request):
        return filesystem_http_endpoints._fs_GET(
            PUBLIC_ROOT,
            '/public/index.html'
        )

    # Define another endpoint that accepts query args.
    @route('/echo', methods=(GET,), query_param_parser_map={
        'text': as_type(str)
    })
    async def echo(request, text):
        return _200(body=text)

if __name__ == '__main__':
    # Get the async event loop.
    event_loop = uasyncio.get_event_loop()

    # Attach the filesystem and machine HTTP endpoints.
    filesystem_http_endpoints.attach(PUBLIC_ROOT)
    machine_http_endpoints.attach()

    # Create a webserver task.
    event_loop.create_task(serve())

    # Run the application import/init as a task so that the web server
    # will still run when application code updates break things.
    event_loop.create_task(init_app())

    # Start the event loop.
    event_loop.run_forever()
