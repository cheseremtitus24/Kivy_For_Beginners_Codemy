from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_checkbox.kv')

class MyLayout(Widget):
    checks = []

    def checkbox_click(self, instance, value, topping):
        # instance is the chckbx object addrss
        # value is boolean either True/False
        if value == True:
            MyLayout.checks.append(topping)
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'
            self.ids.output_label.text = f'You selected : {tops}'
        else:
            MyLayout.checks.remove(topping)
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'

            self.ids.output_label.text = f'You selected : {tops}'
            


            

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
