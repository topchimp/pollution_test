# pollution_test

## Contents
* sds011.py - Driver for the SDS 011 pollution monitor
* test.py - Simple calling Python that stores the PM2.5 and PM10 readings in a text file
* parse_GPX_to_CSV.py - Converts a recorded walk exported from Strava as a GPX file to a csv of lat, long and timestamp

## Useful tools used along the way 
* [export-dynamodb](https://pypi.org/project/export-dynamodb/) Python module to export dynamodb data as JSON or CSV that gets around the consloe limit of 100 rows
