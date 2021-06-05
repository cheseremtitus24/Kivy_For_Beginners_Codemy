from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#For the global window color setup from within the main file you will need to import the following line
from kivy.core.window import Window



#Designate Our .kv design file
Builder.load_file('app_background_color.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
        #Setting a Global color for entire application 
        #Window.clearcolor = (1,0,0,1)
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()
    
