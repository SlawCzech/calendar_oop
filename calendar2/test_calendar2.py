from datetime import datetime, timedelta

import pytest

from calendar2.calendar2 import Calendar
from event import Event, Reminder, Workshop


@pytest.fixture
def event():
    return Event(1, datetime.now() + timedelta(days=1), 30, 'short event', 'desc_1', 'tomek')


@pytest.fixture
def reminder():
    return Reminder(2, datetime.now() + timedelta(days=2), 60, 'medium reminder', 'desc_2', 'kasia', True)


@pytest.fixture
def workshop():
    return Workshop(3, datetime.now() + timedelta(days=2), 90, 'long workshop', 'desc_3', 'elo', ['brygada', 'ekipa'])


@pytest.fixture
def cal_object(event, reminder, workshop):
    return Calendar([event, reminder, workshop])


def test_calendar_object(cal_object):
    assert len(cal_object) > 0


def test_events_counter(cal_object):
    assert cal_object.events == 'You have 3 events in next four weeks.'


def test_filter_by_date(cal_object):
    assert len(cal_object.filter_by_date(datetime.now(), datetime.now() + timedelta(hours=30))) == 1


def test_filter_by_duration(cal_object):
    assert len(cal_object.filter_by_duration(duration_max=45)) == 1


def test_filter_by_exact_duration(cal_object):
    assert len(cal_object.filter_by_duration(duration=30)) == 1


# def test_setter_event(cal_object):
#     cal_object.events(Event(4, datetime.now() + timedelta(days=1), 50, '', '', ''))
#     assert len(cal_object) == 4


def test_setter_invalid(cal_object):
    with pytest.raises(TypeError):
        cal_object.events(datetime.today())


def test_remove_event(cal_object):
    cal_object.remove(1)
    assert len(cal_object) == 2


def test_remove_event_not_existing(cal_object):
    with pytest.raises(ValueError):
        cal_object.remove(4)


def test_custom_filter_title(cal_object):
    assert len(cal_object.filter('title', search_text='medium reminder')) == 1


def test_custom_filter_duration(cal_object):
    assert len(cal_object.filter('duration', max=80)) == 2


def test_custom_filter_description(cal_object):
    assert len(cal_object.filter('description', search_text='desc_3')) == 1


def test_custom_filter_owner(cal_object):
    assert len(cal_object.filter('owner', search_name='kasia')) == 1


def test_custom_filter_participants(cal_object):
    assert len(cal_object.filter('participants', search_name='ekipa')) == 1
