import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
from typing import Tuple
import numpy as np
from time import sleep

df = pd.read_csv('https://raw.githubusercontent.com/barissayil/beautifulworld/master/beautifulworld/worldcities.csv')

class City():
	def __init__(self, name: str):
		self.name = name
		self.df = df.loc[df['city'] == self.name].iloc[0]
		self.country = self.df['country']
		self.population = int(self.df['population'])
		self.latitude = self.df['lat']
		self.longitude = self.df['lng']
		soup = self.get_soup()
		self.time = soup.find(id='ct').getText()
		self.date = soup.find(id='ctdat').getText()
		self.currency = str(soup.find(string='Currency: ').parent.next_sibling.text)
		self.temperature = soup.find(id='wt-tp').getText()
		self.weather = str(next(soup.find(id='curwt').next_sibling.next_sibling.next_sibling.descendants))
	def __repr__(self) -> str:
		text = f"{self.name}, {self.country}\n"
		text += f"Time: {self.time}\n"
		text += f"Date: {self.date}\n"
		text += f"Weather: {self.weather}\n"
		text += f"Temperature: {self.temperature}\n"
		text += f"Population: {self.population}\n"
		text += f"Currency: {self.currency}\n"
		text += f"Coordinates: ({self.latitude}, {self.longitude})"
		return(text)
	def get_soup(self) -> BeautifulSoup:
		name = ''
		for i in range(len(self.name)):
			if self.name[i] == ' ':
				name += '-'
			else:
				name += self.name[i]
		if self.country == 'United Kingdom':
			country = 'UK'
		elif self.country == 'United States':
			country = 'USA'
		else:
			country = self.country
		URL = f'https://www.timeanddate.com/worldclock/{country}/{name}'
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		return soup
	def climate_graph(self):
		name = ''
		for c in self.name:
			if c == ' ':
				name += '_'
			else:
				name += c
		if name == 'new_york':
			name = 'new_york_city'
		URL = f'https://www.holiday-weather.com/{name}/averages/'
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		soup = soup.find_all("div", class_="averages_table-wrap")[1]
		soup = soup.find_all("tr")
		months = soup[0]
		temp_high = soup[1]
		temp_high_f = soup[2]
		temp_low = soup[3]
		temp_low_f = soup[4]
		months = months.find_all("th")[1:]
		temp_high = temp_high.find_all("td")[1:]
		months = [month.text for month in months]
		temp_high = [int(each_temp_high.text) for each_temp_high in temp_high]
		data = pd.DataFrame(temp_high, months, columns=[self.name])
		sns.lineplot(data=data, palette="tab10", linewidth=2.5, sort=False)
		sleep(.2)

def climateGraph(*cities: Tuple[City]):
	temp_high_list = []
	for city in cities:
		name = ''
		for c in city.name:
			if c == ' ':
				name += '_'
			else:
				name += c
		if name == 'new_york':
			name = 'new_york_city'
		URL = f'https://www.holiday-weather.com/{name}/averages/'
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		soup = soup.find_all("div", class_="averages_table-wrap")[1]
		soup = soup.find_all("tr")
		months = soup[0]
		temp_high = soup[1]
		temp_high_f = soup[2]
		temp_low = soup[3]
		temp_low_f = soup[4]
		months = months.find_all("th")[1:]
		temp_high = temp_high.find_all("td")[1:]
		months = [month.text for month in months]
		temp_high = [int(each_temp_high.text) for each_temp_high in temp_high]
		temp_high_list.append(temp_high)
		sleep(.2)
	temp_high = np.array(temp_high_list)
	temp_high = temp_high.transpose()
	data = pd.DataFrame(temp_high, months, columns=[city.name for city in cities])
	sns.lineplot(data=data, palette="Set1", linewidth=2.5, sort=False)