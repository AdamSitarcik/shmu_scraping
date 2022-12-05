import requests
from bs4 import BeautifulSoup
import dateutil.parser as dparser
import pandas as pd

page = requests.get('https://www.shmu.sk/sk/?page=1&id=meteo_apocasie_sk')
soup = BeautifulSoup(page.content, 'html.parser')

stations = {'ba':'Bratislava Ivanka', 'mj':'Malý Javorník', 'br':'Brezno'}
output_datafile = {}
station_info = {}

datetime_string = soup.find('caption').get_text()
datetime = dparser.parse(datetime_string, fuzzy=True)

for station in stations.keys():
    station_info[station] = soup.find('td', string=stations[station]).find_parent('tr').find_all('td') # find all td elements which are children of tr element
    df = pd.DataFrame({
                        'datetime':datetime,
                        'temperature':float(station_info[station][1].get_text().split(' ')[0]), # extract float from the string
                        'pressure':float(station_info[station][5].get_text().split(' ')[0]), # extract float from the string
                        'clouds':[station_info[station][6].get_text()],
                        'visibility':[station_info[station][7].get_text()]
                    })
    df.to_csv('/home/adam/skola/tutorialy/python/data_anal/web_scraping/data_'+station+'.csv', mode='a', index=False, header=False)