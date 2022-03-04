from datetime import datetime, timedelta

from data import GenerateData
from event.event_abc import EventABC


class Event(EventABC):

    @staticmethod
    def room():
        return super().room()

    @classmethod
    def custom_constructor(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.magic = lambda self: 42

        super().__init__(obj, *args, **kwargs)

        return obj

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        if isinstance(val, str):
            if len(str(val)):
                self._title = str(val)
            else:
                self._title = 'No title'

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, val):
        if not isinstance(val, str):
            raise ValueError(f'Invalid new date value: {val}')

        try:
            parsed_datetime = datetime.strptime(val, '%d-%m-%Y %H:%M')
        except ValueError:
            raise ValueError(f'Invalid date format, use DD-MM-YYYY HH:MM, {val}')

        if parsed_datetime < datetime.now() + timedelta(minutes=15):
            raise ValueError(f'Try to use a date in the future, dummy... {parsed_datetime}')

        self._start_time = parsed_datetime

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError(f'Invalid duration value: {val}')

        if not (10 < val < 600):
            raise ValueError(f'Too short or too long: {val}')

        self._duration = timedelta(minutes=val)

    def __str__(self):
        total_seconds = (self.start_time - datetime.now())
        hours, rest = total_seconds.seconds // (60 * 60), total_seconds.seconds % (60 * 60)
        minutes, seconds = rest // 60, rest % 60
        return f"{self.title}, time to event: {total_seconds.days} days, {hours} hour(s), {minutes} minute(s), {seconds} second(s). "