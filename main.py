import requests

def get_elevation_data(locations):
    base_url = "https://api.open-elevation.com/api/v1/lookup"
    locations_param = "|".join([f"{lat},{lng}" for lat, lng in locations])
    response = requests.get(base_url, params={"locations": locations_param})
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

route1 = [
    (53.2000, 22.5000),
    (53.2100, 22.5100),
    (53.2200, 22.5200),
    (53.2300, 22.5300),
    (53.2400, 22.5400),
    (53.2500, 22.5500)
]

route2 = [
    (50.4500, 18.2000),
    (50.4600, 18.2100),
    (50.4700, 18.2200),
    (50.4800, 18.2300),
    (50.4900, 18.2400),
    (50.5000, 18.2500)
]
route3 = [
    (49.2700, 19.8500),
    (49.2800, 19.8600),
    (49.2900, 19.8700),
    (49.3000, 19.8800),
    (49.3100, 19.8900),
    (49.3200, 19.9000)
]
route4 = [
    (54.2000, 18.0000),
    (54.2100, 18.0100),
    (54.2200, 18.0200),
    (54.2300, 18.0300),
    (54.2400, 18.0400),
    (54.2500, 18.0500)
]
route5 = [
    (52.2300, 21.0100),
    (52.2400, 21.0200),
    (52.2500, 21.0300),
    (52.2600, 21.0400),
    (52.2700, 21.0500),
    (52.2800, 21.0600)
]

elevation_results1 = get_elevation_data(route1)
elevation_results2 = get_elevation_data(route2)
elevation_results3 = get_elevation_data(route3)
elevation_results4 = get_elevation_data(route4)
elevation_results5 = get_elevation_data(route5)

print("\nRoute 1:\n")
for result in elevation_results1:
    elevation = result.get('elevation', 'Unknown')
    print(f"Elevation: {elevation} meters")

print("\nRoute 2:\n")
for result in elevation_results2:
    elevation = result.get('elevation', 'Unknown')
    print(f"Elevation: {elevation} meters")

print("\nRoute 3:\n")
for result in elevation_results3:
    elevation = result.get('elevation', 'Unknown')
    print(f"Elevation: {elevation} meters")

print("\nRoute 4:\n")
for result in elevation_results4:
    elevation = result.get('elevation', 'Unknown')
    print(f"Elevation: {elevation} meters")

print("\nRoute 5:\n")
for result in elevation_results5:
    elevation = result.get('elevation', 'Unknown')
    print(f"Elevation: {elevation} meters")

# TODO
# save coordinates and elevation into file / proper solution
