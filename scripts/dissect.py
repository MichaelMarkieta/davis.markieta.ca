import csv

trips_from_station = {}
trips_to_station = {}
trips_by_bike = {}
 
with open("../hackbikesharetoronto/trips.csv", 'r') as f:
    rows = csv.reader(f)
    header = rows.next()

    for row in rows:
        
        if row[4] not in trips_from_station:
            trips_from_station[row[4]] = [header]

        if row[7] not in trips_to_station:
            trips_to_station[row[7]] = [header]

        if row[8] not in trips_by_bike:
            trips_by_bike[row[8]] = [header]

        trips_from_station[row[4]].append(row)
        trips_to_station[row[7]].append(row)
        trips_by_bike[row[8]].append(row)

for k,v in trips_from_station.iteritems():
    with open("../data/trips_from_station_" + k + ".csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(v)

for k,v in trips_to_station.iteritems():
    with open("../data/trips_to_station_" + k + ".csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(v)

for k,v in trips_by_bike.iteritems():
    with open("../data/trips_by_bike_" + k + ".csv", 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(v)