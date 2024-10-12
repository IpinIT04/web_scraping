from bs4 import BeautifulSoup
import requests

url = str(input('URL: '))

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        print(f"Error: received status code  {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request faild : {e}")

def parsing_content(response):
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.find('h1')
    if not title:
        print('Error: no title found')
        return
    content = ' '.join([p.text for p in soup.find_all('p')])
    if not content:
        print("Error: no content found")
        return
    
    with open('text.txt', 'w') as f:
        f.write('Title: ' + title.text + content)

    return print(title.text, content)

response = fetch_html(url)

parsing_content(response)