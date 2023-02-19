from webull import paper_webull as pw
import data.stockdata as st

api_key = "6PD17LFH92V8TU9P"

kmx = st.StockDay(api_key, "kmx", 1, 1, 15)

print(kmx.getdata())
