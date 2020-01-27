"""
The International Cricket Council (ICC) wanted to do some analysis of international cricket matches held in last 10
years.
Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:

find_matches (country_name): Accepts the country_name and returns the list of details of matches played by that country.

max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which
have won the maximum number of matches in that championship as the value.

find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of
matches in all championships. If both have won equal number of matches, return "Tie".
"""


def find_matches(country_name):
    result_list = []
    for i in match_list:
        if i[:3] == country_name:
            result_list.append(i)

    return result_list


def max_wins():
    d = {}
    lt = []
    for i in match_list:
        l = i.split(':')
        lt.append(l[0])
        d[l[1]] = list(set(lt))

    return d


def find_winner(country1, country2):
    l1 = find_matches(country1)
    l2 = find_matches(country2)
    match = 0
    print(l1, l2)
    for i in l1:
        l = i.split(':')
        match += int(l[-1])

    match2 = 0
    for j in l2:
        l = j.split(':')
        match2 += int(l[-1])

    if match > match2:
        return 'AUS'
    elif match < match2:
        return 'IND'
    return 'Tie'


match_list = ["AUS:CHAM:5:2", "AUS:WOR:2:1", "ENG:WOR:2:0", "IND:T20:5:3", "IND:WOR:2:1", "PAK:WOR:2:0", "PAK:T20:5:1",
              "SA:WOR:2:0", "SA:CHAM:5:1", "SA:T20:5:0"]

print("The match status list details are:", match_list)
print(find_matches('AUS'))
print(max_wins())
print(find_winner('AUS', 'IND'))
