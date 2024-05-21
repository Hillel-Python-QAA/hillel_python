# __iter__() - returns iterator object, calls when iter() function executed

# __next__()

my_iterable = iter([1, 2, 3, 4, 5])

print(my_iterable)

print(next(my_iterable))  # 1
print(next(my_iterable))  # 2
print(next(my_iterable))  # 3
print(next(my_iterable))  # 4
print(next(my_iterable))  # 5

try:
    print(next(my_iterable))  # StopIteration exception
except StopIteration:
    print("StopIteration: Iterator ended")


class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current
        else:
            raise StopIteration


my_iterator = MyIterator(5)
for num in my_iterator:
    print(num)
