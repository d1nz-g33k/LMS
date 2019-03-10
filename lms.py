from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
# from kivymd.MDtable import Table

import time

import requests
from bs4 import BeautifulSoup
import html5lib
from lxml import html
from pyquery import PyQuery

class Asteroids(Widget):
	velocity_x = NumericProperty(1500)
	velocity_y = NumericProperty(0)
	v = ReferenceListProperty(velocity_x, velocity_y)
	def passage(self):
		self.pos = Vector(*self.v) + self.pos

class Milkyway(Widget):
	#C = ObjectProperty(None)
	i = 0
	sub = list()
	at = list()
	batch = list()
	category = list()
	course = list()

	def Get(self):
		url = 'http://lms.bmu.edu.in/login/index.php'

		with requests.Session() as s:
			r = s.post(url, data = {'username': 'dinesh.sai.16cse', 'password': 'D1nz-3943'})
			r.content

			# p = s.get("http://lms.bmu.edu.in/local/dashboard/index.php")
			q = s.get("http://lms.bmu.edu.in/mod/attendance/myattendance.php?studentid=2186")
			p = s.get("http://lms.bmu.edu.in/my")

			tree = html.fromstring(q.content)
			self.sub = tree.xpath('//a[@class="panel-title"]/text()')
			self.at = tree.xpath('//td[@class="centeralign cell c0"]/text()')
			# print (at)
			# print(sub)
			tree2 = html.fromstring(p.content)
			self.batch = tree2.xpath('//h2[@class="batch-heading"]/text()')
			self.category = tree2.xpath('//h2[@class="semester-heading"]/text()')
			self.course = tree2.xpath('//h2[@class="title"]//a/@title')
			# print(self.course)

			# soup = BeautifulSoup(p.content, 'html.parser')

		# file = open('text.txt', 'w')
		# file.write(p.text)
		# file.close()
		# return sub, at

	# def add_table(self,id,list,at):
	# 	# from MDTable import Table
	# 	id.add_widget(Table(table_content=list))

	def on_touch_up(self, touch):
		if(self.i==0 and touch.x>self.a.center_x-70 and touch.x<self.a.center_x+70 and touch.y>self.a.center_y-15 and touch.y<self.a.center_y+15):
			self.i += 1
			print("start")
			self.Get()
			print("done")
			self.clear_widgets()
			# z=dict()
			k=[None] * len(self.sub)
			for x in range (0,len(self.sub)):
				t = str(self.sub[x]).split('(Attendance)')
				t = str(t[0]).split(':')
				if(len(t)==3):
					t[0] = t[2]
				if(str(t[0])=='CSE-4'):
					t[0] = t[1]

				k[x] = str(t[0])
				# z[k[x]] = self.at[x]
			# thead = list()
			# for j in z.keys():
				# thead.append(j)
			# print (thead)
			for x in range (0,len(self.sub)):
				# self.add_table(self, k, self.at)
				self.add_widget(Label(text=str(k[x]) + "   " + str(self.at[x]) , font_size='15', center= [self.center_x, self.height-(20*(x+1))]))
		
		elif(self.i==0 and touch.x>self.c.center_x-70 and touch.x<self.c.center_x+70 and touch.y>self.c.center_y-15 and touch.y<self.c.center_y+15):
			self.i += 1
			print("start")
			self.Get()
			print("done")
			self.clear_widgets()
			k=[None] * len(self.course)
			for x in range (0,len(self.course)):
				# t = str(self.sub[x]).split('(Attendance)')
				t = str(self.course[x]).split(':')
				if(len(t)==3):
					t[0] = t[2]
				elif(len(t)==2):
					t[0] = t[1]
				if(str(t[0])=='CSE-4'):
					t[0] = t[1]
				k[x] = str(t[0])

			for x in range (0,len(self.course)):
				# self.add_table(self, k, self.at)
				self.add_widget(Label(text=k[x], font_size='15', center= [self.center_x, self.height-(50*(x+1))]))
		else:
			print("looser")


class Intro(Widget):
	u = ObjectProperty(None)
	v = ObjectProperty(None)

	Mw = Milkyway()

	def Timer(self, dt):
		self.u.passage()


	
	

class lmsApp(App):
	
	def build(self):
		il = Intro()
		layout = BoxLayout(padding=10)
		# root = BoxLayout()
		# il.add_widget(Rectangle, 0)
		Clock.schedule_once(il.Timer, 5)
		# il.Hide()
		# il.Timer()

		return il 
	
	


if __name__ == '__main__':
	lmsApp().run()



