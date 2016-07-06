import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 44),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# C-style
high_measurements1 = [] # all with value over 70
# TODO

# list comprehension
# TODO
high_measurements2 = []

# generator expression
# TODO


# process the generator to get something printable.
# TODO
high_measurements3 = list()

# dict comprehension
# TODO
high_m_by_id = {}

# set comprehension
# TODO
high_values_distinct = set()

print(high_measurements1)
print(high_measurements2)
print(high_measurements3)
print(high_m_by_id)
print(high_values_distinct)
