import pandas as pd

# 리스트 --> 행 인덱스
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서', '예은'],
                  columns=['나이','성별','학교'])

print(df)
print()
print(df.index)
print(df.columns)

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print()
print(df)
print()
print(df.index)
print(df.columns)