import pyupbit
import numpy as np

#OHLCV(OPEN, HIGH, LOW, CLOSE, VOLUME)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=7)

# 변동성 돌파 기준 범위 계산, (고가-저가) *k 값 계산
df['range'] = (df['high'] - df['low']) * 0.5
# target(매수가), range 컬럼을 한칸씩 밑으로 내림
df['target'] = df['open'] + df['range'].shift(1)

print(df)
# ror(수익률), npwhere(조건문, 참일때 값, 거짓일떄 값)
df['ror'] = np.where(df['high'] > df['target'],
                    df['close'] / df['target'],
                    1)
#누적 곱 계싼(cumprod) =>누적수익률
df['hpr'] = df['ror'].cumprod()
#draw donw 계산 (누적최대값과 현재 hpr 차이/ 누적 최대값 *100 )
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#mdd 계산
print("MDD(%): ", df['dd'].max())
#엑셀 출력
df.to_excel("dd.xlsx")