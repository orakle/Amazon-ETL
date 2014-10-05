import datetime
import csv
import json


review_list = []

# Read file into a list
# Strip new lines
for line in open('movies.small.txt'):
	# Ignore encoding errors (0xf8 error)  
	try:
		encoded_line = line.encode('utf-8')
	except Exception:
		pass
	review_list.append(encoded_line.strip())
    
# Grouping review into dict of dicts based on the empy string item
grouped_reviews = []
new_group = []
for line in review_list:
    if line != '':
        new_group.append(line)
    else:
        grouped_reviews.append(new_group)
        new_group = []

# Create a list of dictionaries
list_of_dict = []

for review in grouped_reviews:
    new_dict = {}
    for item in review:
        rev_key, rev_value = item.split(': ', 1)
        clean_rev_key = rev_key.split('/')[1]
        new_dict[clean_rev_key] = rev_value
    list_of_dict.append(new_dict)

# Convert time stamp into time
# Convert score string into float
for review in list_of_dict:
    # Convert string into a float
    review['score'] = float(review['score'])
    
    # Convert integer timestamp into year, month and date
    time_float = float(review['time'])
    temp_time = datetime.datetime.fromtimestamp(time_float)
    format_time = str(temp_time.month) + ':' + str(temp_time.day) + ':' + str(temp_time.year)
    review['time'] = format_time


# Output to tsv
# Create a writer object
writer = csv.DictWriter(open('movie.small.output.tsv', 'w'),
                       ['productId', 'profileName', 'helpfulness', 'score', 'time'],
                       delimiter = '\t',
                       extrasaction = 'ignore')
writer.writeheader()
for review in list_of_dict:
    writer.writerow(review)

# Output to JSON
with open('movie.small.output.json', 'w') as outfile:
		json.dump(list_of_dict, outfile)