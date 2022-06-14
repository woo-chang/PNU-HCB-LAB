from konlpy.tag import Komoran

# txt, tsv 파일을 파이참에서 생성하게 되면 Tab 인식이 잘 안되는 듯
# 외부에서 생성해서 가져오니까 잘 되는 것을 확인
text = "우리 챗봇은 엔엘피를 좋아해."
komoran_1 = Komoran()
print(komoran_1.pos(text))

komoran = Komoran(userdic='./user_dic.txt')
pos = komoran.pos(text)
print(pos)