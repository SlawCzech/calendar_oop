from datetime import datetime, timedelta

from event import Reminder


def test_reminder_construction():
    remind = Reminder(1, datetime.now() + timedelta(days=1), 30, '', '', '', '')
    assert isinstance(remind, Reminder)
