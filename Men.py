# Install required libraries
# pip install requests
# pip install beautifulsoup4

import requests
import re
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/2023_AFL_season'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
response.close()

# pattern = "'\\n(.+day), (\d+ .+) \((\d+:\d+)\\xa0([a,p]m)\)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.+?)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.*?) \(crowd:\\xa0(\d+,\d+)"

pattern = "^\\n(.+day), (\d+ .+) \((\d+:\d+)\\xa0([a,p]m)\)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.+?)\\n\\n(.*?) \d+.\d+ \((\d+)\)\\n\\n(.*?) \(crowd:\\xa0(\d+,\d+)\)\\n\\nReportStats\\n$"

pattern

print(soup.prettify())

allTables = soup.find_all('table')
round1 = allTables[4]

roundRows = round1.find_all('tr')
roundRows
print(len(roundRows))
text = roundRows[2].text
# text

if re.search(pattern, text):
    print('Found a match')
else:
    print('No match')

mysearch = re.search(pattern, text)

mysearch
mysearch.groups()
mysearch.group(1)
mysearch.group(2)
