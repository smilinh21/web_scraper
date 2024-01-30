import requests
# Beautiful Soup is a Python librart for parsing structured data
from bs4 import BeautifulSoup 

URL = 'https://pythonjobs.github.io/'
page = requests.get(URL)

# create a Beautiful Soup object
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('section', class_='job_list')

python_jobs = results.find_all('h1', string=lambda text: 'python' in text.lower())

python_job_elements = [python_job.parent for python_job in python_jobs]

for job_elm in python_job_elements:
    title = job_elm.find('h1').text
    location = job_elm.find('span', class_="info")
    company = location.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    link = job_elm.find('a', class_='go_button')['href']
    print(title)
    print(location.text)
    print(company.text)
    print(f'Read more: {link}')
    print()
