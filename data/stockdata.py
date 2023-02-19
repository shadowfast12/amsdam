import requests
import csv


class StockDay:
    # key of data_set is time in year, month, day, and time in a 24hr clock
    # value of data_set is [open, high, low, close, volume]
    data_set = {}

    # init the stock symbol and convert the data into the data_set dict
    def __init__(self, api_key: str, symbol: str, slice_year: int, slice_month: int, interval: int):
        res_data = list(
            csv.reader((requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&"
                                     "symbol=" + symbol + "&interval=" + str(interval) + "min&slice=year" + str(
                slice_year) + "month" + str(slice_month) + "&apikey=" + api_key)).content.decode("utf-8").
                       splitlines(), delimiter=","))

        for row in res_data[1:]:
            self.data_set[int(str(row[0]).split()[0].replace("-", "") + str(row[0]).split()[1].replace(":", ""))] \
                = [float(i) for i in row[1:]]

    def getdata(self):
        return self.data_set
