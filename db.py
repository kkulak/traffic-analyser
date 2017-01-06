from itertools import chain, imap

class DBEntry:

	def __init__(self, timestamp, value):
		self.timestamp = timestamp
		self.value = value

class DB:

    def __init__(self):
        self.data = []

    def store(self, timestamp, value):
        self.data.append(DBEntry(timestamp, value))

    def __distinct(self, lst):
        return list(set(lst))

    def entries(self):
        return self.data

    def keys(self):
        return self.__distinct([db_entry_value['Name'] for db_entry in self.data for db_entry_value in db_entry.value])