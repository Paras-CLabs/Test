import random
import datetime 
import string


eventID_lists = random.sample(range(10, 30), 10)


def generate_dates(today,count):
   while count >= 0:
       date_time = today + datetime.timedelta(hours =random.randrange(4), minutes=random.randrange(60))
       yield date_time
       count -= 1
today = datetime.datetime(2022, 1, 31,13,00)
timestamp_lists=[]
for x in generate_dates(today,10):
    timestamp_lists.append(x.isoformat())
    
    
letters = string.ascii_lowercase
message_lists=[]
for j in range(10):   
    message_lists.append(''.join(random.choice(letters) for i in range(10)))


with open('Event_records.txt', 'w') as file:
    file.writelines("Event_ID Time Message\n")
    for index,i in enumerate(eventID_lists):
        file.writelines(f"{i} {timestamp_lists[index]} {message_lists[index]}\n")

