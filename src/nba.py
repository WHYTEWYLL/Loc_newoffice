import requests
from bs4 import BeautifulSoup

r = requests.get('https://state.1keydata.com/nba-teams-by-state.php',verify=False)
soup = BeautifulSoup(r.text)
country_with_nba_team=[x.find_all("td")[0].text  for x in soup.select(".content3")[0].find_all("tr")[2:]]