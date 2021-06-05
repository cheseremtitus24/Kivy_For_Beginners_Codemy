from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#Tab class
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.core.window import Window


#Design Our .kv design file
Builder.load_file('design_tab.kv')

class MyLayout(TabbedPanel):
    pass

class windowtabApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    windowtabApp().run()
