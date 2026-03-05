import requests
from bs4 import BeautifulSoup
import csv


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
        description_div = div.find('div', class_='s-post-summary--content-excerpt')
        description = description_div.text.strip() if description_div else ''
        questions.append({'title': title, 'description': description})

filename = "qustions.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Question Title", "Description"])
    for question in questions:
        writer.writerow([question['title'], question['description']])
print(f"Questions have been saved to {filename}")


from send_email import send_csv_email

sender_email =  "cursormohit23@gmail.com"
sender_password = "mhrh jehm tjql cgck"     
recipient_email = "mohit.radkrishnan@gmail.com"     

send_csv_email(filename, sender_email, sender_password, recipient_email)
