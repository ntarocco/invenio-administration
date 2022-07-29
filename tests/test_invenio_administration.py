# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 CERN.
#
# invenio-administration is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_administration import invenioadministration


def test_version():
    """Test version import."""
    from invenio_administration import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = invenioadministration(app)
    assert "invenio-administration" in app.extensions

    app = Flask("testapp")
    ext = invenioadministration()
    assert "invenio-administration" not in app.extensions
    ext.init_app(app)
    assert "invenio-administration" in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert "Welcome to invenio-administration" in str(res.data)