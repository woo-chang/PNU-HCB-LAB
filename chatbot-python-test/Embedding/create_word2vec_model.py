from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# 데이터 읽어오기
def read_review_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 헤더 제거
    return data

# 학습 시간 측정
start = time.time()

# 리뷰 파일 읽어오기
print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./ratings.txt')
print(len(review_data)) # 리뷰 데이터 전체 개수
print('1) 말뭉치 데이터 읽기 완료 : ', time.time() - start)

# 문장 단위로 명사만 추출해 학습 입력 데이터로 만들기
print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료 : ', time.time() - start)

# Word2Vec 모델 학습
print('3) Word2Vec 모델 학습 시작')
# sentences : 모델 학습에 필요한 문장 데이터
# size -> vector_size : 단어 임베딩 벡터의 차원
# window : 주변 단어 윈도우의 크기
# hs : 0(0이 아닌 경우 음수 샘플링 사용), 1(모델 학습에 softmax 사용)
# min_count : 단어 최소 빈도 수, 설정된 빈도 수 이하의 단어들은 학습하지 않음
# sg : 0(CBOW 모델), 1(skip-gram 모델)
# 모델학습에 필요한 세팅값은 하이퍼파라미터라고 한다.
# 함수에 사용되는 파라미터와는 다른 개념
model = Word2Vec(sentences=docs, vector_size=200, window=4, hs=1, min_count=2, sg=1)
print('3) Word2Vec 모델 학습 완료 : ', time.time() - start)

# 모델 저장
print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료 : ', time.time() - start)

# 학습된 말뭉치 수, 코퍼스 내 전체 단어 수
print("corpus_count : ", model.corpus_count)
print("corpus_total_words : ", model.corpus_total_words)