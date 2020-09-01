import schedule
import time
import requests
from bs4 import BeautifulSoup


def scrap():
    """to scrap web for data"""
    res = requests.get('https://www.worldometers.info/coronavirus/')
    date = res.headers['Date']
    soup = BeautifulSoup(res.content, 'html.parser')
    items = soup.findAll('div', attrs={'class':'maincounter-number'})
    result = [item.text.strip() for item in items]
    print(f"""
    Coronavirus Cases: {result[0]}
    Deaths: {result[1]}
    Recovered: {result[2]}
    @{date}
    """)


schedule.every(5).seconds.do(scrap)

while True:
    time.sleep(1)
    schedule.run_pending()


