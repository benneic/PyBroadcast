# -*- coding: utf-8 -*-

"""
pyroamz.create
~~~~~~~~~~~~~~

This module provides the entry points for pyBroadcast.
"""

from .api import Broadcast
import os

def create(base_url=None):
    """Returns a Broadcast instance."""

    return Broadcast(base_url=base_url)