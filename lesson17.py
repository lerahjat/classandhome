import os
import json
import csv
import googlemaps
from datetime import datetime
from dataclasses import dataclass


class OpenFile:

    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()
        return True


class Maps:

    def __init__(self, key):
        self._client = googlemaps.Client(key=key)

    def __enter__(self):
        return self._client

    def __exit__(self, error_type, value, traceback):
        del self._client
        return True


@dataclass
class Tag:

    name: str
    color: str = 'Yellow'


class Task:

    def __init__(self, title):
        self.done = False
        self.title = title
        self._priority = 1
        self.location = None
        self.tag = Tag('Default tag')

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'Task(title=\'{}\')'.format(self.title)

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def add_location(self):
        place_lookup = input('Enter location name: \t')
        with Maps(key='AIzaSyCZ8gzf2JOsUXTTXwG7lXWiLw5LFJ0-qRI') as gmaps:
            place = gmaps.find_place(
                place_lookup,
                'textquery',
                fields=['geometry/location', 'name', 'place_id']
            )
            if place['status'] == 'OK':
                self.location = {
                    'coordinates': place['candidates'][0]['geometry']['location'],
                    'name': place['candidates'][0]['name'],
                    'google_id': place['candidates'][0]['place_id']
                }


class Dashboard:

    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:   ')
        new_task = Task(title)
        self.task_list.append(new_task)

    def print_all_tasks(self):
        for task in self.task_list:
            print(task)

    def sort_by_title(self):
        return sorted(self.task_list,
            key=lambda task: task.title)

    def dump_to_json(self):
        task_list = [t.__dict__ for t in self.task_list]
        dump_time = datetime.now()
        filename = 'tasks_{}.json'.format(
            dump_time.strftime('%Y%m%d%H%M%S'))
        filepath = os.path.join(os.getcwd(),'data', filename)


# load_from_json
    def load_from_json(self):
        dirpath = os.path.join(os.getcwd(), 'data')
        files_data = os.listdir(dirpath)
        filepath = os.path.join(os.getcwd(), 'data',[file for file in files_data if file.endswith('json')][-1])

# dump_to_csv
    def dump_to_csv(self):
        filename = f'tasks_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
        filepath = os.path.join(os.getcwd(), 'data', filename)
        task_list = [task.__dict__ for task in self.task_list]
        with OpenFile(filepath, 'w') as file:
            writer = csv.DictWriter(file, [dict_task.keys() for dict_task in task_list][0])
            writer.writeheader()
            for dict_task in task_list:
                writer.writerow(dict_task)

# load_from_csv
    def load_from_csv(self):
        dirpath = os.path.join(os.getcwd(), 'data')
        files_data = os.listdir(dirpath)
        filepath = os.path.join(os.getcwd(), 'data',[file for file in files_data if file.endswith('csv')][-1])


        task_list = []
        with OpenFile(filepath, 'w') as dump_file:
            json.dump(task_list, dump_file)
            csv.dump(task_list,dump_file)






