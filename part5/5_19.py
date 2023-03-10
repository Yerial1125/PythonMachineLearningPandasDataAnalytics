import pandas as pd

# read_csv() 함수로 파일 읽어와서 df로 변환
df = pd.read_csv('data/stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
print(df.info())
df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())
print()

# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
df['Year'] = df.new_Date.dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df.new_Date.dt.day
print(df.head())
print()

# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df.new_Date.dt.to_period(freq='A')
df['Date_m'] = df.new_Date.dt.to_period(freq='M')
print(df.head())
print(df.info())
print()

# 원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_m', inplace=True)
print(df.head())