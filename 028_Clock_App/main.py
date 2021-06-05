# File: main.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.text import LabelBase #use to define custome font
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock
import datetime


#Design Our .kv design file
#Builder.load_file('clock.kv')


class MyLayout(Widget):
    pass
class ClockApp(App):
    sw_started = False
    sw_seconds = 0
    
    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0

    #Method to display time on-screen 
    def update_time(self,nap):
        self.root.ids.time.text = datetime.datetime.now().strftime('[b]%H[/b]:%M:%S')
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %        (int(minutes), int(seconds), int(seconds * 100 % 100)))

    # Function to schedule the function to run once per second
    def on_start(self):
        Clock.schedule_interval(self.update_time,0)

    def build(self):
        return MyLayout()

#
if __name__ == '__main__':
    # Clearing Window Color
    Window.clearcolor = get_color_from_hex('#101216')

    #Defining our Roboto font_family importing from the font directory
    LabelBase.register(name='Roboto',
            fn_regular='roboto/Roboto-Thin.ttf',
            fn_bold='roboto/Roboto-Medium.ttf')

    ClockApp().run()
