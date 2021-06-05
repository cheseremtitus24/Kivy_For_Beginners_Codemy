from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_markup.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
