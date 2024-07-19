import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", id="main_table_countries_today")

rows = table.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    print(*cols)