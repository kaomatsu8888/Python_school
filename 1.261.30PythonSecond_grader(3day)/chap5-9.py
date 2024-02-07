from datetime import datetime, timedelta, timezone # datetimeは日付と時刻を扱うモジュール、timedeltaは日付と時刻の計算を行うモジュール、timezoneはタイムゾーンを扱うモジュール

# UTC(協定世界時)をJST(日本標準時)に変換する関数
timestamp = 1 # 2019年7月12日0時0分0秒

tz = timezone(timedelta()) # タイムゾーンをUTCとして設定
utc = datetime.fromtimestamp(timestamp, tz) # UTCの時間を取得
print(utc) # UTCの時間を表示

tz = timezone(timedelta(hours=9), "JST") # タイムゾーンをJSTとして設定
jst = datetime.fromtimestamp(timestamp, tz) # JSTの時間を取得
print(jst) # JSTの時間を表示
print(str(jst)[:-9]) # JSTの時間を表示
