#todo:
'''
1. on click of backspace it should change to go_back when textbox is empty
2. implement a button image employing Material design with normal_down feature

'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #allows to set obj properties to design file properties
from kivy.lang import Builder # allows for defining of custom design files
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.core.window import Window # allows for defining of app color theme
from kivy.utils import get_color_from_hex
from kivy.factory import Factory # enables for access of popup widget items

# Designate Our kv.design file
Builder.load_file('design_popup.kv') # or ...load_string
Window.size = (400,600)

class MyLayout(Widget):

    # creating an instance of the Popup once
    login_popup = Factory.MyPopup()
    def open_popup(self):
        self.login_popup.open()
    
    submitlabel = ObjectProperty()
    def hello_on(self):
        self.login_popup.ids['backspace_button'].background_color  = (0,0,0,.55555)
        self.login_popup.ids.my_image.source = 'icons/backspace_normal.png'
    def hello_off(self):
        self.login_popup.ids['backspace_button'].background_color  = (0.7,0.7,0.7,1)
        self.login_popup.ids.my_image.source = 'icons/backspace_down.png'

    def ok_on(self):
        self.login_popup.ids['submit'].background_color  = (0,0,0,.55555)
    def ok_off(self):
        self.login_popup.ids['submit'].background_color  = (0.7,0.7,0.7,1)

    def backspace(self):
        self.hello_on()
        prior = self.login_popup.ids.calc_input.text 
        if prior == 'Enter Pin':
            pass
        else:

            if prior == '':
                prior = 'Enter Pin'
                self.login_popup.ids.clear = "BACK"
            else:
                prior = prior[:-1]

            if prior == '':
                prior = 'Enter Pin'
            self.login_popup.ids.calc_input.text = prior
    def button_press(self,button):
        #create a variable to hold prior text values
        prior = self.login_popup.ids.calc_input.text


        if prior == 'Error':
            self.login_popup.ids.calc_input.text = 'Enter Pin'
            self.login_popup.ids.calc_input.text ='{button}'.format(button=button)

        elif prior == 'Enter Pin':
            self.login_popup.ids.calc_input.text = ''
            self.login_popup.ids.calc_input.text = '{button}'.format(button=button)


        else:
            self.login_popup.ids.calc_input.text = '{prior}{button}'.format(prior=prior,button=button)
        

    def clear_all(self):
        self.login_popup.ids.calc_input.text = '0'


    def equals(self):
        prior = self.login_popup.ids.calc_input.text
        self.ok_on()
        
        # Error handling for divide by zero


        try:
            # Evaluate Math operations
            # todo: Employ eval security measures
            answer = eval(prior)

            # Output the answer on-screen
            self.login_popup.ids.calc_input.text = str(answer)
        except :
            self.login_popup.ids.calc_input.text = "Error"

class Awesome(App):
    def build(self):
        # Create an instance of the Popup once
        return MyLayout()

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')

    Awesome().run()
