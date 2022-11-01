#asks a user to input an instagram account username and retuens the image link to that account's profile image
#not working

import requests 
from bs4 import BeautifulSoup as bs

insta_user= input('Input Instagram username:')
url = 'https://instagram.com/'+ insta_user + '/'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(url)