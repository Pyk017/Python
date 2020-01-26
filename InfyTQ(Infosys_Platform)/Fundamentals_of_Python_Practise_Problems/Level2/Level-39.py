"""
Suppose you are given a data structure which is a list of dictionaries as follows:
cities = [
{'Name':'Vancouver','State':'WA','Population':161791},
{'Name':'Salem','State':'OR','Population':154637},
{'Name':'Seattle','State':'WA','Population':608660},
{'Name':'Spokane','State':'WA','Population':208916},
...
]

Complete the function max_in_state to return the city (as a dictionary) with the highest population in a given state.
If the population is a tie then return the city that comes first alphabetically.

If cities contained only the dictionaries above, a call to max_in_state(cities, 'WA') would return:
{'Name':'Seattle','State':'WA','Population':608660}
"""


def max_populated_state(city_dict, state):
    max_populated_city = {}
    temp = 0
    city_dict = sorted(city_dict, key=lambda x: x['Name'])
    for i in city_dict:
        if i['State'] in state:
            if i['Population'] > temp:
                temp = i['Population']
                max_populated_city = i

    return max_populated_city


cities_dict = [
    {'Name': 'Vancouver', 'State': 'WA', 'Population': 161791},
    {'Name': 'Salem', 'State': 'OR', 'Population': 154637},
    {'Name': 'Seattle', 'State': 'WA', 'Population': 80885},
    {'Name': 'Bellingham', 'State': 'WA', 'Population': 608660},
    {'Name': 'Spokane', 'State': 'WA', 'Population': 208916},
    {'Name': 'Bellevue', 'State': 'WA', 'Population': 608660},
    {'Name': 'Portland', 'State': 'OR', 'Population': 583776}
]
states = "WA"
print("The city details are:", cities_dict)
print("State:", states)
output = max_populated_state(cities_dict, states)
print("The highest populated city in the given state is:", output)
