# -*- coding: utf-8 -*-

"""
pybroadcast.create
~~~~~~~~~~~~~~

This module provides the entry points for pyBroadcast.
"""

from .api import Broadcast
import os

DEFAULT_BASE_URL='http://localhost:7000/'

def create(base_url=None):
    """Returns a Broadcast instance."""

    if not base_url:
      base_url = os.environ['PYBROADCAST_BASE_URL'] if os.environ.has_key('PYBROADCAST_BASE_URL') else DEFAULT_BASE_URL

    return Broadcast(base_url=base_url)