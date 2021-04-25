import pyupbit

access = "8G08udKYKWAvK8b1xiHDx2qYUSCOVZlcEZUDdzig"
secret = "VAw4YLeMKiKj2UyMK91xBvqN8EKfwBNEt5WePQSL"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-Neo"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
print(upbit.get_balances())