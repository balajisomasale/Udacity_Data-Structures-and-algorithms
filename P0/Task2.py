"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_dur(data):
    
    # Creating a new dictionary as it has key value pairs and is best for this use case
    my_dictionary = {}
    
    # Iterating through and appending the values to my newly added dictionary
    for i in data:
        if i[0] not in my_dictionary:
            my_dictionary[i[0]] = int(i[3])

        if i[1] not in my_dictionary:
            my_dictionary[i[1]] = int(i[3])
            
        else:
            my_dictionary[i[0]] += int(i[3])
            my_dictionary[i[1]] += int(i[3])

    number_max = None
    number_dur = 0
    
    # Find the number with the maximum duration
    for k,v in my_dictionary.items():
        if v > number_dur:
            number_dur = v
            number_max = k

    return [number_max, str(number_dur)]

number, time = longest_dur(calls)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, time))

