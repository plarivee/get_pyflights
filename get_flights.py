from bs4 import BeautifulSoup
import urllib2
import re
import sys
from datetime import datetime as date


if len(sys.argv) > 1:
    show_all= True
else:
    show_all = False
    
current_day=date.today().strftime("%a")
fa_base_url='http://flightaware.com/live/airport/'
fa_phases=[['ARRIVALS',"/enroute?;offset=%s;order=estimatedarrivaltime;sort=ASC"],['DEPARTURE',"/scheduled?;offset=%s;order=filed_departuretime;sort=ASC"]]
airports=['CYUL','CYMX']
planes=['B748','B744','B742','A340','A343','A345','A380','B77W','A333','MD11']
liveries=['RAM','RJA','UAE','KLM','BAW','DLH','DAH','DLX','SWR','RZO','CUB']

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
                if not flight_row.find_all('th'):
                    flight_info = flight_row.find_all('td')
                    try:
                        liverie= re.search(r'^(\w{3})', flight_info[0].get_text().strip()).group(1)
                    except:
                        pass
                    if show_all:
                        if fa_phase == "ARRIVALS":
                            print flight_info[0].get_text().strip() + "\t" + flight_info[1].get_text() + "\t"  + flight_info[5].get_text()
                        else:
                            print flight_info[0].get_text().strip() + "\t" + flight_info[1].get_text() + "\t"  + flight_info[3].get_text()
                    elif flight_info[1].get_text() in planes or liverie in liveries:
                        if fa_phase == "ARRIVALS":
                            print flight_info[0].get_text().strip() + "\t" + flight_info[1].get_text() + "\t"  + flight_info[5].get_text()
                        else:
                            print flight_info[0].get_text().strip() + "\t" + flight_info[1].get_text() + "\t"  + flight_info[3].get_text()
                    if not re.search(r"^%s\s" % current_day, flight_info[3].get_text()):
                        is_current_day= False
            fa_offset += 20
