# Install required libraries
# pip install requests
# pip install beautifulsoup4

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

allRoundRows

len(allRoundRows)

# allRoundRows is a list of lists. Contains 24 lists, one for each
# round with each containing the <tr> of the round table as elements.
# So... I want to make a new list of lists. One that contains 24 lists,
# one for each round containing the text of each game row.
rowText = allRoundRows[0][2].text

if re.search(pattern, rowText):
    print("Found a match")
else:
    print("No match found")

header = [
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

data = []

capturedColumns = re.search(pattern, rowText)
row_list = []
day = capturedColumns.group(1)
date = capturedColumns.group(2)
time = capturedColumns.group(3) + " " + capturedColumns.group(4)
team1name = capturedColumns.group(5)
team1score = capturedColumns.group(6)
team1_win_status = capturedColumns.group(7)
team2name = capturedColumns.group(8)
team2score = capturedColumns.group(9)
location = capturedColumns.group(10)
attendance = capturedColumns.group(11)

row_list = [
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
