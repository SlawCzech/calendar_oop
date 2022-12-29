from datetime import datetime, timedelta

from event import Event
import pytest


@pytest.fixture
def event():
    return Event(1, datetime.now() + timedelta(days=1), 30, '', '', '')


def test_duration_less_than_10_min_raise_error():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(days=1), 5, '', '', '')
        assert 'in one hour the earliest' in str(excinfo.value)


def test_duration_change_less_than_10_min_raise_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.duration = 5

        assert 'cannot be shorter than 10 minutes' in str(excinfo.value)


def test_duration_positive(event):
    assert event.duration == 30


def test_duration_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, datetime.now() + timedelta(days=1), '5', '', '', '')

        assert 'should be a positive digit' in str(excinfo.value)


def test_start_date_less_than_1_hour():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(minutes=30), 30, '', '', '')

        assert 'in one hour the earliest' in str(excinfo.value)


def test_start_date_change_with_less_than_hour(event):
    with pytest.raises(ValueError) as excinfo:
        event.start_date = datetime.now() + timedelta(minutes=30)

        assert 'in one hour the earliest' in str(excinfo.value)


def test_start_date_invalid_type_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, 5, 30, '', '', '')

    assert 'Provided value is not date or time' in str(excinfo.value)


def test_start_date_positive(event):
    assert f'{event.start_date:"%A %b %y, %H:%M"}' == f'{(datetime.now() + timedelta(days=1)):"%A %b %y, %H:%M"}'
