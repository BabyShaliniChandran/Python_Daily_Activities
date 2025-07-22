fruit_price={
"elppa":100,
"ybab":20,
"ananab":30}
from collections import Counter
user_input = input()
print(fruit_price[[*fruit_price][(Counter(user_input) == Counter([*fruit_price][0])) * 0 + (Counter(user_input) == Counter([*fruit_price][1])) * 1 + (Counter(user_input) == Counter([*fruit_price][2])) * 2]])

