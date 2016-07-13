
#coding: utf-8
#Mayoral Excuse Machine
#Create your own version of the Mayoral Excuse Machine in Python that
#takes in a name and location, selects an excuse at random and prints
#an excuse (“Sorry, Richard, I was late to City Hall to meet you, I had
#a very rough night and woke up sluggish”)

#Use the “excuses.csv” in the Github repository
#Extra credit if you print the link to the story as well

import pandas as pd
import random
from random import randint

#Asking for the persons name:
Name = input("Who were you supposed to meet? ")
#And there location
Location = input("Where were you supposed to meet them? ")

#Setting up the data. First, creating Pandas file:
df = pd.read_csv("data/excuse.csv")

#This is the formatting you need to change a Pandas DF into a list of Dictionaries:
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html
list_of_dict = df.to_dict('records')

number = randint(0,9)
print("Sorry, {}, I was late to {} to meet you, {}. Story Link: {}".format\
    (Name, Location, list_of_dict[number]['excuse'], list_of_dict[number]\
    ['hyperlink']))
