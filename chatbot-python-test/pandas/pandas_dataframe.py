import pandas as pd

# 계절별 서울/부산 지역 온도 데이터 정의
temperatures = [[1, 2, 3, 4], [5, 6, 7, 8]]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
regions = ['Seoul', 'Pusan']

# 데이터프레임 객체 생성
data = pd.DataFrame(temperatures, index=regions, columns=seasons)

print(data)
print("=" * 50)
print(data.index)
print(data.columns)
print(data.values)
print("=" * 50)

print(data['Spring']['Seoul'])
print("=" * 50)

# 앞부분에서 첫번째 행까지 조회
print(data.head(1))

# 뒷부분에서 첫번째 행까지 조회
print(data.tail(1))

user_list = pd.read_excel('../excell/sample.xlsx', sheet_name='Sheet1')
print(user_list)