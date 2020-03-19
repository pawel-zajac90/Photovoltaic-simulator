import datetime
seconds_of_the_day = 60*60*24

def time():
    y = datetime.date.today().year
    m = datetime.date.today().month
    d = datetime.date.today().day
    t = datetime.datetime(y, m, d)
    delta = datetime.timedelta(seconds=1)
    for _ in range(seconds_of_the_day):
        yield t
        t += delta
