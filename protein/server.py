import aiohttp_cors
from aiohttp import web
import logging

from protein.routes import routes
from protein.middleware import middleware_cache, middleware_db

from settings import settings

logger = logging.getLogger(__name__)


app = web.Application(
    middlewares=[
        middleware_cache,
        middleware_db,
    ]
)
app.settings = settings



# Add routes
for route in routes:
    app.router.add_route(*route)

# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})


# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)


# This is useful if you want to launch default aiohttp
# server without gunicorn worker
#
# PYTHONPATH=. python user/server.py
if __name__ == '__main__':
    import logging

    access_log = logging.getLogger('aiohttp.access')
    access_log.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler()
    access_log.addHandler(stdout_handler)

    web.run_app(app)
