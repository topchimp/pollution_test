import gpxpy
import os
import pandas as pd
import sys
sys.path.append("/usr/local/lib/python3.7/site-packages")

INDIR = r'.'
OUTDIR = r'outdata'


#Start in the input dir
os.chdir(INDIR)

def parsegpx(f):
    points2 = []
    with open("Pollution_walk.gpx", 'r') as gpxfile:
        # print f
        gpx = gpxpy.parse(gpxfile)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    dict = {'Timestamp' : point.time,
                            'Latitude' : point.latitude,
                            'Longitude' : point.longitude,
                            'Elevation' : point.elevation
                            }
                    points2.append(dict)
    return points2   

#Parse the gpx files into a pandas dataframe
files = os.listdir(INDIR)

df2 = pd.concat([pd.DataFrame(parsegpx(f)) for f in files], keys=files)
df3 = pd.DataFrame(df2, columns=['Latitude', 'Longitude', 'Timestamp'])

#Write the data out to a CSV file
os.chdir(OUTDIR)
df3.to_csv('out.csv', index=False, header=False)
