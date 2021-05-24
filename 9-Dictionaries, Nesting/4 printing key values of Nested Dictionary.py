# printing key values of Nested Dictionary
travel_log = {"France": 
    {"cities_visited":["Paris", "Lille", "Dijon"],
    "visits": 12,},
    "Germany":
        {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  "visits": 5,} 
    }
    
#print(travel_log)
for key,value in travel_log.items():
    #print("key ",travel_log[key], " value ", travel_log[value])
    print("country: ",key)
    for key in value:
        print("\t"+key+":",value[key])

# output:        
# country:  France
# 	cities_visited: ['Paris', 'Lille', 'Dijon']
# 	visits: 12
# country:  Germany
# 	cities_visited: ['Berlin', 'Hamburg', 'Stuttgart']
# 	visits: 5
