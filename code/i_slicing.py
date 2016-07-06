from d_yield_away import classic_fibonacci as fibonacci
from i_slicing_support import session_factory, Measurement

nums = fibonacci(200)

print("All nums")
print(nums)
print()

print("First 5 nums")
print(nums[:5])
print()

print("2->7 nums")
print(nums[2:8])
print()

print("Last 3 nums (less good via len)")
print(nums[len(nums) - 3:len(nums)])
print()

print("Last 3 nums (pythonic)")
print(nums[-3:])
print()

s = session_factory()
measurements = s.query(Measurement). \
    filter(Measurement.value > .9). \
    order_by(Measurement.value.desc())

print("Top three measurements values via SQLAlchemy")
top_three = [m.value for m in measurements[:3]]
for v in top_three:
    print(v, end=', ')
