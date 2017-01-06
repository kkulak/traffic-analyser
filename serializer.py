import datetime

def serialize(db, file):
	db_keys = db.keys()
	csv_header = ','.join(['Timestamp'] + db_keys)

	with open(file, 'w') as file:
		file.write(csv_header + '\n')

		for entry in db.entries():
		    timestamp = datetime.datetime.fromtimestamp(entry.timestamp).strftime('%H:%M')
		    values = [__denormalize(entry.value, key) for key in db_keys]
		    csv_entry = ','.join([timestamp] + values)
		    file.write(csv_entry + '\n')

def __denormalize(entries, key):
	matching_entry = filter(lambda entry: entry['Name'] == key, entries)
	float_value = 0 if len(matching_entry) == 0 else matching_entry[0]['Confidence']
	return str(float_value)