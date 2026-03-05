import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

questions = []
question_divs = soup.find_all('div', class_='s-post-summary')

for div in question_divs:
    title_link = div.find('a', class_='s-link')
    if title_link:
        title = title_link.text.strip()
        questions.append(title)

for question in questions:
    print(question)