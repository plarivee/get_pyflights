# get_pyflights
python version of the perl get_flights

It gets the flights from flightware. It's easier to scrape than fr24 when using free version. 

```
python get_flights.py -h
usage: get_flights.py [-h] [--all] [--airports AIRPORTS [AIRPORTS ...]]

Fetch flights info for Airports

optional arguments:
  -h, --help            show this help message and exit
  --all                 List all flights, skip filtering
  --airports AIRPORTS [AIRPORTS ...]
                        List of airports to fetch flights from, space
                        separated
                        
                        
python get_flights.py --airport CYUL
CYUL

ARRIVALS

FLIGHT	TYPE	MANUFACTURER        	NAME                     	TIME
CLH478	A343	AIRBUS              	A-340-300 Prestige       	Tue 04:08PMEDT
EGF3940	E135	EMBRAER             	ERJ-135                  	Tue 04:11PMEDT
AAL3940	E145	EMBRAER             	C-99                     	Tue 04:11PMEDT
CDR627	CL60	BOMBARDIER          	CL-600 Challenger 650    	Tue 04:12PMEDT
PDT4845	E145	EMBRAER             	C-99                     	Tue 04:24PMEDT
DAH2700	A332	AIRBUS              	A-330-200 Voyager        	Tue 04:30PMEDT
ASQ3986	E45X	EMBRAER             	ERJ-145XR                	Tue 04:35PMEDT
FAB865	B732	BOEING              	737-200                  	Tue 04:36PMEDT
SKW3126	CRJ2	CANADAIR            	Challenger 800           	Tue 04:36PMEDT
ACA314	B788	BOEING              	787-8 Dreamliner         	Tue 04:38PMEDT
KLM671	A332	AIRBUS              	A-330-200 Voyager        	Tue 04:46PMEDT
ACA778	B38M	BOEING              	737 MAX 8                	Tue 04:49PMEDT
ACA865	B77W	BOEING              	777-300ER                	Tue 05:11PMEDT
ASP816	E545	EMBRAER             	EMB-545 Legacy 450       	Tue 05:14PMEDT
N595TM	BE9L	BEECH               	90 (A90) King Air        	Tue 05:16PMEDT
N96UJ	FA50	DASSAULT            	Mystère 50                     Tue 05:19PEDT
ASQ4400	E145	EMBRAER             	C-99                     	Tue 05:22PMEDT
N62MV	GLF3	GULFSTREAM AEROSPACE	C-20A Gulfstream 3       	Tue 05:33PMEDT
THY35	A333	AIRBUS              	A-330-300                	Tue 05:41PMEDT
```
                        
