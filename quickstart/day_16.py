# Day 16: datetime
from datetime import date, datetime, timedelta

now = datetime.now()
print(now.day, now.month, now.year, now.hour, now.minute)   # Ex 1
print(now.timestamp())                                      # seconds since 1 Jan 1970

print(now.strftime('%d/%m/%Y %H:%M'))                       # Ex 2: date -> text
# %d day  %m month  %Y year  %H hour  %M minute  %S second  %B full month name

d = datetime.strptime('14 March, 2027', '%d %B, %Y')        # Ex 3: text -> date
print(d)                                                    # the format must match exactly

print(datetime(now.year + 1, 1, 1) - now)                   # Ex 4-5: date - date = timedelta
print(date(2027, 1, 1) + timedelta(days=30))                # date + timedelta = date
