import datetime
import random
from pprint import pprint


class DataGenerator:
    def __init__(self, beginning_date, duration_range, titles, descriptions, users, reminder=False, workshop=False):
        self.beginning_date = beginning_date
        self.duration_range = duration_range
        self.titles = titles
        self.descriptions = descriptions
        self.users = users
        self.reminder = reminder
        self.workshop = workshop

    def generate_data(self, amount):
        events = []

        for idx in range(amount):
            event = {
                'idx': idx,
                'start_date': self.beginning_date + datetime.timedelta(hours=random.randint(1, 5000)),
                'duration': random.randint(*self.duration_range),
                'title': random.choice(self.titles),
                'description': random.choice(self.descriptions),
                'owner': random.choice(self.users),
            }

            if self.reminder:
                event['reminder'] = random.choice([True, False])

            if self.workshop:
                event['workshop'] = random.choices(self.users, k=random.randint(3, 20))

            events.append(event)

        pprint(events)


d = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me please', 'emergency meeting'],
    ['ryszard ochodzki', 'wacek', 'szwedka', 'trener', 'minister'],
    False,
    True
)

d.generate_data(50)

