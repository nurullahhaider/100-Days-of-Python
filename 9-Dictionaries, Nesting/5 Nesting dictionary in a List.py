# Nesting dictionary in a List Python Program
travel_log = [
    { "country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    { "country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},]

def add_country(countries,visit_time,cities_visit):
    new_country={}
    new_country ["country"] = countries
    new_country["visits"]= visit_time
    new_country["cities"] = cities_visit
    travel_log.append(new_country)

add_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print key value pairs
print(travel_log)
print()
for item in travel_log:
    for key,value in item.items():
        print(key+": ", value)
        
# output:
# [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]
# 
# country:  France
# visits:  12
# cities:  ['Paris', 'Lille', 'Dijon']
# country:  Germany
# visits:  5
# cities:  ['Berlin', 'Hamburg', 'Stuttgart']
# country:  Russia
# visits:  2
# cities:  ['Moscow', 'Saint Petersburg']

