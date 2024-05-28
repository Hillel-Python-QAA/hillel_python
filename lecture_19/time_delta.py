from datetime import timedelta, datetime


now = datetime.now()
print(now)
past_date = now - timedelta(days=5, hours=4)
print(past_date)

time_diff = now - past_date
print(time_diff)

print(timedelta(days=5))


def is_diff_more_30_sec(time_a: datetime, time_b: datetime) -> bool:
    time_difference = time_b - time_a
    return time_difference > timedelta(seconds=30)


time_a = datetime.now()
time_b = time_a + timedelta(seconds=31)

if is_diff_more_30_sec(time_a, time_b):
    print("WARNING! The difference is greater then 30 seconds!")
