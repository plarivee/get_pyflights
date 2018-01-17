from bs4 import BeautifulSoup
import urllib2
import re
import sys
from datetime import datetime as date
import argparse
import pyfscache
import yaml

with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
planes= cfg['planes']
liveries= cfg['liveries']


parser = argparse.ArgumentParser(description='Fetch flights info for Airports')
parser.add_argument('--all', dest='show_all', action='store_true',default=False, help='List all flights, skip filtering')
parser.add_argument('--airports', dest='airports', default=['CYUL'], help='List of airports to fetch flights from, space separated', nargs='+')
parser.add_argument('--cache-timeout', dest='cache_timeout', default=5, help='cache info for this amount of minutes',type=int)
args = parser.parse_args()
show_all=args.show_all
airports=args.airports
fa_page_cache_timeout= args.cache_timeout
fa_page_cache = pyfscache.FSCache('/tmp/get_flights',minutes=fa_page_cache_timeout)

current_day=date.today().strftime("%a")
fa_base_url='http://flightaware.com/live/airport/'
fa_phases= [['ARRIVALS',"/enroute?;offset=%s;order=estimatedarrivaltime;sort=ASC"],
        ['DEPARTURE',"/scheduled?;offset=%s;order=filed_departuretime;sort=ASC"]]

def print_flights(fa_phase,flight_info):
    flight_number = flight_info[0].get_text().encode('utf-8').strip()
    plane_type = flight_info[1].get_text().encode('utf-8')

    if fa_phase == "ARRIVALS":
        date = flight_info[5].get_text().encode('utf-8')
    else:
        date = flight_info[3].get_text().encode('utf-8')

    print "\t".join([flight_number, plane_type, date])

@fa_page_cache
def fetch_page_data(offset, airport, phase):
    fetch_url=fa_base_url + airport + phase %offset
    flights = BeautifulSoup(urllib2.urlopen(fetch_url), 'html.parser').find('table', attrs={'class': 'prettyTable fullWidth'})
    return flights.find_all('tr')

def check_plane(plane_type):
    if plane_type in planes:
        return True
    else:
        return False

def check_liverie(liverie_name):
    if liverie_name in liveries:
        return True
    else:
        return False

def check_still_current_day(current_date):
    if re.search(r"^%s\s" % current_day, current_date):
        return True
    else:
        return False

def show_flights():
    for airport in airports:
        print airport
        for fa_phase in fa_phases:
            fa_offset=0
            is_current_day= True
            print fa_phase[0]
            print "\t".join(["FLIGHT","TYPE","TIME"])
            while is_current_day:
                flights_rows = fetch_page_data(fa_offset,airport,fa_phase[1])
                for flight_row in flights_rows:
                    liverie=None
                    if not flight_row.find_all('th'):
                        flight_info = flight_row.find_all('td')
                        try:
                            liverie= re.search(r'^(\w{3})', flight_info[0].get_text().strip()).group(1)
                        except:
                            pass
                        if show_all:
                            print_flights(fa_phase[0],flight_info)
                        elif check_plane(flight_info[1].get_text()) or check_liverie(liverie):
                            print_flights(fa_phase[0],flight_info)
                        is_current_day = check_still_current_day(flight_info[3].get_text())
                fa_offset += 20

show_flights()
