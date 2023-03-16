"""
problem H:

If you have ever travelled internationally by plane, you will be aware that working out
when you are going to arrive at your destination depends on the flight time and the
time zone difference between departure and destination airports.
In this problem you will be given the departure city, its time zone and the departure
time, the destination city and its time zone, and the flight time. From this data you
must calculate the arrival time.

Input:

Input will be for a single journey in the following format:
Line 1: The departure city
Line 2: The time of departure as mm dd hh:mm (month, day, hours and minutes all as
2 digits and separated by spaces and a colon as shown).
Line 3: The time zone of the departure city as (UTC) + or –hh:mm
Line 4: The destination city
Line 5: The time zone of the destination city as (UTC) + or –hh:mm
Line 6: The flight time as hh:mm (hours and minutes both as 2 digits and separated by
a colon)
A time zone which is exactly UTC will be shown as 00:00. Flights have been selected
so that:
• No flight crosses the International Date Line.
• Flights arrive on the day of departure or the following day.

Output:

Two lines giving the city and time of departure and the city and time of arrival. The
lines will start with the words Departs and Arrives respectively.
Departure time to be shown as mm dd hh:mm , as in the input.
Arrival time to be shown as hh:mm (hours and minutes, both as 2 digits and separated
by a colon) followed by either same day or following day as appropriate.
"""

departureCity = input()
departureTime = input()
departureDay = int(departureTime.split(' ')[0])
departureMonth = int(departureTime.split(' ')[1])
departureHour = int(departureTime.split(' ')[2].split(':')[0])
departureMin = int(departureTime.split(' ')[2].split(':')[1])
departureTimeZone = input()

destinationCity = input()
destinationTimeZone = input()
flightTime = input()

