## Problem Statement
- Booking badminton courts can be difficult during peak hours due to high demand and limited court capacity. Users face uncertainty about availability and risk of fully booked slots.

- This project analyses historical booking data to quantify risk levels for different venues, times, and days, helping users make informed decisions during booking.

## Assumptions
- Each user can only book 1 court at 1 time slot, each booking is 1 hour 
- Courts are booked via a balloting system; users who try to book the court may or may not be successful
- Bookings are independent
- No last minute cancellations
- Venues have fixed number of courts
- Every court is identical, there is no preference for certain courts
- Demand varies by (a) day of the week, (b) time of the day and (c) location

## Format of data
| Column Name    | Meaning                                     |
|----------------|---------------------------------------------|
| venue          | Name of venue                               |
| date           | YYYY-MM-DD                                  |
| day_of_week    | Monday, Tuesday etc                         |
| hour           | Hour of the booking (18, 19, 20 …)          |
| total_courts   | Total number of courts at the venue         |
| booked_courts  | Number of courts booked (demand)            |
| utilisation    | booked_courts / total_courts                |

## Methodology
1. Calculate utilisation for each venue-hour combination. (utilisation = booked_courts / total_courts)
2. Assign a risk level (Low, Medium, High) based on risk score. (risk_score = 0.5 * utilisation + 0.3 * peak_hour_flag + 0.2 * weekend_flag)
3. Group data by venue, hour, and day of week to identify peak periods.
4. Visualise utilisation trends and risk distribution to get insights.

## Limitations
- The model does not account for sudden changes in demand.
- External factors such as weather or holidays are not included.
- Assumes equal probability of booking across users; does not model individual behaviour.
- Risk scores are heuristic-based and not probabilistic.
