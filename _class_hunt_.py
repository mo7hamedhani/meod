import requests,os
import re
import http.cookies
from bs4 import BeautifulSoup
class GoogleQuey:
	def __init__(self,query:str = None) -> None:
		self.query=query
		match = re.search(r'\d+', query)
		if match:
			op = match.group()
		else:
			op=1
		words = self.query.split()
		filtered_words = [word for word in words if not word.isdigit()]
		hi = ' '.join(filtered_words)
		self.sesion   = requests.Session()
		self.url = f"https://www.google.com/search?q={hi}&start={op}&sourceid=chrome&ie=UTF-8"
		self.response = self.sesion.get(self.url)
		pass
	def getbs4(self):
		responBs = BeautifulSoup(self.response.text, 'html.parser').find_all('a', href = True)
		print(responBs)
		return responBs
