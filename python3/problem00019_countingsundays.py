'''
You are given the following information, but you may prefer to do some research
for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
        but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

ans = sum(day_of_the_week=='月' and nth_of_the_month==1
    for i, nth_of_the_month in enumerate(day
        for year in range(1901, 2001)
        for is_leap_year in [(year%4==0 and not year%100==0) or (year%400==0)]
        for days_in_month in [31,29 if is_leap_year else 28]+[31,30,31,30,31]*2
        for day in range(1, days_in_month+1)
    ) for day_of_the_week in ['月火水木金土日'[i%7]])
print(ans)
