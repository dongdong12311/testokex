import okex.account_api as account
import okex.ett_api as ett
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import json,sys
import traceback
from time import strftime, localtime
from  datetime import datetime
import time
api_key = '3cbbc362-4a31-4f02-8e19-8c8092a7bbd2'
seceret_key = '4FC0928F9E7C73F536FF7334E305FDED'
passphrase = 'dongdong'
spotAPI = spot.SpotAPI(api_key, seceret_key, passphrase, True)


a =strftime('%Y_%m_%d_%H_%M_%S',localtime())
file = open("ETH"+a+".csv",'w+')
file.writelines("last,best_bid,best_ask\n")

while 1:
    try:        
        result = spotAPI.get_specific_ticker('ETH-USDT')
        file.writelines(result['last']+','+result['best_bid']+ ','+result['best_ask'] + '\n')
        time.sleep(0.105)
        print(result['last'])
    except:
        print("error")
        time.sleep(1)
    
file.close()
