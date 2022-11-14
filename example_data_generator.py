import datetime

from data_generator import DataGenerator

event_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me please', 'emergency meeting'],
    ['ryszard ochodzki', 'wacek', 'szwedka', 'trener', 'minister'],
    False,
    False
)
events = event_data.generate_data(150)
reminder_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me please', 'emergency meeting'],
    ['ryszard ochodzki', 'wacek', 'szwedka', 'trener', 'minister'],
    True,
    False
)
reminder_events = reminder_data.generate_data(50)
workshop_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me please', 'emergency meeting'],
    ['ryszard ochodzki', 'wacek', 'szwedka', 'trener', 'minister'],
    False,
    True
)
workshops = workshop_data.generate_data(50)


event_data.save_data(events, 'events_data.json')

reminder_data.save_data(reminder_events, 'reminder_data.json')

workshop_data.save_data(workshops, 'workshop_data.json')