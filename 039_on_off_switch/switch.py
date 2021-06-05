from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_Switch.kv')

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        if switchValue:
            self.ids.my_label.text = "Switch is on"
        else:
            self.ids.my_label.text = "Switch is off"
            self.ids.my_switch.disabled = True
class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
