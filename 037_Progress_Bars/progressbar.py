from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Design Our .kv design file
Builder.load_file('design_progressbar.kv')

class MyLayout(Widget):
    def press_it(self):
        #Grab the current_value progress bar value
        current_value = self.ids.my_progress_bar.value
        # if Statement to start over after 100
        if current_value == 1:
            current_value = 0

        # increment progress bar value by .25
        current_value += .25
        #update progress bar 
        self.ids.my_progress_bar.value = current_value
        #update %age label
        self.ids.my_label.text = f'{int(current_value*100)}'

class ProgressBarApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ProgressBarApp().run()
