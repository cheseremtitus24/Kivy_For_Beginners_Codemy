from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_spinner.kv')

class MyLayout(Widget):

    def spinner_clicked(self, value):
        print(value)
        self.ids.click_label.text = "You have selected: {select}".format(select=value)

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
