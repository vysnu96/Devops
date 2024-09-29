from bs4 import BeautifulSoup
import requests
import os

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

# Getting the response from the torrent website
try:
    response = requests.get('https://www.1tamilmv.tf/')
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("Website accessed successfully!")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")

# Beautify the response
beauty = BeautifulSoup(response.text, 'html.parser')
# List of styles to ignore
ignore_styles = ["color:#0000ff;", "color:#000099;"]

links = beauty.find_all('a')  # Find all the hyperlinks

hyperlinkCounter = 0  # counter to keep track of no. of films or whatever

# Getting the list of web series, TV Shows and others
generic_list = []
for i, link in enumerate(links):
    if hyperlinkCounter >= 10:
        break
    if i > 34:
        custom_color = link.find('span', style=lambda style: style in ignore_styles if style else False)
        if custom_color:
            continue

        span = link.find('span')
        if span:  # Ensure there's a <span> inside the <a>
            hyperlinkCounter = hyperlinkCounter + 1
            #print(hyperlinkCounter, span.text)
            generic_list.append(span.text)
        else:  # If no <span> exists, extract the direct text inside <a>
            hyperlinkCounter = hyperlinkCounter + 1
            #print(hyperlinkCounter, link.text, hyperlinkCounter)
            generic_list.append(link.text)

# Getting the list of movies in all languages
movies_list = []
p_tags = beauty.find_all('span', style='color:#000000;')
for i, element in enumerate(p_tags):
    if i > 10:
        break
    #print(i, element.text)
    movies_list.append(element.text)

generic_text = ("List of latest 10 series, english movies listed in website. Our data may vary. Please check website "
                "for integrity\n")
movies_text = ("List of latest 10 movies in all languages listed in website. Our data may vary. Please "
               "check website for integrity\n")

generic = generic_text + "\n".join(generic_list)
movies = movies_text + "\n".join(movies_list)

URL = f"https://api.telegram.org/bot{token}/sendMessage"
header = {"Content-Type": "application/json"}

generic_payload = {'chat_id': {chat_id}, 'text': generic}
gen_set = list(generic_payload)
generic_res = requests.post(URL, headers=header, json=gen_set)
#print(generic)
print(generic_res.json())

movies_payload = {'chat_id': {chat_id}, 'text': movies}
mov_set = list(movies_payload)
movies_res = requests.post(URL, headers=header, json=mov_set)
#print(movies)
print(movies_payload, movies_res.json())

