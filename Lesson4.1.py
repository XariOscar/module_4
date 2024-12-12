from fake_math import divide as dfake
from true_math import divide as dtrue


result1 = dfake(69, 3)
result2 = dfake(3, 0)
result3 = dtrue(49, 7)
result4 = dtrue(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)