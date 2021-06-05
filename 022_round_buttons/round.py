from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder # required for adding custom design file
from kivy.core.window import Window # enable for defining app theme and window size

# Designate Our .kv design file

Builder.load_file('x.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1) # Defining the application theme color
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
