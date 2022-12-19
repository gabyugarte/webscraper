import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website and retrieve the HTML
url = "https://www.hosco.com/en/jobs"
response = requests.get(url)
html = response.text

# Step 2: Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Navigate the HTML tree and extract the information
jobs = []
for job_element in soup.find_all("div", class_="JobTileContent__TextWrapper-sc-byt6e7-1 dOJPvm"):
  job_title = job_element.find("a").text
  location = job_element.find("div", class_="JobTileContent__TextLine-sc-byt6e7-3 JobTileContent__Location-sc-byt6e7-5 gpHxGp kkHjRl").text
  duration = job_element.find("div", class_="JobTileContent__TextLine-sc-byt6e7-3 JobTileContent__AdditionalText-sc-byt6e7-6 gpHxGp cYMzwf").text
  jobs.append((job_title, location, duration))

# Step 4: Create a spreadsheet and save the information
import pandas as pd
df = pd.DataFrame(jobs, columns=["Job Title", "Location", "Duration"])
df.to_csv("jobs.csv", index=False)
