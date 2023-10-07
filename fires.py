import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "data/world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for i in range(len(header_row)):
        if header_row[i] == "latitude":
            lat_ind = i
        elif header_row[i] == "longitude":
            lon_ind = i
        elif header_row[i] == "brightness":
            brightness_ind = i

    # Get dates and high temperatures from this file
    lats, lons, brightness_values = [], [], []
    for row in reader:
        try:
            lat = row[lat_ind]
            lon = row[lon_ind]
            brightness_value = int(row[brightness_ind])
        except ValueError:
            print(f"Missing data")
        else:
            lats.append(lat)
            lons.append(lon)
            brightness_values.append(brightness_value)

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [brightness / 50 for brightness in brightness_values],
        "color": brightness_values,
        "colorscale": "Magma",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    }
}]
my_layout = Layout(title="World Fires")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")
