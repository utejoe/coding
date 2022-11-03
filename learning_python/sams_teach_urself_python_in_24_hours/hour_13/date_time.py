import datetime
from datetime import time
lunch = time(11, 30)
lunch = datetime.time(11, 30)
print(lunch)
print(lunch.hour)
print(lunch.minute)
print(lunch.second)
print("Lunch will be served at {minutes} minutes past {hour}".format(minutes=lunch.minute, hour=lunch.hour))