"""
Python library to communicate with an obs-websocket server.
"""

from .base_classes import Baseevents, Baserequests, ClassFactory

events = ClassFactory(Baseevents)
requests = ClassFactory(Baserequests)

from .core import obsws  # noqa: E402

__all__ = ["obsws", "events", "requests"]

VERSION = "1.0"
