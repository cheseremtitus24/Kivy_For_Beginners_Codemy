from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
''' To assign the initial window size, insert the next code snippet right above
the line that reads:
#from kivy.core.window import Window
its critical to apply these settings before the Window object is even imported;
othewise, the won't have any effect
'''

# set default size and disable resizability
from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '300')

#disable window resizing
Config.set('graphics', 'resizable', '0')

#disable multitouch Emulation
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.core.window import Window

#Design Our .kv design file
Builder.load_file('design.kv')

class MyLayout(Widget):
    pass

class SplittersApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    SplittersApp().run()
