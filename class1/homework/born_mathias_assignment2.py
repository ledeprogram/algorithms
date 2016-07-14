
import csv
import random

# User input
def get_name():
    return input("What's the name of the person you were supposed to meet? ")

def get_location():
    return input("Where were you supposed to go? ")

def make_excuse(excuses, name, location):
    a_number = random.randint(0,len(excuses)-1)
    phrase = excuses[a_number][0]
    weblink = excuses[a_number][2]
    excuse = "Sorry, " + name + ", I was late to " + location + " to meet you, " + phrase + ". (Source: " + weblink + ")"
    return excuse

# Import csv with exuses
infile = '/home/this/Dokumente/bz/ny/algorithms/class1/homework/data/excuse.csv'
reader = csv.reader(open(infile))
excuses = list(reader)[1:]

user_name = get_name()
user_loc = get_location()
print(make_excuse(excuses, user_name, user_loc))
