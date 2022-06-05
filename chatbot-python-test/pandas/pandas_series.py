import pandas as pd

# 인덱스를 생략한 시리즈 객체
numbers = pd.Series([100, 200, 300])
print(numbers)

# 인덱스를 지정한 시리즈 객체
scores = pd.Series([90, 80, 99], index=['국어', '수학', '영어'])
print(scores)
print(scores.index)
print(scores.values)
print(scores.index[1], scores.values[1])