from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image # required for defining images from within the main file
from kivy.core.window import Window # for setting global app back_color

#Designate Our .kv design file
Builder.load_file('app_background_image.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()
    
