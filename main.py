import requests
import csv
from bs4 import BeautifulSoup

# Mapping function to return the text of a cell
def get_text(cell):
  return cell.get_text()

# Open up our csv
with open('nba_rankings.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')

  # Fetch the html
  nba_url = 'https://www.teamrankings.com/nba/stat/2nd-half-points-per-game?date=2019-11-26'
  nba_rankings_request = requests.get(nba_url)
  if nba_rankings_request.status_code != 200:
    print('FAIL')

  # Pass the html into beautiful soup
  html = nba_rankings_request.content
  soup = BeautifulSoup(html, 'html.parser')

  # Get the table
  table = soup.table

  # Get the table header and append its contents
  table_header = map(get_text, table.find_all('th'))
  writer.writerow(table_header)

  # For each row, append its contents
  table_rows = table.find_all('tr')
  for row in table_rows:
    row_content = map(get_text, row.find_all('td'))
    if len(row_content) > 0:
      writer.writerow(row_content)