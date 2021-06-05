from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_image_button.kv')

class MyLayout(Widget):
    def hello_on(self):
        self.ids['my_button'].background_normal  = ''
        self.ids.my_image.source = 'icons/login_down.png'
        self.ids['my_button'].background_color = 0.0, 0.0, 0.0, 0.0
    def hello_off(self):
        self.ids.my_image.source = 'icons/login_normal.png'
        self.ids['my_button'].background_color = 0, 0, 0, 0.0
        self.ids.my_label.text = "You pressed the button"
    
class ImageButtonApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    #Below main program
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    
    ImageButtonApp().run()
