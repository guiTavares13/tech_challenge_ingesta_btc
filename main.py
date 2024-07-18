from connection import Connection
from scraper_btc import Scraper
from datetime import datetime
import json
import time

coin = 'bitcoin'
url = 'https://www.google.com/search?q=' + coin + 'price'
stream_name = 'firehosebtcstream'

conn = Connection()
scraper = Scraper(url)

while True:
    now = datetime.now()
    coleta = now.strftime("%Y-%m-%d %H:%M:%S")
    price = scraper.scrape()
    record = {
        "price": price,
        "coleta": coleta
    }
    record_json = json.dumps(record) + "\n" 
    
    print("Registro JSON:", record_json)
    
    send = conn.firehose.put_record(
        DeliveryStreamName=stream_name,
        Record={
            'Data': record_json
        }
    )
    print("Resposta do Firehose:", send, "Preço:", price, "Coleta:", coleta)
    time.sleep(5)
