import requests
from bs4 import BeautifulSoup


# Getting FaceIt ID
steam_url = "https://steamcommunity.com/id/ramoyasalame/"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

data = {
    'name': steam_url
}

response = requests.post('https://faceitfinder.com/profile/', headers=headers, data=data)

faceit_id = ''.join([x for x in response.content.decode() if x.isdigit()])

# Getting FaceIt Data
response_html = requests.get('https://faceitfinder.com/profile/' + faceit_id, headers=headers)

response_html_soup = BeautifulSoup(response_html.content, 'html.parser')
url = response_html_soup.find_all("a", href=True)

faceit_url = [x["href"] for x in url if "https://www.faceit.com/" in str(x["href"]) and "csgo" not in str(x["href"])][0]

faceit_description = response_html_soup.find_all("meta")[::-1][0]["content"]

skill_image_url = "https://faceitfinder.com" + [x["src"] for x in response_html_soup.find_all("img") if "skill_level" in str(x["src"])][0]
