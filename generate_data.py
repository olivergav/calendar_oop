from random import randint, choice
from pprint import pprint as pp

from app import Event


class GenerateData:
	def __init__(self):
		self.title = ['piwo', 'wino', 'wódka']
		self.location = ['amsterdam', 'berlin', 'warszawa']
		self.users = ['ala', 'ola']

	@staticmethod
	def _start_time_generator():
		return f'{randint(1, 28)}-{randint(2, 12)}-{randint(2022, 2050)} {randint(0, 23)}:{randint(0, 59)}'

	def do_magic(self, amount):
		temp = []

		for i in range(amount):
			temp.append(Event(
				choice(self.title),
				choice(self.location),
				self._start_time_generator(),
				randint(15, 599),
				choice(self.users),
				[choice(self.users) for _ in range(randint(0, len(self.users) - 1))]
			))
		pp(temp)

g = GenerateData()
g.do_magic(10)



