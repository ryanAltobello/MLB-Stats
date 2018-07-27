from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

all_seasons_url = 'https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_seasons'
# opening up connection grabbing the page
seasons_url = uReq(all_seasons_url)
# offload content into variable
page_html = seasons_url.read()
# close connection
seasons_url.close()
# html parsing
page_soup = soup(page_html, "html.parser")
"""
decade_table = page_soup.findAll("table", {"class": "wikitable"})
decades = decade_table[0]

for decades in decade_table:
    row = decades.findAll("tr")
    rows = row[0]
    for rows in row:
        a = rows.find("a")
        if a is not None:
            get_year_link = a.get("href")
            new_year_link = "https://en.wikipedia.org" + get_year_link
            print(new_year_link)

            year_url = uReq(new_year_link)
            page_html2 = year_url.read()
            year_url.close()
            page_soup2 = soup(page_html2, "html.parser")
            team_table = page_soup2.find("table", {"class": "wikitable"})
            find_team_link = team_table.find()
            print(team_table)
            """


year_url = uReq('https://en.wikipedia.org/wiki/1876_Major_League_Baseball_season')
page_html2 = year_url.read()
year_url.close()
page_soup2 = soup(page_html2, "html.parser")
team_table = page_soup2.find("table", {"class": "wikitable"})
find_team_link = team_table.findAll("tr")
teams = find_team_link[0]
for teams in find_team_link:
    td = teams.find("td")
    if td is not None:
        a2 = td.a
        get_year_link2 = a2.get("href")
        new_year_link2 = "https://en.wikipedia.org" + get_year_link2
        print(new_year_link2)


"""
filename = "baseballinfo.csv"
f = open(filename, "a")

for name, club in zip(player, flag):

    print(origin_country, player_name, club_team)
    f.write(club_team + "," + origin_country + "," + player_name + "\n")
f.close()
"""
