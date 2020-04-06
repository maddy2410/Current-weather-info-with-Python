#2670e36a0245cd5cd972e25560958354
#https://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import requests

Weather,_=loadUiType('weather.ui')


class weather(QMainWindow,Weather):


	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.handleButtons()

	def handleButtons(self):
		self.pushButton.clicked.connect(self.display_weather)

	def getting_city(self):
		a=self.lineEdit.text()
		self.lineEdit.setText('')
		self.textEdit.setPlainText('')
		a=a.split(',')
		return a

	def display_weather(self):
		b=self.getting_city()
		weather_key='2670e36a0245cd5cd972e25560958354'
		url='https://api.openweathermap.org/data/2.5/weather'
		params={'APPID':weather_key,'q':b,'units':'Metric'}
		response=requests.get(url,params=params)
		a=response.json()
		b='CITY : {},{}\nCURRENT TEMP : {}\nMAX TEMP : {}  MIN TEMP : {}\nWEATHER TYPE : {}'.format(a['name'],a['sys']['country'],a['main']['feels_like'],a['main']['temp_max'],a['main']['temp_min'],a['weather'][0]['main'])
		self.textEdit.setPlainText(b)


def main():
	app=QApplication(sys.argv)
	window=weather()

	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
