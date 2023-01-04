import datetime
import random

from data_generator import DataGenerator


def test_data_construction():
    data_gen = DataGenerator(datetime.date.today() + datetime.timedelta(days=2), 30, 'meeting', 'desc', 'zbyszko')
    assert isinstance(data_gen, DataGenerator)


def test_reminder_construction():
    data_gen = DataGenerator(datetime.date.today() + datetime.timedelta(days=2), (30,50), 'meeting', 'desc', 'zbyszko', reminder=True)
    reminders = data_gen.generate_data(1)
    assert 'remind' in reminders[0]


def test_workshop_construction():
    data_gen = DataGenerator(datetime.date.today() + datetime.timedelta(days=2), (30,50), 'meeting', 'desc', 'zbyszko', workshop=True)
    workshops = data_gen.generate_data(1)
    assert 'participants' in workshops[0]


def test_events_generator():
    data_gen = DataGenerator(datetime.date.today() + datetime.timedelta(days=2), (30,50), 'meeting', 'desc', 'zbyszko')
    evts = data_gen.generate_data(2)
    assert len(evts) == 2

