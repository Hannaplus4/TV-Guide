import requests
from bs4 import BeautifulSoup

def scrape_disney_tv():
    url = "https://tv.disney.nl/tv-gids"
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    program_titles = []
    for title in soup.find_all('h2', class_='title'):
        program_titles.append(title.text)

    with open('programas_disney.txt', 'w') as f:
        for title in program_titles:
            f.write(title + '\n')

if __name__ == '__main__':
    scrape_disney_tv()
