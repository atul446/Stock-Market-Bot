import os
import requests
import json

api_key = os.environ.get("marketapi")
base_url = "http://api.marketstack.com/v1/"

def get_stock_price(stock_symbol):
    params = {
        'access_key' : api_key
    }
    end_point = ''.join([base_url, "tickers/", stock_symbol, "/intraday/latest"])
    api_result = requests.get(end_point, params)
    json_result = json.loads(api_result.text)
    return json_result
