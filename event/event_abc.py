from abc import ABC, abstractmethod


class EventABC(ABC):

	def __init__(self, title, location, start_time, duration, owner, participants):
		self.title = title
		self.location = location
		self.start_time = start_time
		self.duration = duration
		self.owner = owner
		self.participants = participants

	@staticmethod
	@abstractmethod
	def room():
		return 42

	@classmethod
	@abstractmethod
	def custom_constructor(cls):
		pass

	@abstractmethod
	def __str__(self):
		pass

	@property
	@abstractmethod
	def title(self):
		pass

	@title.setter
	@abstractmethod
	def title(self, val):
		pass

	def __repr__(self):
		attrs = ', '.join(f'{k if k[0] != "_" else k[1:]}={v}' for k, v in self.__dict__.items())
		return f"{type(self).__name__}({attrs})"
