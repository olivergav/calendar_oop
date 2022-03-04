import os.path

from data import GenerateData
from event import Event

from pprint import pprint as pp

base_dir = os.path.dirname(__file__)
print(base_dir)


def main(path):
	data = GenerateData()
	if not os.path.exists(path):
		data.generate(500, path)

	events = []
	events_json = GenerateData.load(path)
	for event_ in events_json:
		events.append(Event(**event_))

	pp(events)


if __name__ == '__main__':
	main(os.path.join(base_dir, 'data', 'data.json'))