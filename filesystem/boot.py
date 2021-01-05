
from machine import reset
from micropython import alloc_emergency_exception_buf

from femtoweb.server import Config as webserver_config

from data import (
    config,
    load_datafiles
)
from lib.filesystem import init_filesystem
from lib.wifi import (
    connect_to_access_point,
    create_access_point,
)

alloc_emergency_exception_buf(100)

# Ensure that the required directories exist and wipe the temp directory.
init_filesystem()

# Load the device configuration.
load_datafiles()

if config['WIFI_STATION_CONNECT_ON_BOOT']:
    connect_to_access_point(
        config['WIFI_STATION_SSID'],
        config['WIFI_STATION_PASSWORD']
    )

if config['WIFI_CREATE_ACCESS_POINT_ON_BOOT']:
    create_access_point()

# Configure the webserver
webserver_config.port = config['WEBSERVER_PORT']
webserver_config.backlog = config['WEBSERVER_BACKLOG']
webserver_config.use_cors = config['WEBSERVER_USE_CORS']
