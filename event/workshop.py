from datetime import timedelta

from event import Event


class Workshop(Event):
    @property
    def duration(self):
        return self._duration + timedelta(minutes=10)

    @duration.setter
    def duration(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError(f'Invalid duration value: {val}')

        if not (10 < val < 600):
            raise ValueError(f'Too short or too long: {val}')

        self._duration = timedelta(minutes=val)