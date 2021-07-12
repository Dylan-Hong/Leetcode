# github test
# Update 
import pandas as pd
import requests

TargetDate = '20200501'
TargetStockNo = '0050'
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=" + TargetDate + "&stockNo=" + TargetStockNo

data = pd.read_html( requests.get( url ).text )[ 0 ]
# 都用index
print( data.iat[ 0, 6 ] )
# 確認columns的名稱
# print( data.columns )
# 指定完整column名稱
print( data[ '109年05月 0050 元大台灣50 各日成交資訊',  '收盤價' ][ 0 ] )
# 輸出column的第一個element的字串
print( data.columns[ 0 ][ 0 ] )
# 直接load第一個字串進來，就可以call到對應的column了
print( data[ data.columns[ 0 ][ 0 ],  '收盤價' ][ 0 ] )
print( data[ data.columns[ 0 ][ 0 ],  '日期' ][ 0 ] )
writer = pd.ExcelWriter( './practice/xlsfile/' + 'test' + '.xlsx', engine='openpyxl' )

data.to_excel( writer, sheet_name = '0050' )
writer.save()
