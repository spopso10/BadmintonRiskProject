import pandas as pd
import random
from datetime import datetime, timedelta

# venue date day_of_week hour total_courts booked_courts utilisation

data = [] # 30 days, 5 venues, 16 slots daily
# 2400 rows, 7 columns 

venues = {
    "USC Hall": 6,
    "MPSH 1": 4,
    "MPSH 2": 4,
    "UTown Sports Hall": 8,
    "Kent Ridge Hall": 3
}
start_date = datetime(2025, 12, 25)
num_days = 30 #for the next 30 days
hours = range(7,23) #timings range from 7am to 10pm
#hours is an immutable iterable
#print(list(venues.keys()))

for venue, total_courts in venues.items(): #for each venue
    for i in range(num_days): #30 days
        current = start_date + timedelta(days=i)
        # current.date() to get just the date
        day = current.strftime("%A")
        for hour in hours: #16 time slots for each day
            booked_courts = 0.3*total_courts #base demand (demand scales with venue size)
            if hour in [18, 19, 20]: # peak hours
                booked_courts += 0.4*total_courts
            if day in ["Saturday", "Sunday"]: # weekends are busier
                booked_courts += 0.2*total_courts
            noise = random.uniform(-0.2, 0.2)*total_courts
            booked_courts += noise # element of randomness
            if booked_courts > total_courts: # cannot exceed total
                booked_courts = total_courts
            if booked_courts < 0: # cannot be negative
                booked_courts = 0

            utilisation = round(booked_courts / total_courts, 1)
            data.append([
                venue,
                current.date(),
                day,
                hour,
                total_courts,
                round(booked_courts),
                utilisation
            ])
    
columns = ["venue", 
           "date", 
           "day_of_week", 
           "hour", 
           "total_courts", 
           "booked_courts", 
           "utilisation"]
df = pd.DataFrame(data, columns = columns)
df.to_csv("bookings.csv", index = False)