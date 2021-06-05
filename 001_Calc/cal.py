from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #allows to set obj properties to design file properties
from kivy.lang import Builder # allows for defining of custom design files
from kivy.core.window import Window # allows for defining of app color theme

# Designate Our kv.design file
Builder.load_file('design_cal.kv') # or ...load_string
Window.size = (400,600)

class MyLayout(Widget):
    def hello_on(self):
        self.ids['my_button'].background_normal  = ''
        self.ids.my_image.source = 'icons/login_down.png'
        self.ids['my_button'].background_color = 0.0, 0.0, 0.0, 0.0
    def hello_off(self):
        self.ids.my_image.source = 'icons/login_normal.png'
        self.ids['my_button'].background_color = 0, 0, 0, 0.0
    def backspace(self):
        prior = self.ids.calc_input.text 
        if len(list(prior)) == 1:
            prior = '0'
        else:
            prior = prior[:-1]
        self.ids.calc_input.text = prior
    def button_press(self,button):
        #create a variable to hold prior text values
        prior = self.ids.calc_input.text


        if prior == 'Error':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text ='{button}'.format(button=button)

        elif prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = '{button}'.format(button=button)


        else:
            self.ids.calc_input.text = '{prior}{button}'.format(prior=prior,button=button)
        

    def clear_all(self):
        self.ids.calc_input.text = '0'

    def equals(self):
        prior = self.ids.calc_input.text
        
        # Error handling for divide by zero


        try:
            # Evaluate Math operations
            # todo: Employ eval security measures
            answer = eval(prior)

            # Output the answer on-screen
            self.ids.calc_input.text = str(answer)
        except :
            self.ids.calc_input.text = "Error"

'''
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0

            #loop through our list
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_input.text = str(answer)
'''

class Awesome(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Awesome().run()
