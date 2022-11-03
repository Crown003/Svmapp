from kivy.uix.screenmanager import Screen
from Modules.db import p
from ..Widget.Listitem import ListItemWithIcon


list_color= "white" 
class Physics_notes(Screen):
	def add_list_items(self):
		for i in range(len(p)):
			self.ids.Mathlist.add_widget(ListItemWithIcon(text=p[i],icon="file-pdf"))
	def on_enter(self):
		self.add_list_items()
	def on_leave(self):
		self.ids.Mathlist.clear_widgets()