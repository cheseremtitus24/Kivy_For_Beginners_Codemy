from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #defining ids
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Defining our different screens that we want to use
class FirstWindow(Screen):# all inherit screen
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager): # Keeps track of all the windows
    pass

#Design Our .kv design file
kv = Builder.load_file('window.kv')


class AwesomeApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    AwesomeApp().run()
