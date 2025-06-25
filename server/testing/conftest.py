#!/usr/bin/env python3
import pytest
from config import app, db

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

@pytest.fixture(autouse=True, scope='session')
def setup_database():
    with app.app_context():
        db.create_all()
    yield
    # Optionally, drop tables after tests
    # with app.app_context():
    #     db.drop_all()