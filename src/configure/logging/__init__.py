
import logging

from pyramid.events import NewRequest


def log_request_url(event):
    request = event.request
    log = logging.getLogger(__name__)
    log.info("[%s] %s", request.remote_addr, request.url)


def includeme(config):
    config.add_subscriber(log_request_url, NewRequest)
