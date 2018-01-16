from bs4 import BeautifulSoup
import urllib2
import re
import sys
from datetime import datetime as date
import argparse

parser = argparse.ArgumentParser(description='Fetch flights info for Airports')
parser.add_argument('--all', dest='show_all', action='store_true',default=False, help='List all flights, skip filtering')
parser.add_argument('--airports', dest='airports', default=['CYUL'], help='List of airports to fetch flights from, space separated', nargs='+')
args = parser.parse_args()
show_all=args.show_all
airports=args.airports

current_day=date.today().strftime("%a")
fa_base_url='http://flightaware.com/live/airport/'
fa_phases= [['ARRIVALS',"/enroute?;offset=%s;order=estimatedarrivaltime;sort=ASC"],
        ['DEPARTURE',"/scheduled?;offset=%s;order=filed_departuretime;sort=ASC"]]
planes=['B748','B744','B742','A340','A343','A345','A380','B77W','A333','MD11']
liveries=['RAM','RJA','UAE','KLM','BAW','DLH','DAH','DLX','SWR','RZO','CUB']

def print_flights(fa_phase,flight_info):
    flight_number = flight_info[0].get_text().encode('utf-8').strip()
    plane_type = flight_info[1].get_text().encode('utf-8')

    if fa_phase == "ARRIVALS":
        date = flight_info[5].get_text().encode('utf-8')
    else:
        date = flight_info[3].get_text().encode('utf-8')

    print "\t".join([flight_number, plane_type, date])

for airport in airports:
    print airport
    for fa_phase in fa_phases:
        fa_offset=0
        is_current_day= True
        print fa_phase[0]
        print "FLIGHT\tTYPE\tTIME"
        while is_current_day:
            fetch_url=fa_base_url + airport + fa_phase[1] %fa_offset
            flights = BeautifulSoup(urllib2.urlopen(fetch_url), 'html.parser').find('table', attrs={'class': 'prettyTable fullWidth'})
            flights_rows = flights.find_all('tr')
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
                    elif flight_info[1].get_text() in planes or liverie in liveries:
                        print_flights(fa_phase[0],flight_info)
                    if not re.search(r"^%s\s" % current_day, flight_info[3].get_text()):
                        is_current_day= False
            fa_offset += 20
