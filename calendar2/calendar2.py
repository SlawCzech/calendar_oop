import datetime
from pprint import pprint

from main import data
from helpers import generate_objects

from event import Reminder, Workshop, Event


class Calendar:
    def __init__(self, events=None):
        self._events = events or []

    @property
    def events(self):

        counter = 0
        for event in self._events:
            if datetime.datetime.now() < event.start_date < datetime.datetime.now() + datetime.timedelta(weeks=4):
                counter += 1
            return f'You have {counter} events in next four weeks.'

    @events.setter
    def events(self, value):

        if not isinstance(value, (Event, Workshop, Reminder)):
            raise TypeError(f'Invalid datatype. You entered {type(value)}')

        self._events.append(value)

    def filter_by_date(self, start_date=datetime.datetime.min, end_date=datetime.datetime.max):

        events = []

        for event in self._events:
            if start_date <= event.start_date < end_date:
                events.append(event)

        return events

    def __len__(self):
        return len(self._events)



calendar = Calendar(data)

print('data', len(data))

filter = calendar.filter_by_date(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(weeks=4))
# pprint(filter)

print(len(filter))
pprint(calendar)


