# csp_mta
Realtime csp input adapter for the MTA's GTFS data feed. Feeds covered are all lines of the New York City subway, LIRR and Metro North railroads

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AdamGlustein/csp_mta/main?urlpath=lab)

Setup:

```
pip install csp httpx protobuf
```

# Example use:

## 1) Subway departure board

The example script `e_01_nyct_subway.py` prints a realtime departure board for a set of platforms. The 'platforms' are specified as a pair of `stop_id:line` combinations. The `stop_id` corresponding to a specific station/service can be found in file `stops.txt`.

For example, at 14 St - Union Square the `stop_id` for the Lexington Ave (4/5/6) line is `635` (35th stop on the 6 line), the `stop_id` for the Broadway line (N/Q/R/W) trains is `R20` (20th stop on the R line), and the `stop_id` for the BMT Canarsie line (L) is `L03`. Thus, to see the next 5 trains for **all** platforms at Union Square, you could run:
```
>> python e_01_nyct_subway.py 635:456 L03:L R20:NQRW --num_trains 5

2024-04-20 00:27:24.166629 Departure Board:
 At station 14 St-Union Sq

Uptown L train to 8 Av in 1 minutes
Downtown L train to Canarsie-Rockaway Pkwy in 1 minutes
Uptown L train to 8 Av in 2 minutes
Uptown L train to 8 Av in 5 minutes
Downtown L train to Canarsie-Rockaway Pkwy in 5 minutes

2024-04-20 00:27:24.187608 Departure Board:
 At station 14 St-Union Sq

Downtown Q train to Coney Island-Stillwell Av in 1 minutes
Uptown W train to Astoria-Ditmars Blvd in 2 minutes
Downtown W train to Whitehall St-South Ferry in 3 minutes
Downtown N train to Coney Island-Stillwell Av in 5 minutes
Uptown R train to Forest Hills-71 Av in 6 minutes

2024-04-20 00:27:24.224544 Departure Board:
 At station 14 St-Union Sq

Uptown 5 train to Eastchester-Dyre Av in 1 minutes
Downtown 6 train to Brooklyn Bridge-City Hall in 2 minutes
Uptown 6 train to Pelham Bay Park in 4 minutes
Uptown 4 train to Woodlawn in 6 minutes
Downtown 6 train to Brooklyn Bridge-City Hall in 8 minutes
```

## 2) Realtime accessibility information

The MTA also exposes realtime accessibility information about elevator/escalator outages at their stations. In `e_02_realtime_accessibility.py` we access this data through a JSON adapter and compute some basic stats on the current state of subway accessibility.

```
>> python e_02_realtime_accessibility.py

2024-04-20 14:32:22.075735 Current Accessibility Status:
Total elevator outages: 26
ADA critical elevator outages: 3
Realtime Accessible Stations: 110 of 472
Average Time per Outage: 139 days
```

## 3) Bus alert panel

Alerts for all MTA services are published as both GTFS and JSON feeds. In `e_03_bus_alerts.py` we leverage the JSON feed to print all current bus alerts.

```
>> python e_03_bus_alerts.py

2024-04-20 16:04:17.556450 Realtime Alerts:
-- B103: B25, B26, B38, B41 B52, and B103 buses may experience delays in the Downton Brooklyn area and will wait out any temporary closures

-- B103: B25, B26, B38, B41, B52 and B103 stops on Joralemon St at Court St and Joralemon St at Adams St are closed

-- B15: Eastbound B15 buses may experience delays near JFK AirTrain and will wait out any temporary closures

-- B16: B16 stops on Ocean Ave between Parkside Ave and Empire Blvd, on Lincoln Rd, and Flatbush Ave at Ocean Ave will be closed
...
```
