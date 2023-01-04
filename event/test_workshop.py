from datetime import datetime, timedelta

from event import Workshop


def test_workshop_construction():
    work = Workshop(1, datetime.now() + timedelta(days=1), 30, '', '', '', '')
    assert isinstance(work, Workshop)
