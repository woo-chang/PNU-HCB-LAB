import matplotlib.pyplot as plt

temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# 바차트 출력
plt.title("Bar Chart");
# x축은 y축의 카테고리를 의미
plt.bar(x, temperatures);
# x축 데이터 위치에 라벨을 표시
plt.xticks(x, x_labels);
# 오름차순으로 정렬된 온도값을 y축에 표시
plt.yticks(sorted(temperatures));
plt.xlabel("계절")
plt.ylabel("온도")
plt.show()