from d_yield_away import classic_fibonacci as fibonacci
from i_slicing_support import session_factory, Measurement

nums = fibonacci(200)

print("All nums")
print(nums)
print()

print("First 5 nums")
# TODO
print()

print("2->7 nums")
# TODO
print()

print("Last 3 nums (less good via len)")
# TODO
print()

print("Last 3 nums (pythonic)")
# TODO
print()

s = session_factory()
measurements = s.query(Measurement). \
    filter(Measurement.value > .9).\
    order_by(Measurement.value.desc())

print("Top three measurements values via SQLAlchemy")
# TODO