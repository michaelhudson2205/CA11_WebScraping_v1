# Install required libraries
# pip install requests
# pip install beautifulsoup4

import csv
import re

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/2023_AFL_season"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
response.close()

# pattern = "'\\n(.+day), (\d+ .+) \((\d+:\d+)\\xa0([a,p]m)\)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.+?)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.*?) \(crowd:\\xa0(\d+,\d+)"

pattern = "^\\n(.+day), (\d+ .+) \((\d+:\d+)\\xa0([a,p]m)\)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.+?)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.*?) \(crowd:\\xa0(\d+,\d+)\)\\n\\nReportStats\\n$"

# pattern

# print(soup.prettify())

allTables = soup.find_all("table")

allRoundRows = []

for i in range(4, 28):
    RoundRows = allTables[i].find_all("tr")
    allRoundRows.append(RoundRows)

# allRoundRows is a list of lists. Contains 24 lists, one for each
# round with each containing the <tr> of the round table as elements.
# So... I want to make a new list of lists. One that contains 24 lists,
# one for each round containing the text of each game row.

# Test with only one round from allRoundRows
data = []

for i in range(24):
    for row in allRoundRows[i]:
        rowText = row.text
        if re.search(pattern, rowText):
            #     print("Found a match")
            # else:
            #     print("No match found!")
            m = re.search(pattern, rowText)
            row_list = []
            roundno = str(i + 1)
            day = m.group(1)
            date = m.group(2)
            time = m.group(3) + " " + m.group(4)
            team1name = m.group(5)
            team1score = m.group(6)
            team1_win_status = m.group(7)
            team2name = m.group(8)
            team2score = m.group(9)
            location = m.group(10)
            attendance = m.group(11)
            row_list = [
                roundno,
                day,
                date,
                time,
                team1name,
                team1score,
                team1_win_status,
                team2name,
                team2score,
                location,
                attendance,
            ]
            data.append(row_list)

data

header = [
    "Round",
    "Day",
    "Date",
    "Time",
    "First_Team_Name",
    "First_Team_Score",
    "First_Team_Win_Status",
    "Second_Team_Name",
    "Second_Team_Score",
    "Location",
    "Crowd_Attendance",
]

with open("M_AFL_2023.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

file.close()
