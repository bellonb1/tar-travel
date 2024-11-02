from bs4 import BeautifulSoup
import requests

url = 'https://mycarolina.unc.edu/portal/study_abroad_preapproved_courses'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

soup.find('program_id')

