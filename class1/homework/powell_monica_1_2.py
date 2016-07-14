import pandas as pd
excuses_df= pd.read_csv("data/excuse.csv")





person = input('Enter your name: ')

location = input('Where was the mayor supposed to meet you? ')



import random

stop = len(excuses_df)
random_index = random.randrange(stop)
link = excuses_df['hyperlink'][random_index]
random_excuse = excuses_df['excuse'][random_index]

print("Sorry,", person, "I was late to", location, 'to meet you,', random_excuse, "url: " , link)
