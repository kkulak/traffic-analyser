
class DBEntry:

	def __init__(self, timestamp, value):
		self.timestamp = timestamp
		self.value = value

class DB:

    def __init__(self):
        self.data = []

    def store(self, timestamp, value):
        self.data.append(DBEntry(timestamp, value))

    def __distinct__(self, lst):
        return list(set(lst))
 
    def keys(self):
        return self.__distinct__(map(lambda e: e.value['Name'], self.data))