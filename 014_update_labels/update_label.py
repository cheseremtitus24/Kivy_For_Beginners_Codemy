from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image # required for defining images from within the main file
from kivy.core.window import Window # for setting global app back_color
# Below line will be used in instantiating a float layout
from kivy.uix.floatlayout import FloatLayout


#Designate Our .kv design file
Builder.load_file('label_update.kv')
class MyLayout(Widget):
    
    def press(self):
        #create Variables for our widget
        name = self.ids.name_input.text

        #update the label only if string is greater than 0
            
        self.ids.name_label.text = "Hello {place_holder} !".format(place_holder=name)

            #clear input box
        self.ids.name_input.text = ''


class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()
    
