from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "오늘 날씨는 구름이 많아요."

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)

# 단어 사전 구축 및 단어별 인덱스 부여
dict = {}
for word in nouns:
    if word not in dict.keys():
        dict[word] = len(dict)
print(dict)

# 원-핫 인코딩
nb_classes = len(dict)
targets = list(dict.values())
# 인자 크기대로 단위 행렬을 생성
# target을 이용하여 생성된 단위행렬의 순서를 단어 사전의 순서에 맞게 정렬
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)