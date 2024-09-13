import time
from datetime import datetime

process_start = time.process_time()
curr_time = time.localtime()
print(curr_time)
print(curr_time.tm_year)
print(curr_time.tm_mon)
print(curr_time.tm_mday)

print(str(curr_time))
time.sleep(1)
curr = time.time()
print(curr)
total = time.time() - curr
print(total)

# asctime([tupletime])
print(time.asctime(time.localtime()))
print(time.asctime(curr_time))

# ctime([secs])
print(time.ctime())
print(time.ctime(curr))

# gmtime([secs])
print("gmtime:", time.gmtime(1000))

# localtime([])
print("localtime:", time.localtime(1000))

# perf_counter
start = time.perf_counter_ns()
print(start)
stop = time.perf_counter_ns()

print(stop - start)

# process_time()
print(time.process_time() - process_start)

# sleep(sec)
# time.sleep(1)

# strptime(str, format)
print(time.strptime("Sep 20, 2022", "%b %d, %Y"))

# strftime
print(time.strftime("%d/%m/%Y %H:%M:%S %Z", time.localtime()))


now = time.time()
print("time:", now)

my_datetime = datetime.fromtimestamp(now)
print("datetime:", my_datetime)
