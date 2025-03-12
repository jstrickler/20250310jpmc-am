d = {}
d = dict()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
airports['GLA'] = "Glasgow"

print(f"{airports['MCO'] = }")
airports['YCC'] = "Alberta"

print(f"{airports = }")
print(f"{len(airports) = }")

if 'RDU' in airports:
    print("found")
else:
    print("not found")

del airports['MCO']

print(f"{airports = }")

print(f"{airports['YCC'] = }")

print(f"{airports.get('YYC') = }")
print(f"{airports.get('YYC', 'NOPE') = }")

print(f"{airports.setdefault('WAW', 'Warsaw') = }")
print(f"{airports = }")
print()

for code, city in airports.items():
    print(code, city)
print()

for code, city in sorted(airports.items()):
    print(code, city)
print()

for code, city in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, city)
print()

more_airports = {
    'PAR': 'Paris',
    'VZE': 'Venice',
}

# airports.update(more_airports)
airports |= more_airports
print(f"{airports = }")

# dict comprehension
#d = {k:v for k in ITERABLE ...}