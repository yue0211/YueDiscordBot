import datetime

#獲取當前時間
a = datetime.datetime.now().strftime("%Y %m %d") # 小寫m => 月份 , 大寫M => 分鐘
print(a)

#日期時間轉換
b=datetime.datetime(2021,10,10,10,10,10)
print(b)